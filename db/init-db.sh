#!/bin/bash
set -e

# Warten, bis PostgreSQL gestartet ist
sleep 10

# Ausführen der SQL-Befehle im PostgreSQL-Container
docker exec -i postgres_new psql -U lukasmetzler -d postgres <<-EOSQL
    CREATE DATABASE LivingLabVisualization;
    CREATE USER hella WITH ENCRYPTED PASSWORD 'hella';
    GRANT ALL PRIVILEGES ON DATABASE LivingLabVisualization TO lukasmetzler;
EOSQL
