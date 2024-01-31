from time import sleep
import json
from kafka import KafkaProducer
import config
import logging
import random
from typing import Dict, List
import signal
import sys
import uuid
import postgres as pg
import column_names as cn
import psycopg2


def stop_producer(signum, frame):
    logging.info("Stopping producer...")
    producer.close()
    db_connection.close()
    sys.exit(0)


def generate_uuid_from_database(
    table_name: str, first_column_name: str, connection
) -> str:
    with connection.cursor() as cursor:
        generated_id = str(uuid.uuid4())

        while is_id_existing(table_name, generated_id, cursor):
            generated_id = str(uuid.uuid4())

    return generated_id


def is_id_existing(table_name: str, id_to_check: str, cursor) -> bool:
    first_column_name = cn.table_column_names[table_name][0]
    query = f"SELECT COUNT(*) FROM {table_name} WHERE {first_column_name} = %s"
    cursor.execute(query, (id_to_check,))
    result = cursor.fetchone()

    return result and result[0] > 0


def generate_random_data(column_names: List[str], connection) -> Dict[str, float]:
    data = {}

    for table, columns in cn.table_column_names.items():
        first_column = columns[0]
        generated_id = generate_uuid_from_database(table, first_column, connection)

        with connection.cursor() as cursor:
            while is_id_existing(table, generated_id, cursor):
                generated_id = generate_uuid_from_database(
                    table, first_column, connection
                )

        data.update(
            {
                column: generated_id
                if column == first_column
                else random.uniform(0, 100)
                for column in columns
            }
        )

    logging.debug("Generated data: %s", data)
    return data


c = config.load_config()
print("Configuration loaded.")
logging.info("Starte den Producer...")
print(f"KAFKA_BOOTSTRAP_SERVER: {c.KAFKA_BOOTSTRAP_SERVER}")

# Stellen Sie die PostgreSQL-Verbindung her
db_connection = psycopg2.connect(
    dbname=c.CONSUMER_POSTGRES_DB,
    user=c.CONSUMER_POSTGRES_USER,
    password=c.CONSUMER_POSTGRES_PASSWORD,
    host=c.CONSUMER_POSTGRES_HOST,
    port=c.CONSUMER_POSTGRES_PORT,
)

producer = KafkaProducer(
    bootstrap_servers=[c.KAFKA_BOOTSTRAP_SERVER],
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

kafka_topic = c.KAFKA_TOPIC
wait_between_iterations = c.PRODUCER_INTERVAL_SECONDS
print("Starting producer loop...")


signal.signal(signal.SIGINT, stop_producer)


while True:
    data_for_tables = {
        table: generate_random_data(columns, db_connection)
        for table, columns in cn.table_column_names.items()
    }
    logging.debug("Data for tables: %s", data_for_tables)
    producer.send(kafka_topic, value=data_for_tables)
    sleep(wait_between_iterations)
