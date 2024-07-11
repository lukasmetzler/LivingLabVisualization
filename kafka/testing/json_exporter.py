import json
import random
import time
from datetime import datetime
from kafka import KafkaProducer


def generate_random_body():
    return {
        "id": random.randint(1, 1000),
        "unique_object_id": str(random.randint(1, 1000)),
        "tracking_state": random.choice(["TRACKED", "NOT_TRACKED"]),
        "action_state": random.choice(["STANDING", "WALKING", "SITTING"]),
        "confidence": random.uniform(0, 1),
        "keypoint": [random.uniform(-1, 1) for _ in range(18)],
        "head_position": [random.uniform(-1, 1) for _ in range(3)],
        "keypoint_confidence": [random.uniform(0, 1) for _ in range(18)],
    }


def generate_random_data():
    return {
        "is_new": random.choice([True, False]),
        "is_tracked": random.choice([True, False]),
        "timestamp": datetime.utcnow().isoformat(),
        "rotation": [random.uniform(-180, 180) for _ in range(3)],
        "bodies": [generate_random_body() for _ in range(random.randint(1, 5))],
    }


def main():
    producer = KafkaProducer(
        bootstrap_servers=["85.215.59.47:9092"],  # Kafka server address
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )

    topic = "zed_kamera_topic"

    try:
        while True:
            data = generate_random_data()
            producer.send(topic, value=data)
            print(f"Sent data: {data}")
            time.sleep(60)  # Wait for 1 minute
    except KeyboardInterrupt:
        print("Stopped by user")
    finally:
        producer.close()


if __name__ == "__main__":
    main()
