import contextlib
import psycopg2
import psycopg2.extensions
import config
import logging


@contextlib.contextmanager
def postgres_connection(
    user: str = None,
    password: str = None,
    host: str = None,
    port: int = None,
    database: str = None,
) -> "psycopg2.extensions.connection":
    """Creates a context with a psycopg2 connection for a database alias"""
    c = config.load_config()
    user = user if user is not None else c.CONSUMER_POSTGRES_USER
    password = password if password is not None else c.CONSUMER_POSTGRES_PASSWORD
    host = host if host is not None else c.CONSUMER_POSTGRES_HOST
    port = port if port is not None else c.CONSUMER_POSTGRES_PORT
    database = database if database is not None else c.CONSUMER_POSTGRES_DB

    connection = psycopg2.connect(
        dbname=database, user=user, password=password, host=host, port=port
    )
    logging.info("Connected to PostgreSQL database.")
    try:
        yield connection
    except Exception as e:
        raise e
    finally:
        connection.close()
