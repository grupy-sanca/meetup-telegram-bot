from pydantic import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    TELEGRAM_TOKEN: str
    MEETUP_API_TOKEN: str
    MEETUP_GROUP_ID: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
