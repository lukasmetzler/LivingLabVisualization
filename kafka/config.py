import os
from dotenv import load_dotenv

_config_cache = None


class ProducerConfig:
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        env_file_path = os.path.join(current_dir, "..", "local.env")

        print(f"Loading .env file from: {env_file_path}")  # Debugging-Ausgabe
        if not os.path.exists(env_file_path):
            print(f".env file not found at: {env_file_path}")  # Debugging-Ausgabe
        else:
            print(f".env file found at: {env_file_path}")  # Debugging-Ausgabe

        load_dotenv(dotenv_path=env_file_path)

        # Debugging-Ausgabe aller geladenen Umgebungsvariablen
        for key, value in os.environ.items():
            print(f"{key}: {value}")

        self.KAFKA_BOOTSTRAP_SERVER = os.environ.get("KAFKA_BOOTSTRAP_SERVER")
        kafka_topic_str = os.environ.get("KAFKA_TOPICS")  # Verwenden Sie KAFKA_TOPICS

        print(f"Raw KAFKA_TOPICS from .env: {kafka_topic_str}")  # Debugging-Ausgabe

        if kafka_topic_str:
            self.KAFKA_TOPICS = kafka_topic_str.split(",")
        else:
            self.KAFKA_TOPICS = []

        self.KAFKA_CERT_PATH = os.environ.get("KAFKA_CERT_PATH")
        self.PRODUCER_INTERVAL_SECONDS = int(
            os.environ.get("PRODUCER_INTERVAL_SECONDS", 60)
        )
        self.CONSUMER_POSTGRES_USER = os.environ.get("CONSUMER_POSTGRES_USER")
        self.CONSUMER_POSTGRES_PASSWORD = os.environ.get("CONSUMER_POSTGRES_PASSWORD")
        self.CONSUMER_POSTGRES_DB = os.environ.get("CONSUMER_POSTGRES_DB")
        self.CONSUMER_POSTGRES_HOST = os.environ.get("CONSUMER_POSTGRES_HOST")
        self.CONSUMER_POSTGRES_PORT = int(
            os.environ.get("CONSUMER_POSTGRES_PORT", 5432)
        )


def load_config() -> ProducerConfig:
    global _config_cache
    if not _config_cache:
        _config_cache = ProducerConfig()
    return _config_cache
