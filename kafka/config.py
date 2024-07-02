import os
from dotenv import load_dotenv

_config_cache = None

class ProducerConfig:
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        env_file_path = os.path.join(current_dir, "..", "local.env")

        load_dotenv(dotenv_path=env_file_path)

        self.KAFKA_BOOTSTRAP_SERVER = os.environ.get("KAFKA_BOOTSTRAP_SERVER")
        self.KAFKA_TOPIC = os.environ.get("KAFKA_TOPIC")
        self.KAFKA_CERT_PATH = os.environ.get("KAFKA_CERT_PATH")
        self.PRODUCER_INTERVAL_SECONDS = int(os.environ.get("PRODUCER_INTERVAL_SECONDS", 60))
        self.CONSUMER_POSTGRES_USER = os.environ.get("CONSUMER_POSTGRES_USER")
        self.CONSUMER_POSTGRES_PASSWORD = os.environ.get("CONSUMER_POSTGRES_PASSWORD")
        self.CONSUMER_POSTGRES_DB = os.environ.get("CONSUMER_POSTGRES_DB")
        self.CONSUMER_POSTGRES_HOST = os.environ.get("CONSUMER_POSTGRES_HOST")
        self.CONSUMER_POSTGRES_PORT = int(os.environ.get("CONSUMER_POSTGRES_PORT", 5432))

def load_config() -> ProducerConfig:
    global _config_cache
    if not _config_cache:
        _config_cache = ProducerConfig()
    return _config_cache
