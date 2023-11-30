from time import sleep
import json
from kafka import KafkaProducer
import config
import logging

logging.basicConfig(level=logging.DEBUG)

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
    metrological_data = {
        "globirrveract": 121,
        "globalirrhoract": 121,
        "difflrrhoract": 121,
        "windspeedact_ms": 121,
        "sunelevationact": 121,
        "sunazimuthact": 121,
        "longitude": 121,
        "latitude": 121,
        "windspeedact_kmh": 121,
        "winddirectionact": 121,
        "brightnessnorthact": 121,
        "brightnesssouthact": 121,
        "brightnesswestact": 121,
        "twilightact": 121,
        "globalirrhoract_2": 121,
        "precipitationact": 121,
        "absolutairpressureact": 121,
        "relativeairpressureact": 121,
        "absolutehumidityact": 121,
        "relativehumidityact": 121,
        "dewpointtempact": 121,
        "housingtemact": 121,
        "roomtempact": 121,
    }
    producer.send(kafka_topic, value=metrological_data)
    sleep(wait_between_iterations)
