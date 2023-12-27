from time import sleep
import json
from kafka import KafkaProducer
import config
import logging
import random
from typing import Dict, List
import column_names as cn


def generate_random_data(column_names: List[str]) -> Dict[str, float]:
    data = {column: random.uniform(0, 100) for column in column_names}
    logging.debug("Generated data: %s", data)
    return data


c = config.load_config()
print("Configuration loaded.")
logging.info("Starte den Producer...")
print(f"KAFKA_BOOTSTRAP_SERVER: {c.KAFKA_BOOTSTRAP_SERVER}")
producer = KafkaProducer(
    bootstrap_servers=[c.KAFKA_BOOTSTRAP_SERVER],
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

kafka_topic = c.KAFKA_TOPIC
wait_between_iterations = c.PRODUCER_INTERVAL_SECONDS
print("Starting producer loop...")

while True:
    data_for_tables = {
        table: generate_random_data(columns)
        for table, columns in cn.table_column_names.items()
    }
    logging.debug("Data for tables: %s", data_for_tables)
    producer.send(kafka_topic, value=data_for_tables)
    sleep(wait_between_iterations)
