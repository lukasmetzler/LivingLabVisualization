SHELL := /bin/bash

run: run-local

run-local: start-infra-local
	make run-consumer-local
	make run-producer-local

# python3 -m pip install kafka-python - on local system or server and  python3 -m pip install psycopg2 !!
run-all-local: install-dependencies run-producer-local run-consumer-local

run-consumer-local:
	cd kafka && KAFKA_ENV_PATH=../local.env python3 -m consumer &

run-producer-local:
	cd kafka && KAFKA_ENV_PATH=../local.env python3 -m producer &

build-docker:
	docker build -t kafka:latest -f ./Dockerfile .

restart-containers:
	docker-compose down --volumes --remove-orphans
	docker-compose up -d --build

start-infra-local:
	docker-compose --env-file local.env up -d

stop-infra-local:
	docker-compose --env-file local.env down

install-dependencies:
	cd kafka && pip3 install -r requirements.txt

create-topics-local: start-infra-local
	docker exec -it kafka_new kafka-topics --create --topic hella_data_topic --bootstrap-server kafka_new:9092 --partitions 1 --replication-factor 1
	docker exec -it kafka_new kafka-topics --create --topic zed_kamera_topic --bootstrap-server kafka_new:9092 --partitions 1 --replication-factor 1

