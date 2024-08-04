#!/bin/bash
set -e

docker exec -i postgres_new psql -U "$POSTGRES_USER" <<-EOSQL
    CREATE DATABASE LivingLabVisualization;
    CREATE USER lukasmetzler WITH ENCRYPTED PASSWORD 'lukasmetzler';
    GRANT ALL PRIVILEGES ON DATABASE LivingLabVisualization TO lukasmetzler;
EOSQL
