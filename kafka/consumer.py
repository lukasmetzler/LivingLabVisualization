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
            filtered_values = [table_data.get(column, None) for column in column_names if not column.endswith('_id')]

            # Filter out ID columns from the column names
            filtered_columns = [column for column in column_names if not column.endswith('_id')]

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

def get_dimension_data(connection, cursor, table_name, key_column, key_value):
    try:
        query = f"SELECT * FROM {table_name} WHERE {key_column} = %s"
        cursor.execute(query, (key_value,))
        result = cursor.fetchone()
        return result
    except Exception as e:
        logging.error(f"An error occurred while fetching data from {table_name}: {e}")
        return None



def insert_data_into_fact_table(connection, cursor, table_name, column_names, data, dimension_ids):
    try:
        if isinstance(data, dict):
            table_data = data.get(table_name)
            print(table_data)

            if table_data is None:
                logging.error(
                    f"Table data for '{table_name}' not found in the message. Skipping message."
                )
                return

            values = [table_data.get(column) for column in column_names]
            print(column_names)
            print(values)
            #print(values)
            # Replace foreign keys in the fact table data with the corresponding IDs from the dimension tables
            for i, values in enumerate(values):
                if column_names[i] in dimension_ids:
                    dimension_id = dimension_ids[column_names[i]]
                    #print("DimensionIDs: ", dimension_id)
                    if dimension_id:
                        values[i] = dimension_id
                    else:
                        logging.error(
                            f"Failed to retrieve the last inserted ID for column '{column_names[i]}' in dimension table '{table_name}'. Skipping message."
                        )
                        return
                else:
                    logging.error(
                        f"No dimension ID found for column '{column_names[i]}' in dimension table '{table_name}'. Skipping message."
                    )
                    return

            columns_placeholder = (", ").join(column for column in column_names)
            values_placeholder = (", ").join(["%s" for _ in column_names])

            query = f"INSERT INTO {table_name} ({columns_placeholder}) VALUES ({values_placeholder})"
            cursor.execute(query, values)
            logging.info(f"Data inserted into {table_name}")
    except Exception as e:
        logging.error(f"An error occurred while inserting data into {table_name}: {e}")
        connection.rollback()



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

                    # Insert into fact tables using foreign keys from dimension tables
                    for table_name, column_names in fact_table_column_names.items():
                        insert_data_into_fact_table(
                            connection,
                            cursor,
                            table_name,
                            column_names,
                            message.value,
                            dimension_ids,
                        )

                    connection.commit()

    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        consumer.close()


process_messages()
