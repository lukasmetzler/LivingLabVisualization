from flask import Flask, jsonify, request
from kafka import KafkaProducer
import json
import psycopg2

app = Flask(__name__)

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

# PostgreSQL Connection
conn = psycopg2.connect(
    host="localhost",
    database="EVI",
    user="lukasmetzler",
    password="lukasmetzler",
)

@app.route('/api/metrological_data', methods=['GET'])
def get_metrological_data():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM metrological_data')
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)

@app.route('/api/metrological_data', methods=['POST'])
def post_metrological_data():
    data = request.json

    # Senden an Kafka
    topic = "metrological-topic"
    producer.send(topic, value=data)
    print("Data sent to Kafka")

    return jsonify({"message": "Data posted successfully"}), 201


if __name__ == '__main__':
    app.run(debug=True)
