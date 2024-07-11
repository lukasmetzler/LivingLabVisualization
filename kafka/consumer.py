import json
import logging
from kafka import KafkaConsumer
import config
import postgres as pg
from column_names import table_column_names
import signal
import sys

c = config.load_config()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def stop_consumer(signum, frame):
    logging.info("Stopping consumer...")
    consumer.close()
    sys.exit(0)


def get_last_inserted_ids(cursor):
    last_inserted_ids = {}
    try:
        for table_name, column_names in table_column_names.items():
            if table_name.startswith("dim_"):
                query = f"SELECT * FROM {table_name} ORDER BY created_at DESC LIMIT 1"
                cursor.execute(query)
                result = cursor.fetchone()
                if result:
                    id_column_name = next(
                        (
                            col
                            for col in column_names
                            if col.endswith("_id") or col.endswith("_uuid")
                        ),
                        None,
                    )
                    if id_column_name:
                        last_inserted_ids[id_column_name] = result[
                            column_names.index(id_column_name)
                        ]
                    else:
                        logger.error(f"No ID column found for table {table_name}")
        return last_inserted_ids
    except Exception as e:
        logger.error(f"An error occurred while retrieving last inserted IDs: {e}")
        return None


def insert_data_into_table(connection, cursor, table_name, column_names, data):
    try:
        if table_name.startswith("dim_") and isinstance(data, dict):
            table_data = data.get(table_name, None)
            if table_data is None:
                logger.error(
                    f"Table data for '{table_name}' not found in the message. Skipping message."
                )
                return None
            filtered_values = [
                table_data.get(column, None)
                for column in column_names
                if not column.endswith("_id") and column != "created_at"
            ]
            filtered_columns = [
                column
                for column in column_names
                if not column.endswith("_id") and column != "created_at"
            ]
            columns_placeholder = ", ".join(filtered_columns)
            values_placeholder = ", ".join(["%s" for _ in filtered_columns])
            query = f"INSERT INTO {table_name} ({columns_placeholder}) VALUES ({values_placeholder})"
            cursor.execute(query, filtered_values)
            logger.info(f"Data inserted into {table_name}")
            return None
    except Exception as e:
        logger.error(f"An error occurred while inserting data into {table_name}: {e}")
        connection.rollback()
        return None


def process_zed_kamera_data(connection, cursor, data):
    try:
        table_name = "dim_zed_body_tracking_1og_r1"
        column_names = table_column_names[table_name]
        filtered_values = [
            data.get(column, None)
            for column in column_names
            if not column.endswith("_id") and column != "created_at"
        ]
        filtered_columns = [
            column
            for column in column_names
            if not column.endswith("_id") and column != "created_at"
        ]
        columns_placeholder = ", ".join(filtered_columns)
        values_placeholder = ", ".join(["%s" for _ in filtered_columns])
        query = f"INSERT INTO {table_name} ({columns_placeholder}) VALUES ({values_placeholder})"
        cursor.execute(query, filtered_values)
        connection.commit()
        logger.info(f"Data inserted into {table_name}")
    except Exception as e:
        logger.error(f"An error occurred while inserting data into {table_name}: {e}")
        connection.rollback()


def process_messages():
    try:
        with pg.postgres_connection() as connection:
            logger.debug("Connection established successfully")
            for message in consumer:
                with connection.cursor() as cursor:
                    if message.topic == "zed_kamera_topic":
                        process_zed_kamera_data(connection, cursor, message.value)
                    else:
                        dimension_ids = {}
                        for table_name, column_names in table_column_names.items():
                            inserted_id = insert_data_into_table(
                                connection,
                                cursor,
                                table_name,
                                column_names,
                                message.value,
                            )
                            dimension_ids[table_name] = inserted_id
                        last_inserted_ids = get_last_inserted_ids(cursor)
                        if not last_inserted_ids:
                            logger.error(
                                "No last inserted IDs found. Skipping fact table insertion."
                            )
                            continue
                        fact_tables = [
                            table_name
                            for table_name in table_column_names.keys()
                            if table_name.startswith("fact_")
                        ]
                        for table_name in fact_tables:
                            column_names = table_column_names[table_name]
                            if column_names:
                                column_names_str = ", ".join(column_names)
                                placeholders = ", ".join(["%s" for _ in column_names])
                                for column_name in column_names:
                                    inserted_id = last_inserted_ids.get(column_name)
                                    if inserted_id is None:
                                        logger.warning(
                                            f"ID for '{column_name}' not found."
                                        )
                                query = f"INSERT INTO {table_name} ({column_names_str}) VALUES ({placeholders})"
                                cursor.execute(
                                    query,
                                    tuple(
                                        last_inserted_ids[col] for col in column_names
                                    ),
                                )
                            else:
                                logger.warning(
                                    f"Column names for table '{table_name}' not found."
                                )
                        connection.commit()
                        logger.info("Dimension tables inserted successfully")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    finally:
        consumer.close()


if __name__ == "__main__":
    consumer = KafkaConsumer(
        c.KAFKA_TOPIC,
        "zed_kamera_topic",  # Add the new topic here
        bootstrap_servers=[c.KAFKA_BOOTSTRAP_SERVER],
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="consumer",
        value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    )
    process_messages()
    signal.signal(signal.SIGINT, stop_consumer)
