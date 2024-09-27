from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base  # Stelle sicher, dass deine Modelle in models.py sind

# Datenbankverbindung
DATABASE_URL = (
    "postgresql://lukasmetzler:lukasmetzler@postgres_new:5432/livinglabvisualization"
)

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Erstelle alle Tabellen
Base.metadata.create_all(engine)

print("Alle Tabellen wurden erfolgreich erstellt.")
