from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str = "sqlite:///./sql_app.db"
    microservice_api: str = "http://127.0.0.1:8088"

    class Config:
        env_file = '.env'


settings = Settings()
