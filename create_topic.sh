#!/bin/bash

/opt/bitnami/kafka/bin/kafka-topics.sh --create --topic dim_metrological_data_topic --bootstrap-server kafka:9092
echo "Topic test was created"

