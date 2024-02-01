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
        # Check if the table name starts with 'fact_'
        if table_name.startswith("fact_"):
            # For fact tables, remove the 'fact_' prefix to get the correct key
            fact_table_name = table_name[len("fact_") :]
            table_data = data.get(fact_table_name, None)
        else:
            # For dimension tables, directly use the table_name
            table_data = data.get(table_name, None)

        if table_data is None:
            logging.error(
                f"Table data for '{table_name}' not found in the message. Skipping message."
            )
            return

        values = [table_data.get(column, None) for column in column_names]
        id_columns = [column for column in column_names if column.endswith("_id")]
        ids = [(column, values[column_names.index(column)]) for column in id_columns]

        print("ID columns:", ids)

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
