from json import loads
from kafka import KafkaConsumer
import psycopg2
import logging
from time import sleep

logging.basicConfig(
    filename="consumer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

db_params = {
    "dbname": "evi",
    "user": "lukasmetzler",
    "password": "lukasmetzler",
    "host": "postgres",
    "port": "5432",
}

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


consumer = KafkaConsumer(
    "dim_metrological_data_topic",
    bootstrap_servers=["kafka:9092"],
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="my-group",
    value_deserializer=lambda x: loads(x.decode("utf-8")),
    api_version=(2,6,0),
)

sleep(10)

conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

try:
    for message in consumer:
        metrological_data = message.value

        columns_placeholder = ", ".join(metrological_column_names)
        values_placeholder = ", ".join(["%s"] * len(metrological_column_names))

        query = f"INSERT INTO dim_metrological_data ({columns_placeholder}) VALUES ({values_placeholder})"
        values = [metrological_data[column] for column in metrological_column_names]

        cursor.execute(query, values)
        conn.commit()

        logging.info(f"Data inserted into database: {metrological_data}")

except Exception as e:
    logging.error(f"An error occurred: {e}")

finally:
    cursor.close()
    conn.close()
    logging.info("Database connection closed.")
