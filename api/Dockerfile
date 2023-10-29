# Verwende ein Python-Basisimage
FROM python:3.8

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die Python-Anforderungen in den Container
COPY requirements.txt .

# Installiere die erforderlichen Pakete
RUN pip install -r requirements.txt

# Kopiere den Rest der API-Dateien in den Container
COPY . .

# Definiere den Startbefehl der API
CMD ["python", "app.py"]
