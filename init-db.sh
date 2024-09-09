#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE DATABASE grafana;
    GRANT ALL PRIVILEGES ON DATABASE grafana TO lukasmetzler;
EOSQL
