import json
from time import sleep
from kafka import KafkaConsumer
import logging
import config
import postgres as pg

logging.basicConfig(level=logging.INFO)

c = config.load_config()
logging.info("Creating KafkaConsumer...")
consumer = KafkaConsumer(
    c.KAFKA_TOPIC,
    bootstrap_servers=[c.KAFKA_BOOTSTRAP_SERVER],
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="consumer",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)
logging.info("KafkaConsumer created successfully.")

metrological_column_names = [
    "globalirrveract",
    "globirrveract",
    "globalirrhoract",
    "difflrrhoract",
    "windspeedact_ms",
    "sunelevationact",
    "sunazimuthact",
    "longitude",
    "latitude",
    "windspeedact_kmh",
    "winddirectionact",
    "brightnessnorthact",
    "brightnesssouthact",
    "brightnesswestact",
    "twilightact",
    "globalirrhoract_2",
    "precipitationact",
    "absolutairpressureact",
    "relativeairpressureact",
    "absolutehumidityact",
    "relativehumidityact",
    "dewpointtempact",
    "housingtemact",
    "roomtempact",
]


with pg.postgres_cursor_context() as cursor:
    try:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS dim_metrological_data (
                metrological_data_id SERIAL PRIMARY KEY,
                GlobIrrVerAct Numeric,
                GlobalIrrHorAct Numeric,
                DifflrrHorAct Numeric,
                WindSpeedAct_ms Numeric,
                SunElevationAct Numeric,
                SunAzimuthAct Numeric,
                Longitude Numeric,
                Latitude Numeric,
                WindSpeedAct_kmh Numeric,
                WindDirectionAct Numeric,
                BrightnessNorthAct Numeric,
                BrightnessSouthAct Numeric,
                BrightnessWestAct Numeric,
                TwilightAct Numeric,
                GlobalIrrHorAct_2 Numeric,
                PrecipitationAct Numeric,
                AbsolutAirPressureAct Numeric,
                RelativeAirPressureAct Numeric,
                AbsoluteHumidityAct Numeric,
                RelativeHumidityAct Numeric,
                DewPointTempAct Numeric,
                HousingTemAct Numeric,
                RoomTempAct Numeric
            );
        """
        )
        for message in consumer:
            metrological_data = message.value

            columns_placeholder = ", ".join(metrological_column_names)
            values_placeholder = ", ".join(["%s"] * len(metrological_column_names))

            query = f"INSERT INTO dim_metrological_data ({columns_placeholder}) VALUES ({values_placeholder})"
            values = [metrological_data[column] for column in metrological_column_names]

            cursor.execute(query, values)
            logging.info(f"Data inserted into database: {metrological_data}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
