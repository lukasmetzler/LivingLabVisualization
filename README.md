# Echtzeitvisualisierung von Gebäudeindustriedaten

Dieses Projekt bietet eine Lösung zur Echtzeitvisualisierung von Gebäudeindustriedaten. Es umfasst Komponenten für Datenerfassung, Speicherung, Verarbeitung und Visualisierung. Docker Compose wird verwendet, um die verschiedenen Dienste (Datenbank, Kafka, Grafana, etc.) zu orchestrieren. Die Datenbankstruktur wird mithilfe von SQLAlchemy-Modellen (`models.py`) definiert und durch Alembic-Migrationen in der PostgreSQL-Datenbank angewendet.

## Inhaltsverzeichnis

- [Voraussetzungen](#voraussetzungen)
- [Projektstruktur](#projektstruktur)
- [Installation und Einrichtung](#installation-und-einrichtung)
  - [1. Repository klonen](#1-repository-klonen)
  - [2. Umgebungsvariablen konfigurieren](#2-umgebungsvariablen-konfigurieren)
  - [3. Docker-Container starten](#3-docker-container-starten)
- [Datenbankstruktur initial erstellen](#datenbankstruktur-initial-erstellen)
  - [1. Initiale Migration erstellen](#1-initiale-migration-erstellen)
  - [2. Migration anwenden](#2-migration-anwenden)
  - [3. Überprüfung der Tabellen](#3-überprüfung-der-tabellen)
- [Änderungen an der Datenbankstruktur vornehmen](#änderungen-an-der-datenbankstruktur-vornehmen)
  - [1. Modelle anpassen](#1-modelle-anpassen)
  - [2. Neue Migration erstellen](#2-neue-migration-erstellen)
  - [3. Migration anwenden](#3-migration-anwenden)
  - [4. Überprüfung der Änderungen](#4-überprüfung-der-änderungen)
- [Deployment-Anweisungen](#deployment-anweisungen)
  - [1. Datei außerhalb des Containers bearbeiten und mounten](#1-datei-ausserhalb-des-containers-bearbeiten-und-mounten)
    - [1.1. Lokale Kopie der `grafana.ini` erstellen und bearbeiten](#11-lokale-kopie-der-grafanaini-erstellen-und-bearbeiten)
    - [1.2. Container mit gemounteter Datei neu starten](#12-container-mit-gemounteter-datei-neu-starten)
  - [2. Notwendige Installationen für den Server](#2-notwendige-installationen-für-den-server)
    - [Docker installieren](#docker-installieren)
    - [Python3-Pip installieren](#python3-pip-installieren)
  - [3. Kafka-Setup](#3-kafka-setup)
    - [Python-Abhängigkeiten installieren](#python-abhängigkeiten-installieren)
    - [Kafka-Topics initialisieren](#kafka-topics-initialisieren)
  - [4. Grafana-Benutzer erstellen](#4-grafana-benutzer-erstellen)
  - [5. Datenbank-Setup](#5-datenbank-setup)
  - [6. Dockerisierung von Producer und Consumer](#6-dockerisierung-von-producer-und-consumer)
- [Technologien](#technologien)
- [Lizenz](#lizenz)
- [Fehlerbehebung](#fehlerbehebung)

## Voraussetzungen

Stelle sicher, dass die folgenden Tools auf dem System installiert sind:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python 3.10+](https://www.python.org/downloads/) (optional, falls lokale Skripte ausgeführt werden sollen)

## Projektstruktur

Die empfohlene Verzeichnisstruktur für das Projekt sieht wie folgt aus:

```
/var/www/echtzeitvisualisierung-von-gebaeudeindustriedaten/
├── docker-compose.yml
├── kafka/
│   ├── Dockerfile-init
│   ├── Dockerfile-consumer
│   ├── Dockerfile-producer
│   ├── create_tables.py
│   ├── models.py
│   ├── alembic/
│   │   ├── env.py
│   │   ├── alembic.ini
│   │   └── versions/
│   ├── requirements.txt
│   └── create-topic.sh
├── init-db.sh
├── nginx/
│   ├── nginx.conf
│   ├── conf.d/
│   ├── plugins.d/
│   ├── sites-enabled.d/
│   └── ssl/
├── visualization/
│   └── frontend/
├── portainer/
│   └── ... (optional, falls vorhanden)
└── ... (andere Verzeichnisse und Dateien)
```

## Installation und Einrichtung

### 1. Repository klonen

Repository auf den lokalen Rechner klonen:

```bash
git clone https://github.com/dein-username/echtzeitvisualisierung-von-gebaeudeindustriedaten.git
cd echtzeitvisualisierung-von-gebaeudeindustriedaten
```

### 2. Umgebungsvariablen konfigurieren

Eine `.env`-Datei im Stammverzeichnis des Projekts erstellen und die notwendigen Umgebungsvariablen hinzufügen:

```env
POSTGRES_USER=lukasmetzler
POSTGRES_PASSWORD=lukasmetzler
POSTGRES_DB=livinglabvisualization

KAFKA_TOPICS=hella_data_topic,zed_kamera_topic
PRODUCER_INTERVAL_SECONDS=5

JWT_SECRET=dein_jwt_secret
CONSUMER_POSTGRES_USER=lukasmetzler
CONSUMER_POSTGRES_PASSWORD=lukasmetzler
CONSUMER_POSTGRES_DB=livinglabvisualization
```

Sicherstellen, dass die `.env`-Datei die korrekten Werte enthält, insbesondere für die Datenbank- und Kafka-Konfiguration.

### 3. Docker-Container starten

Alle Docker-Container im Hintergrund starten:

```bash
docker-compose up -d
```

Den Status der laufenden Container überprüfen:

```bash
docker-compose ps
```

## Datenbankstruktur initial erstellen

Nachdem die Docker-Container laufen, muss die Datenbankstruktur basierend auf den SQLAlchemy-Modellen (`models.py`) erstellt werden. Dies geschieht mithilfe von Alembic-Migrationen.

### 1. Initiale Migration erstellen

In das `kafka`-Verzeichnis navigieren und eine initiale Migration erstellen:

```bash
cd kafka
alembic -c alembic/alembic.ini revision --autogenerate -m "Initial migration"
```

Dieser Befehl erstellt ein Migrationsskript unter `kafka/alembic/versions/`.

### 2. Migration anwenden

Die Migration anwenden, um die Tabellen in der Datenbank zu erstellen:

```bash
alembic -c alembic/alembic.ini upgrade head
```

Alternativ kann der `db-init`-Service verwendet werden, der automatisch die Migrationen anwendet:

```bash
docker-compose up --build db-init
```

### 3. Überprüfung der Tabellen

Mit der PostgreSQL-Datenbank verbinden und die Tabellen auflisten:

```bash
docker exec -it postgres_new psql -U lukasmetzler -d livinglabvisualization
```

Im PostgreSQL-Prompt:

```sql
\dt
```

Es sollten alle Tabellen aus `models.py` sowie die `alembic_version`-Tabelle sichtbar sein.

## Änderungen an der Datenbankstruktur vornehmen

Wenn Änderungen an den SQLAlchemy-Modellen (`models.py`) vorgenommen werden, müssen entsprechende Alembic-Migrationen erstellt und angewendet werden, um die Datenbankstruktur zu aktualisieren.

### 1. Modelle anpassen

Die `models.py` ändern oder erweitern, indem neue Tabellen hinzugefügt oder bestehende Modelle modifiziert werden.

### 2. Neue Migration erstellen

Eine neue Migration erstellen, die die Änderungen widerspiegelt:

```bash
cd kafka
alembic -c alembic/alembic.ini revision --autogenerate -m "Beschreibe die Änderung"
```

Dieser Befehl erstellt ein neues Migrationsskript unter `kafka/alembic/versions/`.

### 3. Migration anwenden

Die neue Migration anwenden:

```bash
alembic -c alembic/alembic.ini upgrade head
```

Oder den `db-init`-Service verwenden:

```bash
docker-compose up --build db-init
```

### 4. Überprüfung der Änderungen

Erneut mit der PostgreSQL-Datenbank verbinden und überprüfen, ob die Änderungen übernommen wurden:

```bash
docker exec -it postgres_new psql -U lukasmetzler -d livinglabvisualization
```

Im PostgreSQL-Prompt:

```sql
\dt
```

Die neuen oder geänderten Tabellen sollten sichtbar sein.

## Deployment-Anweisungen

### 1. Datei außerhalb des Containers bearbeiten und mounten

#### 1.1. Lokale Kopie der `grafana.ini` erstellen und bearbeiten

Die `grafana.ini` aus dem Container auf das lokale Dateisystem kopieren:

```bash
docker cp grafana_new:/etc/grafana/grafana.ini ./grafana.ini
```

Die lokale `grafana.ini` Datei bearbeiten:

```ini
[server]
root_url = http://85.215.59.47/grafana/
serve_from_sub_path = true
```

#### 1.2. Container mit gemounteter Datei neu starten

Den Container neu starten und die bearbeitete `grafana.ini` mounten:

```bash
docker run -d -p 3000:3000 \
  -v $(pwd)/grafana.ini:/etc/grafana/grafana.ini \
  --name grafana \
  grafana/grafana
```

### 2. Notwendige Installationen für den Server

#### Docker installieren

Alte Docker-Pakete entfernen:

```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

Docker's offizielles GPG-Key hinzufügen und das Repository einrichten:

```bash
# Docker's offizielles GPG-Key hinzufügen
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Repository zu Apt-Quellen hinzufügen
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

Docker Engine und Docker Compose installieren:

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Docker Compose separat installieren (falls nötig):

```bash
sudo apt-get install docker-compose
```

Python3-Pip installieren:

```bash
sudo apt install python3-pip
```

### 3. Kafka-Setup

#### Python-Abhängigkeiten installieren

In das `kafka`-Verzeichnis wechseln und die Python-Abhängigkeiten installieren:

```bash
cd /var/www/echtzeitvisualisierung-von-gebaeudeindustriedaten/kafka
pip3 install -r requirements.txt
```

#### Kafka-Topics initialisieren

Die benötigten Kafka-Topics erstellen:

```bash
docker exec -it kafka_new kafka-topics --create --topic hella_data_topic --bootstrap-server kafka_new:29092 --partitions 1 --replication-factor 1
docker exec -it kafka_new kafka-topics --create --topic zed_kamera_topic --bootstrap-server kafka_new:29092 --partitions 1 --replication-factor 1
```

### 4. Grafana-Benutzer erstellen

Einen neuen Grafana-Benutzer über einen POST-Call erstellen:

```bash
curl -X POST -H "Content-Type: application/json" -d '{
  "name":"Neuer Benutzer",
  "email":"newuser@example.com",
  "login":"newuser",
  "password":"newuserpassword",
  "OrgId": 1
}' http://admin:admin@localhost:3000/api/admin/users
```

### 5. Datenbank-Setup

Mit der PostgreSQL-Datenbank verbinden und den Benutzer sowie die Datenbank einrichten:

```bash
docker exec -it postgres_new psql -U postgres
```

Im PostgreSQL-Prompt:

```sql
-- Benutzer erstellen
CREATE USER lukasmetzler WITH PASSWORD 'lukasmetzler';

-- Datenbank erstellen
CREATE DATABASE livinglabvisualization OWNER lukasmetzler;

-- Berechtigungen erteilen
GRANT ALL PRIVILEGES ON DATABASE livinglabvisualization TO lukasmetzler;
```

### 6. Dockerisierung von Producer und Consumer

Docker-Images für Producer und Consumer bauen:

```bash
docker build -t kafka-producer -f Dockerfile-producer .
docker build -t kafka-consumer -f Dockerfile-consumer .
```

Docker-Container ausführen:

```bash
docker run -d --network=kafka-net --name kafka-producer kafka-producer
docker run -d --network=kafka-net --name kafka-consumer kafka-consumer
```

## Technologien

- **Python**
- **ReactJS**
- **Docker**
- **Kafka**
- **PostgreSQL**
- **Grafana**
- **pgAdmin4**
- **Portainer**
- **Nginx**
- **Apache JMeter** (kommt bald...)

## Lizenz

Dieses Projekt ist unter der [MIT-Lizenz](https://opensource.org/license/mit/) lizenziert.

---

## Fehlerbehebung

Bei Problemen die folgenden Punkte prüfen:

1. **Datenbankverbindung:** Sicherstellen, dass die PostgreSQL-Container laufen und die Umgebungsvariablen korrekt gesetzt sind.
2. **Alembic-Konfiguration:** Die `alembic.ini` und `env.py` überprüfen, um sicherzustellen, dass die `sqlalchemy.url` korrekt ist.
3. **Docker-Netzwerk:** Sicherstellen, dass alle relevanten Container im selben Docker-Netzwerk (`kafka-net`) sind.
4. **Logs prüfen:** Die Logs der Docker-Container überprüfen, um detaillierte Fehlermeldungen zu erhalten.

```bash
docker-compose logs db-init
docker-compose logs postgres_new
docker-compose logs kafka_new
docker-compose logs grafana_new
```