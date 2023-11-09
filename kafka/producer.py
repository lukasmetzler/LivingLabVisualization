from kafka import KafkaProducer
import json

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

topic = "metrological-topic"

try:
    while True:
        data = {
            "GlobIrrVerAct": 42, 
            "GlobalIrrHorAct": 56,
            "DifflrrHorAct": 12,
            "WindSpeedAct_ms": 23,
            "SunElevationAct": 45,
            "SunAzimuthAct": 90,
            "Longitude": 10.123456,
            "Latitude": 45.678901,
            "WindSpeedAct_kmh": 83,
            "WindDirectionAct": 180,
            "BrightnessNorthAct": 75,
            "BrightnessSouthAct": 80,
            "BrightnessWestAct": 70,
            "TwilightAct": 6,
            "GlobalIrrHorAct_2": 55,
            "PrecipitationAct": 2,
            "AbsolutAirPressureAct": 1013,
            "RelativeAirPressureAct": 50,
            "AbsoluteHumidityAct": 10,
            "RelativeHumidityAct": 65,
            "DewPointTempAct": 8,
            "HousingTemAct": 22,
            "RoomTempAct": 20
        }

        # Senden an Kafka
        producer.send(topic, value=data)
        print("Data sent to Kafka")

except KeyboardInterrupt:
    producer.close()
