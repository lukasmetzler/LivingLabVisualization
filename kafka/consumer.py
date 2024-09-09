from datetime import datetime
import json
import logging
from kafka import KafkaConsumer
import config
from models import (
    Base,
    engine,
    DimZedBodyTracking1ogR1,
    DimMetrologicalData,
    DimPvModulData1ogR1,
    DimIlluminationDatapoints1ogR1,
    DimRaffstoreLightData,
    DimUserInput,
    DimLocation,
    DimRadiationForecast,
    DimHeadPositions1ogR1,
    FactUserInputFacts,
    FactSensory,
    FactRaffstoreLightFacts,
    FactEnvironmentalDataFacts,
)
from sqlalchemy.orm import sessionmaker
import signal
import sys

c = config.load_config()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
Session = sessionmaker(bind=engine)

table_to_class = {
    "dim_zed_body_tracking_1og_r1": DimZedBodyTracking1ogR1,
    "dim_metrological_data": DimMetrologicalData,
    "dim_pv_modul_data_1og_r1": DimPvModulData1ogR1,
    "dim_illumination_datapoints_1og_r1": DimIlluminationDatapoints1ogR1,
    "dim_raffstore_light_data": DimRaffstoreLightData,
    "dim_user_input": DimUserInput,
    "dim_location": DimLocation,
    "dim_radiation_forecast": DimRadiationForecast,
    "dim_head_positions_1og_r1": DimHeadPositions1ogR1,
    "fact_user_input_facts": FactUserInputFacts,
    "fact_sensory": FactSensory,
    "fact_raffstore_light_facts": FactRaffstoreLightFacts,
    "fact_environmental_data_facts": FactEnvironmentalDataFacts,
}


def process_zed_kamera_data(session, data):
    try:
        body_list_data = data.get("body_list", "[]")

        if isinstance(body_list_data, str):
            body_list = json.loads(body_list_data)
        else:
            logger.error(
                f"Invalid format for body_list, expected a string but got {type(body_list_data)}: {body_list_data}"
            )
            return

        zed_data = DimZedBodyTracking1ogR1(
            is_new=data.get("is_new", False),
            is_tracked=data.get("is_tracked", False),
            camera_pitch=data.get("camera_pitch"),
            camera_roll=data.get("camera_roll"),
            camera_yaw=data.get("camera_yaw"),
            body_list=body_list,
        )
        session.add(zed_data)
        session.commit()
        logger.info(f"Data inserted into dim_zed_body_tracking_1og_r1: {data}")
    except json.JSONDecodeError as je:
        logger.error(f"JSON decoding error while parsing body_list: {je}")
        session.rollback()
    except Exception as e:
        logger.error(f"An error occurred while inserting zed kamera data: {e}")
        session.rollback()


def process_data(session, table_name, data):
    try:
        model_class = table_to_class[table_name]
        table_data = model_class(**data)
        session.add(table_data)
        session.commit()
        logger.info(f"Data inserted into {table_name}: {data}")
    except Exception as e:
        logger.error(f"An error occurred while inserting data into {table_name}: {e}")
        session.rollback()


def process_messages():
    session = Session()
    consumer = KafkaConsumer(
        *c.KAFKA_TOPICS,
        bootstrap_servers=c.KAFKA_BOOTSTRAP_SERVER,
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="consumer",
        value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    )
    signal.signal(signal.SIGINT, stop_consumer)

    try:
        for message in consumer:
            logger.debug(f"Received message: {message.value}")
            data = message.value
            if message.topic == "zed_kamera_topic":
                process_zed_kamera_data(session, data)
            else:
                for table_name, table_data in data.items():
                    process_data(session, table_name, table_data)
        session.commit()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        session.rollback()
    finally:
        consumer.close()
        session.close()


if __name__ == "__main__":
    print(f"Loaded Kafka Topics: {c.KAFKA_TOPICS}")
    print(f"Kafka Bootstrap Server: {c.KAFKA_BOOTSTRAP_SERVER}")
    if not c.KAFKA_TOPICS:
        raise ValueError("No Kafka topics found. Please check your configuration.")
    process_messages()
