#!/bin/bash

# Wait for Kafka to start
sleep 10

# Create Kafka topic
/usr/bin/kafka-topics.sh --create --topic hella_data_topic --bootstrap-server kafka_new:9092 --replication-factor 1 --partitions 1
