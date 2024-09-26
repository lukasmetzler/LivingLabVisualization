import json
import logging
import sys
import traceback
import signal
from datetime import datetime

print("Starting consumer.py")  # Debugging output

# Import configuration
try:
    import config

    print("Imported config")  # Debugging output
except Exception as e:
    print(f"Error importing config: {e}")
    traceback.print_exc()
    sys.exit(1)

# Load configuration
c = config.load_config()
print("Loaded config")  # Debugging output

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create the database engine and import models
try:
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    # Create the database engine
    engine = create_engine(
        f"postgresql+psycopg2://{c.CONSUMER_POSTGRES_USER}:{c.CONSUMER_POSTGRES_PASSWORD}"
        f"@{c.CONSUMER_POSTGRES_HOST}:{c.CONSUMER_POSTGRES_PORT}/{c.CONSUMER_POSTGRES_DB}"
    )
    print("Database engine created")  # Debugging output

    # Import models after engine creation
    from models import (
        Base,
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

    print("Imported models")  # Debugging output

    # Create database tables
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    print("Database tables initialized")
except Exception as e:
    logger.error(f"Error creating database engine or importing models: {e}")
    traceback.print_exc()
    sys.exit(1)

# Map table names to model classes
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


# Function to handle graceful shutdown on SIGINT
def stop_consumer(signum, frame):
    logger.info("Stopping consumer...")
    sys.exit(0)


# Helper function to get the latest ID from a dimension table
def get_latest_id(session, model_class):
    record = session.query(model_class).order_by(model_class.created_at.desc()).first()
    if record:
        primary_key_column = model_class.__mapper__.primary_key[0].name
        logger.debug(f"Latest record for {model_class.__tablename__}: {record}")
        return getattr(record, primary_key_column)
    else:
        logger.warning(f"No records found for {model_class.__tablename__}")
        return None


# Function to insert data into fact tables
def insert_fact_table(session, fact_model_class, dimension_model_classes):
    try:
        dimension_ids = {}
        for dimension_name, fk_field in dimension_model_classes.items():
            model_class = table_to_class[dimension_name]
            latest_id = get_latest_id(session, model_class)
            dimension_ids[fk_field] = latest_id

            if latest_id is None:
                logger.error(f"Missing required ID for {dimension_name}")
                return

        fact_data = fact_model_class(**dimension_ids)
        session.add(fact_data)
        session.commit()
        logger.info(f"Inserted data into {fact_model_class.__tablename__}: {fact_data}")
    except Exception as e:
        session.rollback()
        logger.error(f"Error inserting data into {fact_model_class.__tablename__}: {e}")
        traceback.print_exc()


# Function to process ZED camera data
def process_zed_kamera_data(session, data):
    try:
        body_list_data = data.get("body_list", "[]")

        if isinstance(body_list_data, str):
            body_list = json.loads(body_list_data)
        elif isinstance(body_list_data, list):
            body_list = body_list_data
        else:
            logger.error(
                f"Invalid format for body_list, expected string or list but got {type(body_list_data)}: {body_list_data}"
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
        logger.error(f"An error occurred while inserting ZED camera data: {e}")
        traceback.print_exc()
        session.rollback()


# Function to process incoming data and insert into appropriate tables
def process_data(session, table_name, data):
    try:
        if table_name.startswith("fact_"):
            # Handling fact tables
            if table_name == "fact_environmental_data_facts":
                insert_fact_table(
                    session,
                    FactEnvironmentalDataFacts,
                    {
                        "dim_location": "location_id",
                        "dim_metrological_data": "metrological_data_id",
                        "dim_pv_modul_data_1og_r1": "pv_modul_data_id",
                        "dim_illumination_datapoints_1og_r1": "illumination_datapoints_id",
                        "dim_radiation_forecast": "radiation_forecast_id",
                        "dim_head_positions_1og_r1": "head_positions_id",
                    },
                )
            elif table_name == "fact_user_input_facts":
                insert_fact_table(
                    session,
                    FactUserInputFacts,
                    {
                        "dim_location": "location_id",
                        "dim_user_input": "user_input_id",
                    },
                )
            elif table_name == "fact_sensory":
                insert_fact_table(
                    session,
                    FactSensory,
                    {
                        "dim_location": "location_id",
                        "dim_zed_body_tracking_1og_r1": "zed_body_tracking_id",
                    },
                )
            elif table_name == "fact_raffstore_light_facts":
                insert_fact_table(
                    session,
                    FactRaffstoreLightFacts,
                    {
                        "dim_location": "location_id",
                        "dim_raffstore_light_data": "raffstore_light_data_id",
                    },
                )
        else:
            # Handling dimension tables
            model_class = table_to_class.get(table_name)
            if model_class:
                table_data = model_class(**data)
                session.add(table_data)
                session.commit()
                logger.info(f"Data inserted into {table_name}: {data}")
            else:
                logger.error(f"Unknown table name: {table_name}")
    except Exception as e:
        session.rollback()
        logger.error(f"Error inserting data into {table_name}: {e}")
        traceback.print_exc()


# Function to deserialize messages from Kafka
def deserialize_message(message):
    try:
        message_str = message.decode("utf-8")
        logger.debug(f"Raw message before deserialization: {message_str}")
        return json.loads(message_str)
    except json.JSONDecodeError as e:
        logger.error(f"JSON deserialization error: {e}")
        logger.error(f"Raw message: {message_str}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error during deserialization: {e}")
        traceback.print_exc()
        return None


# Main function to process messages from Kafka
def process_messages():
    session = Session()

    # Ensure KAFKA_TOPICS is a list
    if isinstance(c.KAFKA_TOPICS, str):
        c.KAFKA_TOPICS = [topic.strip() for topic in c.KAFKA_TOPICS.split(",")]

    logger.debug(f"Subscribing to topics: {c.KAFKA_TOPICS}")

    from kafka import KafkaConsumer

    consumer = KafkaConsumer(
        *c.KAFKA_TOPICS,
        bootstrap_servers=c.KAFKA_BOOTSTRAP_SERVER,
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="consumer_group",
        value_deserializer=deserialize_message,
    )
    signal.signal(signal.SIGINT, stop_consumer)

    try:
        for message in consumer:
            try:
                if message.value is None:
                    logger.warning("Received a message that could not be deserialized.")
                    continue
                logger.debug(f"Received message: {message.value}")
                data = message.value
                # Process the message based on the topic
                if message.topic == "zed_kamera_topic":
                    process_zed_kamera_data(session, data)
                else:
                    for table_name, table_data in data.items():
                        process_data(session, table_name, table_data)
                session.commit()
            except Exception as e:
                logger.error(f"Error processing message: {e}")
                traceback.print_exc()
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
