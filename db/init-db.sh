#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE DATABASE LivingLabVisualization;
    CREATE USER lukasmetzler WITH ENCRYPTED PASSWORD 'lukasmetzler';
    GRANT ALL PRIVILEGES ON DATABASE evi TO lukasmetzler;
EOSQL

