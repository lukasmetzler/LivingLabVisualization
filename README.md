## Checklist 24.06
- [x] Datenbank zum Laufen bringen am Remote Server (Docker Container Stand mitnehmen vom lokalen oder Möglichkeit finden diesen zu deployen)
- [x] Grafana ini für die Produktion anpassen
- [x] Grafana Dashboards importieren
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
### 1. Datei außerhalb des Containers bearbeiten und mounten

1. **Lokale Kopie der `grafana.ini` erstellen und bearbeiten:**
   - Kopiere die `grafana.ini` aus dem Container auf dein lokales Dateisystem:

     ```bash
     docker cp <container_id_or_name>:/etc/grafana/grafana.ini ./grafana.ini
     ```

   - Bearbeite die lokale `grafana.ini` Datei:

     ```ini
     [server]
     root_url = http://85.215.59.47/grafana/
     serve_from_sub_path = true
     ```

2. **Container mit gemounteter Datei neu starten:**
   - Starte den Container neu und mounte die bearbeitete `grafana.ini`:

     ```bash
     docker run -d -p 8080:3000 \
       -v $(pwd)/grafana.ini:/etc/grafana/grafana.ini \
       --name grafana \
       grafana/grafana
     ```

### 2. Must have installationen für Server
```bash
sudo apt install nginx
```
#### Docker:
```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
```
```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```
```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
```bash
sudo apt-get install docker-compose
```
#### Etc.
```bash
sudo apt install python3-pip
```
#### Kafka
```bash
cd /var/www/echtzeitvisualisierung-von-gebaeudeindustriedaten/kafka
pip3 install -r requirements.txt
```

### 3. Nginx Einstellungen (Grafana etc.)
#### /etc/nginx/sites-available/hella
```nginx
server {
    listen 80;
    server_name 85.215.59.47;

    location /grafana/ {
        proxy_pass http://localhost:3000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "Upgrade";
        proxy_http_version 1.1;

        # Add trailing slash to avoid redirects
        rewrite ^/grafana$ /grafana/ permanent;
    }

    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
        root /usr/share/nginx/html;
    }
}
```
#### /var/www/echtzeitvisualisierung-von-gebaeudeindustriedaten/defaults.ini
```ini
[server]
protocol = http
min_tls_version = ""
http_addr =
http_port = 3000
domain = localhost
enforce_domain = false
# The full public facing url
root_url = %(protocol)s://%(domain)s:%(http_port)s/grafana/

# Serve Grafana from subpath specified in `root_url` setting. By default it is set to `false` for compatibility reasons.
serve_from_sub_path = true
router_logging = false
```
```ini
[database]

host = postgres_new:5432
name = postgres
user = lukasmetzler
password = lukasmetzler
```

### 4. Wichtige Details
```bash
docker-compose down --volumes --remove-orphans
docker-compose --env-file local.env up -d
```


### 5. Grafana Benutzer über POST Call erstellen
```bash
curl -X POST -H "Content-Type: application/json" -d '{
  "name":"New User",
  "email":"newuser@example.com",
  "login":"newuser",
  "password":"newuserpassword",
  "OrgId": 1
}' http://admin:admin@localhost:3000/api/admin/users
```

#### Datenbank-setup
```bash
docker exec -it postgres_new psql -U postgres
```
```postgres
-- Benutzer erstellen
CREATE USER lukasmetzler WITH PASSWORD 'lukasmetzler';

-- Datenbank erstellen
CREATE DATABASE your_database_name OWNER lukasmetzler;

-- Berechtigungen erteilen
GRANT ALL PRIVILEGES ON DATABASE your_database_name TO lukasmetzler;
```