from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
import time
import psycopg2

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

topic = "test-topic"

# PostgreSQL Connection
conn = psycopg2.connect(
    host="localhost",
    database="lukasmetzler",  # Hier deinen Benutzernamen einsetzen
    user="lukasmetzler",  # Hier deinen Benutzernamen einsetzen
    password="",
)

try:
    while True:
        data = {"value1": 42, "value2": 56}

        # Senden an Kafka
        producer.send(topic, value=data)
        print("Data sent to Kafka")

        # Speichern in PostgreSQL
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO test_table (value1, value2) VALUES (%s, %s)",
            (data["value1"], data["value2"]),
        )
        conn.commit()
        cursor.close()

        print("Data saved to PostgreSQL")

        time.sleep(60)  # Warte 60 Sekunden zwischen den Nachrichten

except KeyboardInterrupt:
    producer.close()
    conn.close()
