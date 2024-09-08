from sqlalchemy import create_engine
from models import Base
from config import load_config

c = load_config()
engine = create_engine(
    f"postgresql+psycopg2://{c.CONSUMER_POSTGRES_USER}:{c.CONSUMER_POSTGRES_PASSWORD}@{c.CONSUMER_POSTGRES_HOST}:{c.CONSUMER_POSTGRES_PORT}/{c.CONSUMER_POSTGRES_DB}"
)

# Alle Tabellen löschen
Base.metadata.drop_all(engine)

# Alle Tabellen neu erstellen
Base.metadata.create_all(engine)

print("Datenbank wurde zurückgesetzt und neu erstellt.")
