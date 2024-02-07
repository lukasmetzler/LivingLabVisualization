from time import sleep
import json
from kafka import KafkaProducer
import config
import logging
import random
from typing import Dict, List
import signal
import sys
import psycopg2
import column_names as cn


def stop_producer(signum, frame):
    logging.info("Stopping producer...")
    producer.close()
    db_connection.close()
    sys.exit(0)


def generate_random_data(table_column_names: Dict[str, List[str]]) -> Dict[str, float]:
    data = {}

    for table, columns in table_column_names.items():
        # Exclude columns ending with '_id' (assuming these are the ID columns)
        filtered_columns = [column for column in columns if not column.endswith('_id')]
        
        # Generate random data for each non-ID column
        data[table] = {column: random.uniform(0, 100) for column in filtered_columns}

    logging.debug("Generated data: %s", data)
    return data


c = config.load_config()
print("Configuration loaded.")
logging.info("Starting the Producer...")
print(f"KAFKA_BOOTSTRAP_SERVER: {c.KAFKA_BOOTSTRAP_SERVER}")

# Establish PostgreSQL connection
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
print("Starting the producer loop...")

signal.signal(signal.SIGINT, stop_producer)

while True:
    data_for_tables = generate_random_data(cn.table_column_names)
    logging.debug("Data for tables: %s", data_for_tables)
    producer.send(kafka_topic, value=data_for_tables)
    sleep(wait_between_iterations)
