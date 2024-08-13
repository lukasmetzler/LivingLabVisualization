#!/bin/sh
# Warte 50 Sekunden
sleep 50
# Starte den Kafka-Producer
exec "$@"
