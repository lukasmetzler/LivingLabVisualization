import json
import logging
from kafka import KafkaProducer
import random
import signal
import sys
from time import sleep


def stop_producer(signum, frame):
    logging.info("Stopping producer...")
    producer.close()
    sys.exit(0)


def generate_boolean() -> bool:
    return random.choice([True, False])


def generate_random_data() -> dict:
    """Generiere Zufallsdaten für die Zed-Kamera."""
    zed_data = {
        "is_new": generate_boolean(),
        "is_tracked": generate_boolean(),
        "tracking_confidence": random.uniform(0, 100),
        "object_count": random.randint(0, 10)
    }
    logging.debug("Generated Zed data: %s", zed_data)
    return zed_data


def start_producer(broker_server):
    return KafkaProducer(
        bootstrap_servers=[broker_server],
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )


def main():
    broker_server = "83.175.123.10:9092"
    logging.info(f"Starting the Producer with broker {broker_server}...")

    global producer
    producer = start_producer(broker_server)

    wait_between_iterations = 5  # Sekunden zwischen jeder Nachricht
    logging.info("Starting the producer loop...")

    signal.signal(signal.SIGINT, stop_producer)

    while True:
        logging.basicConfig(level=logging.DEBUG)
        # Generiere zufällige Daten für den Zed-Kamera-Topic
        zed_data = generate_random_data()

        # Sende die Daten an den zed_kamera_topic
        producer.send("zed_kamera_topic", value=zed_data)
        logging.info(f"Sent data to topic zed_kamera_topic: {zed_data}")

        sleep(wait_between_iterations)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
