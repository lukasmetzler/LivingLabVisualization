## Checklist 24.06
- [ ] Datenbank zum Laufen bringen am Remote Server (Docker Container Stand mitnehmen vom lokalen oder Möglichkeit finden diesen zu deployen)
- [ ] Grafana Dashboards importieren
- [ ] Frontend bauen und anzeigen lassen, docker container sollte bereits production ready sein
- [ ] Kafka laufen lassen und in 1 min frequenz Werte pushen
- [ ] CI/CD aufbauen
- [ ] Dokumentation des gesamten Deployments um für HELLA vorbereitet zu sein
# Real-time Visualization of Building Industry Data

This project provides a real-time visualization solution for building industry data. It includes components for data acquisition, storage, processing, and visualization.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Stack](#stack)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before running this project, ensure you have the following installed:

- Docker: [Docker Installation Guide](https://docs.docker.com/get-docker/)
- Docker Compose: [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)

## Getting Started

### Stack

![](https://gitlab.com/lukasmetzler/echtzeitvisualisierung-von-gebaeudeindustriedaten/-/raw/main/docs/Finaler_Aufbau.png?ref_type=heads)

### Installation

#### 1. Clone the repository:

```bash
git clone https://gitlab.com/lukasmetzler/echtzeitvisualisierung-von-gebaeudeindustriedaten.git
cd echtzeitvisualisierung-von-gebaeudeindustriedaten
```

#### 2. Build the Docker images:

```bash
 docker-compose build
```

### Running the Application

#### 1. Start the Docker containers:

```bash
 docker-compose up -d
```

#### 2. Access the application:

- Grafana Dashboard: http://localhost:8080
- ReactJS: http://localhost:3000
- PgAdmin4: http://localhost:5050

## Project Structure

- `/grafana`: Contains the configuration files for Grafana.
- `/kafka`: Configuration for Kafka message broker.
- `/postgres`: Configuration for PostgreSQL database.
- `/frontend`: Includes the ReactJS Application
- `/db`: Includes relevant setup scripts for the Database

## Technologies used

- Python
- ReactJS
- Docker
- Kafka
- PostgreSQL
- Grafana
- Apache JMeter (coming soon...)

## License

This project is licensed under the [MIT License](https://opensource.org/license/mit/).

## Deployment Notes:
1. Datei außerhalb des Containers bearbeiten und mounten

    Lokale Kopie der grafana.ini erstellen und bearbeiten:

        Kopiere die grafana.ini aus dem Container auf dein lokales Dateisystem:

        bash

docker cp <container_id_or_name>:/etc/grafana/grafana.ini ./grafana.ini

Bearbeite die lokale grafana.ini Datei:

ini

    [server]
    root_url = http://85.215.59.47/grafana/
    serve_from_sub_path = true

Container mit gemounteter Datei neu starten:

    Starte den Container neu und mounte die bearbeitete grafana.ini:

    bash

        docker run -d -p 8080:3000 \
          -v $(pwd)/grafana.ini:/etc/grafana/grafana.ini \
          --name grafana \
          grafana/grafana

2. Umgebungsvariablen verwenden

Falls du die Konfiguration nicht über eine Datei ändern kannst, kannst du Umgebungsvariablen verwenden, um die Einstellungen zu überschreiben:

    Container mit den entsprechenden Umgebungsvariablen starten:

    bash

docker run -d -p 8080:3000 \
  -e "GF_SERVER_ROOT_URL=http://85.215.59.47/grafana/" \
  -e "GF_SERVER_SERVE_FROM_SUB_PATH=true" \
  --name grafana \
  grafana/grafana

