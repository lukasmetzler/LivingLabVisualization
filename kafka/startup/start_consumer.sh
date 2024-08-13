#!/bin/sh
# Warte 80 Sekunden
sleep 80
# Starte den Kafka-Consumer
exec "$@"
