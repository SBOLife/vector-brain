from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str
    OLLAMA_API_BASE_URL: str
    OLLAMA_MODEL: str
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    class Config:
        env_file = ".env"
settings = Settings()