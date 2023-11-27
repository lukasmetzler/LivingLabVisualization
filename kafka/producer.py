from time import sleep
import typing as t
import json
from kafka import KafkaProducer
import config
import logging

logging.basicConfig(level=logging.DEBUG)


def main():
    c = config.load_config()
    logging.info("Starte den Producer...")
    producer = KafkaProducer(
        bootstrap_servers=[c.KAFKA_BOOTSTRAP_SERVER],
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )

    kafka_topic = c.KAFKA_TOPIC
    wait_between_iterations = c.PRODUCER_INTERVAL_SECONDS
    run_producer(producer, kafka_topic, wait_between_iterations)


def run_producer(
    kafka_producer: KafkaProducer, kafka_topic: str, wait_between_iterations: int
):
    while True:
        metrological_data = {
            "GlobalIrrVerAct": 121,
            "GlobIrrVerAct": 121,
            "GlobalIrrHorAct": 121,
            "DifflrrHorAct": 121,
            "WindSpeedAct_ms": 121,
            "SunElevationAct": 121,
            "SunAzimuthAct": 121,
            "Longitude": 121,
            "Latitude": 121,
            "WindSpeedAct_kmh": 121,
            "WindDirectionAct": 121,
            "BrightnessNorthAct": 121,
            "BrightnessSouthAct": 121,
            "BrightnessWestAct": 121,
            "TwilightAct": 121,
            "GlobalIrrHorAct_2": 121,
            "PrecipitationAct": 121,
            "AbsolutAirPressureAct": 121,
            "RelativeAirPressureAct": 121,
            "AbsoluteHumidityAct": 121,
            "RelativeHumidityAct": 121,
            "DewPointTempAct": 121,
            "HousingTemAct": 121,
            "RoomTempAct": 121,
        }
        kafka_producer.send(kafka_topic, value=metrological_data)
        sleep(wait_between_iterations)
