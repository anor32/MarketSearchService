from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    POSTGRES_CONNECTION_STRING: str = (
        "postgresql+asyncpg://postgres:postgres@localhost:5435/search_db"
    )
    KAFKA_BROKERS: str = "localhost:9092"
    KAFKA_TOPIC_ADS: str = "ads"
    kafka_consumer_group: str = "search-service"
    ad_service_url: str = "http://localhost:8002"
