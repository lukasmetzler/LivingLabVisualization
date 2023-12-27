import json
import logging
from kafka import KafkaConsumer
import config
import postgres as pg
from psycopg2 import sql
from column_names import table_column_names
import time

logging.basicConfig(level=logging.DEBUG)

c = config.load_config()
logging.info("Creating KafkaConsumer...")
consumer = KafkaConsumer(
    c.KAFKA_TOPIC,
    bootstrap_servers=[c.KAFKA_BOOTSTRAP_SERVER],
    auto_offset_reset="earliest",
    enable_auto_commit=False,
    group_id="consumer",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)
logging.info("KafkaConsumer created successfully.")
last_insert_time = 0


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
            connection.commit()
            logging.info(f"Data inserted into database: {data}")
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            print(f"Error inserting data into {table_name}:", e)
            connection.rollback()
        finally:
            logging.debug(f"Vor dem Schließen des Cursors für {table_name}")
            if not cursor.closed:
                cursor.close()
            logging.debug(f"Nach dem Schließen des Cursors für {table_name}")


try:
    with pg.postgres_connection() as connection:
        logging.debug("Verbindung erfolgreich hergestellt")

        for message in consumer:
            current_time = time.time()
            elapsed_time = current_time - last_insert_time

            if elapsed_time >= 60:  # Process only if at least 60 seconds have passed
                with connection.cursor() as cursor:
                    for table_name, column_names in table_column_names.items():
                        insert_data_into_table(
                            connection,
                            cursor,
                            table_name,
                            column_names,
                            message.value,
                        )

                last_insert_time = current_time  # Update the last insert time

except Exception as e:
    logging.error(f"An error occurred: {e}")
finally:
    consumer.close()
