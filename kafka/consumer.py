import json
import logging
from kafka import KafkaConsumer
import config
import postgres as pg
from psycopg2 import sql
from column_names import table_column_names
import fact_column_names as fcn

c = config.load_config()
logging.info("Creating KafkaConsumer...")
consumer = KafkaConsumer(
    c.KAFKA_TOPIC,
    bootstrap_servers=[c.KAFKA_BOOTSTRAP_SERVER],
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="consumer",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)
logging.info("KafkaConsumer created successfully.")


def insert_data_into_table(connection, cursor, table_name, column_names, data):
    if isinstance(data, dict):
        table_data = data.get(table_name, None)
        if table_data is None:
            logging.error(
                f"Table data for '{table_name}' not found in the message. Skipping message."
            )
            return

        values = [table_data.get(column, None) for column in column_names]

        if None in values:
            logging.error(f"Missing required keys in {table_name}. Skipping message.")
            return

        columns_placeholder = (", ").join(column for column in column_names)
        values_placeholder = (", ").join(["%s" for _ in column_names])

        query = f"INSERT INTO {table_name} ({columns_placeholder}) VALUES ({values_placeholder})"

        try:
            logging.debug(f"Vor dem Ausführen von execute für {table_name}")
            cursor.execute(query, values)
            logging.debug(f"Nach dem Ausführen von execute für {table_name}")

            logging.info(f"Data inserted into database: {data}")

        except Exception as e:
            logging.error(f"An error occurred: {e}")
            print(f"Error inserting data into {table_name}:", e)
            connection.rollback()


def insert_into_fact_table(
    connection, cursor, fact_table_name, fact_column_names, data
):
    if isinstance(data, dict):
        # Extract only the values for the fact table
        fact_values = [data.get(column, None) for column in fact_column_names]

        if None in fact_values:
            missing_keys = [
                column
                for column, value in zip(fact_column_names, fact_values)
                if value is None
            ]
            logging.error(
                f"Missing required keys {missing_keys} in {fact_table_name}. Skipping message."
            )
            return

        columns_placeholder = (", ").join(column for column in fact_column_names)
        values_placeholder = (", ").join(["%s" for _ in fact_column_names])

        query = f"INSERT INTO {fact_table_name} ({columns_placeholder}) VALUES ({values_placeholder})"

        try:
            logging.debug(f"Vor dem Ausführen von execute für {fact_table_name}")
            logging.debug(
                f"Inserting data into {fact_table_name}, values: {fact_values}"
            )
            cursor.execute(query, fact_values)
            logging.debug(f"Nach dem Ausführen von execute für {fact_table_name}")

            logging.info(
                f"Data inserted into database: {fact_table_name}, values: {fact_values}"
            )

        except Exception as e:
            logging.error(f"An error occurred: {e}")
            print(f"Error inserting data into {fact_table_name}:", e)
            connection.rollback()


def process_messages():
    try:
        with pg.postgres_connection() as connection:
            logging.debug("Verbindung erfolgreich hergestellt")

            for message in consumer:
                with connection.cursor() as cursor:
                    # Process Dimension Tables
                    for table_name, column_names in table_column_names.items():
                        insert_data_into_table(
                            connection,
                            cursor,
                            table_name,
                            column_names,
                            message.value,
                        )

                    # Process Fact Table
                    for (
                        fact_table_name,
                        fact_column_names,
                    ) in fcn.fact_table_column_names.items():
                        insert_into_fact_table(
                            connection,
                            cursor,
                            fact_table_name,
                            fact_column_names,
                            message.value,
                        )

                connection.commit()

    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        consumer.close()


process_messages()
