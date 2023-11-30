import json
from time import sleep
from kafka import KafkaConsumer
import logging
import config
import postgres as pg

# logging.basicConfig(level=logging.DEBUG)

c = config.load_config()
logging.info("Creating KafkaConsumer...")
consumer = KafkaConsumer(
    c.KAFKA_TOPIC,
    bootstrap_servers=[c.KAFKA_BOOTSTRAP_SERVER],
    auto_offset_reset="earliest",
    enable_auto_commit=False,
    group_id="consumer",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)
logging.info("KafkaConsumer created successfully.")

metrological_column_names = [
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

with pg.postgres_connection() as connection:
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS dim_metrological_data (
                    metrological_data_id SERIAL PRIMARY KEY,
                    globirrveract Numeric,
                    globalirrhoract Numeric,
                    difflrrhoract Numeric,
                    windspeedact_ms Numeric,
                    sunelevationact Numeric,
                    sunazimuthact Numeric,
                    longitude Numeric,
                    latitude Numeric,
                    windspeedact_kmh Numeric,
                    winddirectionact Numeric,
                    brightnessnorthact Numeric,
                    brightnesssouthact Numeric,
                    brightnesswestact Numeric,
                    twilightact Numeric,
                    globalirrhoract_2 Numeric,
                    precipitationact Numeric,
                    absolutairpressureact Numeric,
                    relativeairpressureact Numeric,
                    absolutehumidityact Numeric,
                    relativehumidityact Numeric,
                    dewpointtempact Numeric,
                    housingtemact Numeric,
                    roomtempact Numeric
                );
            """
            )

            for message in consumer:
                print("Received message:", message.value)
                metrological_data = message.value

                if all(key in metrological_data for key in metrological_column_names):
                    values = [
                        metrological_data[column]
                        for column in metrological_column_names
                    ]

                    columns_placeholder = ", ".join(metrological_column_names)
                    values_placeholder = ", ".join(
                        ["%s"] * len(metrological_column_names)
                    )

                    query = f"INSERT INTO dim_metrological_data ({columns_placeholder}) VALUES ({values_placeholder})"
                    print("QUERY: " + query)
                    print("VALUES TEST: ", values)

                    try:
                        cursor.execute(query, values)
                        connection.commit()
                        logging.info(
                            f"Data inserted into database: {metrological_data}"
                        )
                        print("Data inserted into database:", metrological_data)
                    except Exception as e:
                        logging.error(f"An error occurred: {e}")
                        print("Error inserting data into database:", e)
                else:
                    logging.error(
                        "Not all required keys present in metrological_data. Skipping message."
                    )

    except Exception as e:
        logging.error(f"An error occurred: {e}")
