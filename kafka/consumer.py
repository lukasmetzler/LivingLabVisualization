import json
import logging
from kafka import KafkaConsumer
import config
import postgres as pg
from psycopg2 import sql
from column_names import table_column_names

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


def insert_data_into_table(connection, cursor, table_name, column_names, data):
    if isinstance(data, dict):
        try:
            table_data = data[table_name]
        except KeyError:
            logging.error(
                f"KeyError: '{table_name}' not found in the message. Skipping message."
            )
            return

        values = [table_data.get(column, None) for column in column_names]

        if None in values:
            logging.error(f"Missing required keys in {table_name}. Skipping message.")
            return

        columns_placeholder = sql.SQL(", ").join(
            sql.Identifier(column) for column in column_names
        )

        values_placeholder = sql.SQL(", ").join(
            [sql.Identifier(column) for column in column_names]
        )

        query = sql.SQL(
            f"INSERT INTO {table_name} ({columns_placeholder}) VALUES ({values_placeholder})"
        )

        try:
            print("Generated SQL Query:", query)
            cursor.execute(query, values)
            connection.commit()
            logging.info(f"Data inserted into database: {data}")
            print(f"Data inserted into {table_name}:", data)
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            print(f"Error inserting data into {table_name}:", e)


with pg.postgres_connection() as connection:
    try:
        with connection.cursor() as cursor:
            for message in consumer:
                print("Received message:", message.value)
                for table_name, column_names in table_column_names.items():
                    insert_data_into_table(
                        connection,
                        cursor,
                        table_name,
                        column_names,
                        message.value,
                    )

    except Exception as e:
        logging.error(f"An error occurred: {e}")
