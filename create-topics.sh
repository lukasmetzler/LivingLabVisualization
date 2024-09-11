#!/bin/bash

# Warten, bis Kafka verfügbar ist
cub kafka-ready -b kafka_new:29092 1 20

# Topics erstellen
kafka-topics --create --topic hella_data_topic --bootstrap-server kafka_new:29092 --partitions 1 --replication-factor 1
kafka-topics --create --topic zed_kamera_topic --bootstrap-server kafka_new:29092 --partitions 3 --replication-factor 1
