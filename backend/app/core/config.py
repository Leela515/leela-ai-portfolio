from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Leela AI Portfolio"
    version: str = "1.0.0"

settings = Settings()
    