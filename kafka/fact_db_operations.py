import psycopg2
import psycopg2 as sql
import logging
import config

def perform_inserts(data_for_tables):
    c = config.load_config()

    try:
        connection = psycopg2.connect(
            host = c.CONSUMER_POSTGRES_HOST,
            port = c.CONSUMER_POSTGRES_PORT,
            user = c.CONSUMER_POSTGRES_USER,
            password = c.CONSUMER_POSTGRES_PASSWORD,
            database = c.CONSUMER_POSTGRES_DB
        )
        cursor = connection.cursor()

        for table_name, column_names in data_for_tables.items():
            values = [data_for_tables[table_name].get(column, None) for column in column_names]

            if None in values:
                logging.error(f"Missing required keys in {table_name}.")
                continue

            columns_placeholder = sql.SQL(", ").join(sql.Identifier(column) for column in column_names)
            values_placeholder = sql.SQL(", ").join(sql.Placeholder() for _ in column_names)

            query = sql.SQL(f"INSERT INTO {sql.Identifier(table_name)} ({columns_placeholder}) VALUES ({values_placeholder})")

            cursor.execute(query,values)
            connection.commit()
        
        logging.info("INSERTS successfully executed.")

    except Exception as e:
        logging.error(f"An error occured during INSERTS: {e}")