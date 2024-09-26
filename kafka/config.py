import os
from dotenv import load_dotenv

_config_cache = None


class ProducerConfig:
    def __init__(self):
        import logging

        logger = logging.getLogger(__name__)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        env_file_path = os.path.join(current_dir, "..", ".env")

        logger.debug(f"Loading .env file from: {env_file_path}")
        if os.path.exists(env_file_path):
            logger.debug(f".env file found at: {env_file_path}")
            load_dotenv(dotenv_path=env_file_path)
        else:
            logger.warning(f".env file not found at: {env_file_path}")
            # Proceed without loading .env file

        # Fetch environment variables
        self.KAFKA_BOOTSTRAP_SERVER = os.environ.get("KAFKA_BOOTSTRAP_SERVER")
        kafka_topic_str = os.environ.get("KAFKA_TOPICS")

        logger.debug(f"Raw KAFKA_TOPICS from environment: {kafka_topic_str}")

        if kafka_topic_str:
            self.KAFKA_TOPICS = [topic.strip() for topic in kafka_topic_str.split(",")]
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

        # Check for missing required environment variables
        missing_vars = []
        required_vars = [
            "CONSUMER_POSTGRES_USER",
            "CONSUMER_POSTGRES_PASSWORD",
            "CONSUMER_POSTGRES_DB",
            "CONSUMER_POSTGRES_HOST",
            "KAFKA_BOOTSTRAP_SERVER",
            "KAFKA_TOPICS",
        ]

        for var in required_vars:
            if not getattr(self, var):
                missing_vars.append(var)

        if missing_vars:
            logger.error(
                f"Missing required environment variables: {', '.join(missing_vars)}"
            )
            raise EnvironmentError(
                f"Missing required environment variables: {', '.join(missing_vars)}"
            )


def load_config() -> ProducerConfig:
    global _config_cache
    if not _config_cache:
        _config_cache = ProducerConfig()
    return _config_cache
