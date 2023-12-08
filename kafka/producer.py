from time import sleep
import json
from kafka import KafkaProducer
import config
import logging
import random

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
        "globirrveract": random.uniform(100, 200),
        "globalirrhoract": random.uniform(100, 200),
        "difflrrhoract": random.uniform(100, 200),
        "windspeedact_ms": random.uniform(0, 10),
        "sunelevationact": random.uniform(0, 90),
        "sunazimuthact": random.uniform(0, 360),
        "longitude": random.uniform(-180, 180),
        "latitude": random.uniform(-90, 90),
        "windspeedact_kmh": random.uniform(0, 36),
        "winddirectionact": random.uniform(0, 360),
        "brightnessnorthact": random.uniform(0, 100),
        "brightnesssouthact": random.uniform(0, 100),
        "brightnesswestact": random.uniform(0, 100),
        "twilightact": random.uniform(0, 1),
        "globalirrhoract_2": random.uniform(100, 200),
        "precipitationact": random.uniform(0, 10),
        "absolutairpressureact": random.uniform(900, 1100),
        "relativeairpressureact": random.uniform(0, 100),
        "absolutehumidityact": random.uniform(0, 100),
        "relativehumidityact": random.uniform(0, 100),
        "dewpointtempact": random.uniform(-20, 40),
        "housingtemact": random.uniform(-20, 40),
        "roomtempact": random.uniform(-20, 40),
    }
    dim_pv_modul_data_1og_r1_data = {
        "volt_meas_act_module1": random.uniform(100, 200),
        "curr_meas_act_module1": random.uniform(100, 200),
        "volt_meas_act_module2": random.uniform(100, 200),
        "curr_meas_act_module2": random.uniform(100, 200),
    }
    producer.send(kafka_topic, value=metrological_data)
    sleep(wait_between_iterations)
