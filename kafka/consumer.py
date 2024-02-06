import json
import logging
from kafka import KafkaConsumer
import config
import postgres as pg
from psycopg2 import sql
from column_names import table_column_names

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


def insert_data_into_table(
    connection,
    cursor,
    table_name,
    column_names,
    data,
):
    if isinstance(data, dict):
        table_data = data.get(table_name, None)

        if table_data is None:
            logging.error(
                f"Table data for '{table_name}' not found in the message. Skipping message."
            )
            return

        values = [table_data.get(column, None) for column in column_names]
        id_columns = [column for column in column_names if column.endswith("_id")]
        ids = [(column, values[column_names.index(column)]) for column in id_columns]
        values_only = [value[1] for value in ids]
        column_names_only = [value[0] for value in ids]

        if None in values_only:
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

            # Zusätzlich Daten in fact_user_input_facts einfügen
            if table_name == "fact_sensory":
                desired_ids = [
                    "user_input_mp1_id",
                    "user_input_mp2_id",
                    "user_input_mp3_id",
                    "user_input_mp4_id",
                ]
                user_input_values = [
                    table_data.get(desired_id) for desired_id in desired_ids
                ]
                if None in user_input_values:
                    logging.error(
                        "Missing required keys in fact_user_input_facts. Skipping insertion."
                    )
                else:
                    user_input_columns = ", ".join(desired_ids)
                    user_input_placeholders = ", ".join(["%s" for _ in desired_ids])
                    user_input_query = f"INSERT INTO fact_user_input_facts ({user_input_columns}) VALUES ({user_input_placeholders})"
                    cursor.execute(user_input_query, user_input_values)
                    logging.info("Data inserted into fact_user_input_facts")

        except Exception as e:
            logging.error(f"An error occurred: {e}")
            print(f"Error inserting data into {table_name}:", e)
            connection.rollback()

        zed_body_tracking_value = None
        for value, column_name in zip(values_only, column_names_only):
            if "zed_body_tracking_id" in column_name:
                zed_body_tracking_value = value
                break

        if zed_body_tracking_value is not None:
            print(zed_body_tracking_value)
            insert_sql = "INSERT INTO fact_sensory (zed_body_tracking_id) VALUES (%s)"
            try:
                print(insert_sql)
                print(zed_body_tracking_value)
                cursor.execute(insert_sql, (zed_body_tracking_value,))
                logging.info("Inserted into fact_sensory")
            except Exception as e:
                logging.error(
                    f"An error occurred while inserting into fact_sensory: {e}"
                )


def process_messages():
    try:
        with pg.postgres_connection() as connection:
            logging.debug("Verbindung erfolgreich hergestellt")

            for message in consumer:
                with connection.cursor() as cursor:
                    # Einfügen in Dimensionstabellen
                    for table_name, column_names in table_column_names.items():
                        insert_data_into_table(
                            connection,
                            cursor,
                            table_name,
                            column_names,
                            message.value,
                        )

                    connection.commit()

    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        consumer.close()


process_messages()
