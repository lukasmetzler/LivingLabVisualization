import json
import logging
from kafka import KafkaProducer
import config
import column_names as cn
import random
import signal
import sys
from time import sleep
from typing import Dict, List


def stop_producer(signum, frame):
    logging.info("Stopping producer...")
    producer.close()
    sys.exit(0)


def generate_boolean() -> bool:
    return random.choice([True, False])


def generate_random_data(
    table_column_names: Dict[str, List[str]]
) -> Dict[str, Dict[str, float]]:
    data = {}

    for table, columns in table_column_names.items():
        # Filtere nur die Spalten, die keine IDs sind
        filtered_columns = [column for column in columns if not column.endswith("_id")]

        # Generiere die Daten für jede Tabelle
        table_data = {}
        for column in filtered_columns:
            if column in ["is_new", "is_tracked"]:
                # Erzeuge Boolean-Werte für bestimmte Spalten
                table_data[column] = generate_boolean()
            elif column == "body_list":
                # Füge ein korrektes JSON-Format für body_list hinzu
                table_data[column] = json.dumps(
                    [{"id": random.randint(1, 100), "name": "Body"}]
                )
            else:
                # Erzeuge numerische Zufallswerte für andere Spalten
                table_data[column] = random.uniform(0, 100)

        data[table] = table_data

    logging.debug("Generated data: %s", data)
    return data


def start_producer(configurations):
    return KafkaProducer(
        bootstrap_servers=[configurations.KAFKA_BOOTSTRAP_SERVER],
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )


def main():
    configurations = config.load_config()
    logging.info("Starting the Producer...")
    logging.info(f"KAFKA_BOOTSTRAP_SERVER: {configurations.KAFKA_BOOTSTRAP_SERVER}")

    global producer
    producer = start_producer(configurations)

    kafka_topics = configurations.KAFKA_TOPICS  # Verwenden Sie KAFKA_TOPICS
    wait_between_iterations = configurations.PRODUCER_INTERVAL_SECONDS
    logging.info("Starting the producer loop...")

    signal.signal(signal.SIGINT, stop_producer)

    while True:
        data_for_tables = generate_random_data(cn.table_column_names)
        logging.debug("Data for tables: %s", data_for_tables)

        # Beispielhafte Zuweisung von Daten zu Topics
        hella_data = {
            key: value
            for key, value in data_for_tables.items()
            if key != "dim_zed_body_tracking_1og_r1"
        }
        zed_data = data_for_tables.get("dim_zed_body_tracking_1og_r1", {})

        if "hella_data_topic" in kafka_topics:
            producer.send("hella_data_topic", value=hella_data)
            logging.info(f"Sent data to topic hella_data_topic: {hella_data}")

        if "zed_kamera_topic" in kafka_topics:
            producer.send("zed_kamera_topic", value=zed_data)
            logging.info(f"Sent data to topic zed_kamera_topic: {zed_data}")

        sleep(wait_between_iterations)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
