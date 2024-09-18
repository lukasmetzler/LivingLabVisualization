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

# Konfigurationsdatei laden
c = config.load_config()

# Logging konfigurieren, um Nachrichten zu debuggen und Fehler zu verfolgen
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Sessionmaker für die Datenbank-Sitzung initialisieren
Session = sessionmaker(bind=engine)

# Dictionary, das Tabellennamen mit den entsprechenden Modelklassen verbindet
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


# Funktion zum ordnungsgemäßen Beenden des Consumers bei Signalunterbrechung
def stop_consumer(signum, frame):
    logging.info("Stopping consumer...")
    consumer.close()
    sys.exit(0)


# Hilfsfunktion zum Abrufen der neuesten ID einer Dimensionstabelle
def get_latest_id(session, model_class):
    """
    Diese Funktion ruft den neuesten Datensatz aus einer Dimensionstabelle ab und gibt dessen ID zurück.
    """
    record = session.query(model_class).order_by(model_class.created_at.desc()).first()
    if record:
        # Verwende den primären Schlüssel (ID) der Tabelle direkt, ohne dynamische Namensbildung
        return getattr(record, model_class.__mapper__.primary_key[0].name)
    else:
        logger.warning(f"No records found for {model_class.__tablename__}")
        return None


# Funktion zum Einfügen von Daten in die Faktentabelle für Umweltinformationen
def insert_fact_environmental_data(session, data):
    """
    Diese Funktion fügt Daten in die FactEnvironmentalDataFacts-Tabelle ein.
    Sie ruft die neuesten IDs der zugehörigen Dimensionstabellen ab und verknüpft sie in der Fact-Tabelle.
    """
    try:
        # Abrufen der neuesten IDs aus den Dimensionstabellen
        location_id = get_latest_id(session, DimLocation)
        metrological_data_id = get_latest_id(session, DimMetrologicalData)
        pv_modul_data_id = get_latest_id(session, DimPvModulData1ogR1)
        illumination_datapoints_id = get_latest_id(
            session, DimIlluminationDatapoints1ogR1
        )
        radiation_forecast_id = get_latest_id(session, DimRadiationForecast)
        head_positions_id = get_latest_id(session, DimHeadPositions1ogR1)

        # Einfügen der Daten in die Faktentabelle
        fact_data = FactEnvironmentalDataFacts(
            location_id=location_id,
            metrological_data_id=metrological_data_id,
            pv_modul_data_id=pv_modul_data_id,
            illumination_datapoints_id=illumination_datapoints_id,
            radiation_forecast_id=radiation_forecast_id,
            head_positions_id=head_positions_id,
        )
        session.add(fact_data)
        session.commit()

        logger.info(f"Inserted data into FactEnvironmentalDataFacts: {fact_data}")
    except Exception as e:
        session.rollback()
        logger.error(f"Error inserting data into FactEnvironmentalDataFacts: {e}")


# Funktion zum Verarbeiten von ZED-Kamera-Daten
def process_zed_kamera_data(session, data):
    """
    Diese Funktion verarbeitet spezielle ZED-Kamera-Daten und fügt sie in die entsprechende Dimensionstabelle ein.
    """
    try:
        # Überprüfung, ob body_list existiert und korrekt formatiert ist
        body_list_data = data.get("body_list", "[]")

        if isinstance(body_list_data, str):
            body_list = json.loads(body_list_data)
        elif isinstance(body_list_data, list):
            # Falls das body_list bereits als Liste geliefert wird
            body_list = body_list_data
        else:
            logger.error(
                f"Invalid format for body_list, expected string or list but got {type(body_list_data)}: {body_list_data}"
            )
            return

        # Einfügen der ZED-Daten in die Tabelle DimZedBodyTracking1ogR1
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


# Funktion zum Verarbeiten von allgemeinen Daten und Einfügen in die entsprechenden Tabellen
def process_data(session, table_name, data):
    """
    Verarbeitet eingehende Daten, fügt sie in die Dimensionstabellen ein oder ruft insert_fact_environmental_data auf,
    wenn es sich um eine Faktentabelle handelt.
    """
    try:
        if table_name == "fact_environmental_data_facts":
            # Spezielle Behandlung für Umweltfaktendaten
            insert_fact_environmental_data(session, data)
        else:
            # Allgemeiner Fall für Dimensionstabellen
            model_class = table_to_class[table_name]
            table_data = model_class(**data)
            session.add(table_data)
            session.commit()
            logger.info(f"Data inserted into {table_name}: {data}")
    except Exception as e:
        session.rollback()
        logger.error(f"Error inserting data into {table_name}: {e}")


# Hauptschleife zum Empfangen und Verarbeiten von Nachrichten
def process_messages():
    """
    Diese Funktion liest kontinuierlich Nachrichten von Kafka, verarbeitet sie und fügt die Daten in die PostgreSQL-Datenbank ein.
    """
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
            # Falls es sich um ZED-Kameradaten handelt, eine spezielle Verarbeitungsfunktion aufrufen
            if message.topic == "zed_kamera_topic":
                process_zed_kamera_data(session, data)
            else:
                # Für alle anderen Daten die generische Verarbeitungsfunktion aufrufen
                for table_name, table_data in data.items():
                    process_data(session, table_name, table_data)
        session.commit()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        session.rollback()
    finally:
        consumer.close()
        session.close()


# Hauptfunktion für den Start des Kafka-Consumers
if __name__ == "__main__":
    print(f"Loaded Kafka Topics: {c.KAFKA_TOPICS}")
    print(f"Kafka Bootstrap Server: {c.KAFKA_BOOTSTRAP_SERVER}")
    if not c.KAFKA_TOPICS:
        raise ValueError("No Kafka topics found. Please check your configuration.")
    process_messages()
