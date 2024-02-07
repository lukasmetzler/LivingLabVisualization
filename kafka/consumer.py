import json
import logging
from kafka import KafkaConsumer
import config
import postgres as pg
from column_names import table_column_names
from fact_column_names import fact_table_column_names

# Konfiguration laden
c = config.load_config()

# Protokollierung konfigurieren
# logging.basicConfig(level=logging.INFO)

# KafkaConsumer erstellen
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


def get_last_inserted_ids(connection, cursor):
    last_inserted_ids = {}
    try:
        for table_name, column_names in table_column_names.items():
            if table_name.startswith("dim_"):
                # Get the name of the ID column
                id_column_name = None
                for column_name in column_names:
                    if column_name.endswith("_id"):
                        id_column_name = column_name
                        break

                if id_column_name is None:
                    logging.error(f"No ID column found for table {table_name}")
                    continue

                # Query to get the max value of the ID column
                query = f"SELECT max({id_column_name}) FROM {table_name}"
                cursor.execute(query)
                result = cursor.fetchone()[0]
                last_inserted_ids[id_column_name] = result
        return last_inserted_ids
    except Exception as e:
        logging.error(f"An error occurred while retrieving last inserted IDs: {e}")
        return None


def insert_data_into_table(connection, cursor, table_name, column_names, data):
    try:
        if table_name.startswith("dim_") and isinstance(data, dict):
            table_data = data.get(table_name, None)

            if table_data is None:
                logging.error(
                    f"Table data for '{table_name}' not found in the message. Skipping message."
                )
                return None

            # Filter out ID columns from the data
            filtered_values = [
                table_data.get(column, None)
                for column in column_names
                if not column.endswith("_id")
            ]

            # Filter out ID columns from the column names
            filtered_columns = [
                column for column in column_names if not column.endswith("_id")
            ]

            columns_placeholder = (", ").join(column for column in filtered_columns)
            values_placeholder = (", ").join(["%s" for _ in filtered_columns])

            query = f"INSERT INTO {table_name} ({columns_placeholder}) VALUES ({values_placeholder})"
            cursor.execute(query, filtered_values)
            logging.info(f"Data inserted into database: {data}")
            return None
    except Exception as e:
        logging.error(f"An error occurred while inserting data into {table_name}: {e}")
        connection.rollback()
        return None


def process_messages():
    try:
        with pg.postgres_connection() as connection:
            logging.debug("Verbindung erfolgreich hergestellt")

            for message in consumer:
                with connection.cursor() as cursor:
                    # Insert into dimension tables
                    dimension_ids = {}
                    for table_name, column_names in table_column_names.items():
                        inserted_id = insert_data_into_table(
                            connection,
                            cursor,
                            table_name,
                            column_names,
                            message.value,
                        )
                        dimension_ids[table_name] = inserted_id

                    # Get last inserted IDs
                    last_inserted_ids = get_last_inserted_ids(connection, cursor)

                    # Insert into fact tables
                    fact_tables = [
                        table_name
                        for table_name in table_column_names.keys()
                        if table_name.startswith("fact_")
                    ]
                    for table_name in fact_tables:
                        column_names = table_column_names[table_name]
                        if column_names:  # Überprüfen, ob die Liste nicht leer ist
                            # Erstellen Sie eine Komma-getrennte Liste der Spaltennamen
                            column_names_str = ", ".join(column_names)

                            # Erstellen Sie eine Komma-getrennte Liste von Platzhaltern für die VALUES-Klausel basierend auf der Anzahl der Spalten
                            placeholders = ", ".join(["%s" for _ in column_names])

                            for column_name in column_names:
                                inserted_id = last_inserted_ids.get(column_name)
                                if inserted_id is None:
                                    print(f"ID für '{column_name}' nicht gefunden.")

                            # Die INSERT-Anweisung mit den Spaltennamen und Platzhaltern für die Werte
                            query = f"INSERT INTO {table_name} ({column_names_str}) VALUES ({placeholders})"
                            cursor.execute(
                                query,
                                tuple(last_inserted_ids[col] for col in column_names),
                            )
                        else:
                            print(
                                f"Spaltennamen für Tabelle '{table_name}' nicht gefunden."
                            )

                    connection.commit()
                    print("Dimension tables inserted successfully")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        consumer.close()


process_messages()
