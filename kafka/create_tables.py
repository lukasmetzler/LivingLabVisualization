# create_tables.py

from alembic import command
from alembic.config import Config
import os

# Lade die Alembic-Konfiguration
alembic_cfg = Config(os.path.join(os.path.dirname(__file__), "alembic.ini"))

# Führe die Migration aus
command.upgrade(alembic_cfg, "head")

print("Migrationen erfolgreich angewendet.")
