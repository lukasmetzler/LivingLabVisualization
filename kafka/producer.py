from time import sleep
import json
from kafka import KafkaProducer

topic = "dim_metrological_data_topic"
kafka_server = ["192.168.1.22"]
sleep(10)
producer = KafkaProducer(
    bootstrap_servers=kafka_server,
    api_version=(2, 6, 0),
    request_timeout_ms=1000000,
    api_version_auto_timeout_ms=1000000,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)


while True:
    sleep(60)
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
    producer.send(topic, value=metrological_data)
    producer.flush()
    sleep(3)
