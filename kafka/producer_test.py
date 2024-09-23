import json
import logging
import random
from kafka import KafkaProducer
import signal
import sys
from time import sleep


# Funktion zum ordnungsgemäßen Beenden des Producers bei Signalunterbrechung
def stop_producer(signum, frame):
    logging.info("Stopping producer...")
    producer.close()
    sys.exit(0)


# Funktion zur Generierung von zufälligen Daten für die Tabelle dim_zed_body_tracking
def generate_zed_body_tracking_data():
    """
    Generiert zufällige Testdaten für die ZED-Kameradaten.
    """
    data = {
        "is_new": random.choice([True, False]),
        "is_tracked": random.choice([True, False]),
        "camera_pitch": random.uniform(-180, 180),
        "camera_roll": random.uniform(-180, 180),
        "camera_yaw": random.uniform(-180, 180),
        "body_list": [
            {
                "id": random.randint(1, 100),
                "position": [random.uniform(0, 10) for _ in range(3)],
            }
        ],
    }
    return data


# Funktion zum Starten des Kafka-Producers
def start_producer(kafka_server):
    """
    Initialisiert und gibt einen KafkaProducer zurück, der mit dem externen Kafka-Server kommunizieren kann.
    """
    return KafkaProducer(
        bootstrap_servers=[kafka_server],
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        api_version=(2, 8, 0),
    )


# Hauptfunktion des Producers
def main():
    kafka_server = "livinglab-prod.hella.info:9092"  # Externer Kafka-Server
    topic = "zed_kamera_topic"  # Thema, auf das die Daten gesendet werden
    interval_seconds = 5  # Wartezeit zwischen den Nachrichten

    logging.info(f"Connecting to Kafka at {kafka_server}...")
    global producer
    producer = start_producer(kafka_server)

    logging.info("Starting the producer loop...")

    signal.signal(signal.SIGINT, stop_producer)

    while True:
        # Generiere ZED-Kameradaten
        zed_data = generate_zed_body_tracking_data()

        # Sende die Daten an das Kafka-Thema zed_kamera_topic
        producer.send(topic, value=zed_data)
        logging.info(f"Sent data to topic {topic}: {zed_data}")

        # Warte, bevor die nächste Nachricht gesendet wird
        sleep(interval_seconds)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
