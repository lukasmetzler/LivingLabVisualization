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
    DimTime,
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
import datetime

c = config.load_config()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
Session = sessionmaker(bind=engine)

# Table class mapping
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


def stop_consumer(signum, frame):
    logging.info("Stopping consumer...")
    consumer.close()
    sys.exit(0)


def process_zed_kamera_data(session, data):
    try:
        zed_data = DimZedBodyTracking1ogR1(
            is_new=data.get("is_new", False),
            is_tracked=data.get("is_tracked", False),
            camera_pitch=data.get("camera_pitch"),
            camera_roll=data.get("camera_roll"),
            camera_yaw=data.get("camera_yaw"),
            body_list=data.get("body_list", []),
        )
        session.add(zed_data)
        session.commit()
        logger.info(f"Data inserted into dim_zed_body_tracking_1og_r1: {data}")
    except Exception as e:
        logger.error(f"An error occurred while inserting zed kamera data: {e}")
        session.rollback()


def process_data(session, table_name, data):
    try:
        model_class = globals()[table_name]
        if table_name == "dim_metrological_data":
            timestamp = data.get("created_at")
            if timestamp:
                timestamp = datetime.datetime.fromisoformat(timestamp)
                time_record = DimTime.get_or_create(session, timestamp)
                data["time_id"] = time_record.time_id
        table_data = model_class(**data)
        session.add(table_data)
        session.commit()
        logger.info(f"Data inserted into {table_name}: {data}")
    except Exception as e:
        logger.error(f"An error occurred while inserting data into {table_name}: {e}")
        session.rollback()


def process_messages():
    session = Session()
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

    try:
        consumer = KafkaConsumer(
            *c.KAFKA_TOPICS,
            bootstrap_servers=c.KAFKA_BOOTSTRAP_SERVER,
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            group_id="consumer",
            value_deserializer=lambda x: json.loads(x.decode("utf-8")),
        )
        signal.signal(signal.SIGINT, stop_consumer)
        process_messages()
    except Exception as e:
        logger.error(f"An error occurred while creating KafkaConsumer: {e}")
        sys.exit(1)
