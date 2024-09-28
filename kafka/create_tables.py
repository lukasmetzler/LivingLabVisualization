# create_tables.py

import time
import os
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from alembic import command
from alembic.config import Config

DATABASE_URL = os.getenv("DATABASE_URL")

# Warte auf die Datenbankverbindung
print("Warte auf PostgreSQL...")
for i in range(30):
    try:
        engine = create_engine(DATABASE_URL)
        connection = engine.connect()
        connection.close()
        print("PostgreSQL ist verfügbar")
        break
    except OperationalError:
        print("PostgreSQL ist noch nicht verfügbar, warte...")
        time.sleep(1)
else:
    print("Fehler: Konnte keine Verbindung zur Datenbank herstellen.")
    exit(1)

# Lade die Alembic-Konfiguration
alembic_cfg = Config(os.path.join(os.path.dirname(__file__), "alembic.ini"))

# Führe die Migration aus
command.upgrade(alembic_cfg, "head")

print("Migrationen erfolgreich angewendet.")
