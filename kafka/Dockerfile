# Verwende ein Python-Basisimage
FROM python:3.8

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die Kafka-Anforderungen in den Container
COPY requirements.txt .

# Installiere die erforderlichen Pakete
RUN pip install -r requirements.txt

# Kopiere den Rest der Kafka-Dateien in den Container
COPY . .

# Definiere den Startbefehl für den Producer
CMD ["python", "producer.py"]
