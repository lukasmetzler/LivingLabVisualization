#!/bin/bash

# Warten, bis Kafka gestartet ist
sleep 10

# Kafka-Themen erstellen
docker exec -it kafka_new kafka-topics --create --topic hella_data_topic --bootstrap-server kafka_new:9092 --partitions 1 --replication-factor 1
docker exec -it kafka_new kafka-topics --create --topic zed_kamera_topic --bootstrap-server kafka_new:9092 --partitions 1 --replication-factor 1
