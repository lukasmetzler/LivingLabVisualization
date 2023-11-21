import json
from kafka import KafkaConsumer
import logging
from . import config
from . import postgres as pg


def main():
    c = config.load_config();
    consumer = KafkaConsumer(
        c.KAFKA_TOPIC,
        bootstrap_servers=[c.KAFKA_BOOTSTRAP_SERVER],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='consumer',
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    )
    handler(consumer)

def handler(consumer):
    metrological_column_names = [
        "GlobalIrrVerAct",
        "GlobIrrVerAct",
        "GlobalIrrHorAct",
        "DifflrrHorAct",
        "WindSpeedAct_ms",
        "SunElevationAct",
        "SunAzimuthAct",
        "Longitude",
        "Latitude",
        "WindSpeedAct_kmh",
        "WindDirectionAct",
        "BrightnessNorthAct",
        "BrightnessSouthAct",
        "BrightnessWestAct",
        "TwilightAct",
        "GlobalIrrHorAct_2",
        "PrecipitationAct",
        "AbsolutAirPressureAct",
        "RelativeAirPressureAct",
        "AbsoluteHumidityAct",
        "RelativeHumidityAct",
        "DewPointTempAct",
        "HousingTemAct",
        "RoomTempAct",
    ]

    with pg.postgres_cursor_context() as cursor:
        try:
            for message in consumer:
                metrological_data = message.value

                columns_placeholder = ", ".join(metrological_column_names)
                values_placeholder = ", ".join(["%s"] * len(metrological_column_names))

                query = f"INSERT INTO dim_metrological_data ({columns_placeholder}) VALUES ({values_placeholder})"
                values = [metrological_data[column] for column in metrological_column_names]

                cursor.execute(query, values)
                logging.info(f"Data inserted into database: {metrological_data}")

        except Exception as e:
            logging.error(f"An error occured: {e}")
