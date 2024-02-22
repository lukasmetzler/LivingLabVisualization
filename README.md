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
