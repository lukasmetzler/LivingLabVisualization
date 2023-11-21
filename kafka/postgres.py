import contextlib
import psycopg2
import psycopg2.extensions

from . import config

@contextlib.contextmanager
def postgres_cursor_context(user: str = None,
                            password: str = None,
                            host: str = None,
                            port: int = None,
                            database: str = None,
                            sslmode: str = None) -> 'psycopg2.extensions.cursor':
    """Creates a context with a psycopg2 cursor for a database alias"""
    c = config.load_config()
    user = user if user is not None else c.CONSUMER_POSTGRES_USER
    password = password if password is not None else c.CONSUMER_POSTGRES_PASSWORD
    host = host if host is not None else c.CONSUMER_POSTGRES_HOST
    port = port if port is not None else c.CONSUMER_POSTGRES_PORT
    database = database if database is not None else c.CONSUMER_POSTGRES_DB
    ssl_mode = sslmode if sslmode is not None else c.CONSUMER_POSTGRES_SSL_MODE

    connection = psycopg2.connect(dbname=database, user=user, password=password,
                                  host=host, port=port, sslmode=ssl_mode)
    cursor = connection.cursor()
    try:
        yield cursor
        connection.commit();
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        cursor.close()
        connection.close()

