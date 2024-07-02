import json
import logging
import random
import signal
import sys
from time import sleep
from typing import Dict, List
import psycopg2
from kafka import KafkaProducer
import config
import column_names as cn

def stop_producer(signum, frame):
    logging.info("Stopping producer...")
    producer.close()
    db_connection.close()
    sys.exit(0)

def generate_random_data(table_column_names: Dict[str, List[str]]) -> Dict[str, float]:
    data = {}
    for table, columns in table_column_names.items():
        filtered_columns = [column for column in columns if not column.endswith("_id")]
        data[table] = {column: random.uniform(0, 100) for column in filtered_columns}
    logging.debug("Generated data: %s", data)
    return data

def establish_db_connection(configurations):
    return psycopg2.connect(
        dbname=configurations.CONSUMER_POSTGRES_DB,
        user=configurations.CONSUMER_POSTGRES_USER,
        password=configurations.CONSUMER_POSTGRES_PASSWORD,
        host=configurations.CONSUMER_POSTGRES_HOST,
        port=configurations.CONSUMER_POSTGRES_PORT,
    )

def start_producer(configurations):
    return KafkaProducer(
        bootstrap_servers=[configurations.KAFKA_BOOTSTRAP_SERVER],
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )

def main():
    configurations = config.load_config()
    logging.info("Starting the Producer...")
    logging.info(f"KAFKA_BOOTSTRAP_SERVER: {configurations.KAFKA_BOOTSTRAP_SERVER}")

    global db_connection, producer
    db_connection = establish_db_connection(configurations)
    producer = start_producer(configurations)

    kafka_topic = configurations.KAFKA_TOPIC
    wait_between_iterations = configurations.PRODUCER_INTERVAL_SECONDS
    logging.info("Starting the producer loop...")

    signal.signal(signal.SIGINT, stop_producer)

    while True:
        data_for_tables = generate_random_data(cn.table_column_names)
        logging.debug("Data for tables: %s", data_for_tables)
        producer.send(kafka_topic, value=data_for_tables)
        sleep(wait_between_iterations)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
