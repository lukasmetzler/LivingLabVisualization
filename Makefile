#!make
SHELL := /bin/bash

run : run-local

run-local: start-infra-local
	make -j run-producer-local run-consumer-local

run-%-local:
	source .venv/bin/activate && cd src && KAFKA_ENV_PATH=../local.env python3 -m kafka $*

build-docker:
	docker build -t kafka:latest -f ./Dockerfile .

restart-containers:
	docker-compose down --volumes --remove-orphans
	docker-compose up -d --build

start-infra-local:
	docker-compose --env-file local.env up -d

stop-infra-local:
	docker-compose --env-file local.env down