from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    """
    Application settings class that loads configuration from environment variables.
    Inherits from Pydantic's BaseSettings for automatic environment variable parsing.
    """

    DATABASE_URL: str
    OLLAMA_API_BASE_URL: str
    OLLAMA_MODEL: str
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000

    class Config:
        """
        Configuration class for Settings.
        Specifies configuration options for environment variable loading.
        """

        env_file = ".env"


settings = Settings()
