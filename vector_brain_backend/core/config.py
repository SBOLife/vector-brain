"""
Configuration module for application settings.

This module provides configuration management using Pydantic BaseSettings
to handle environment variables and configuration values securely.
"""

from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()


class Settings(BaseSettings):
    """
    Configuration settings class that loads environment variables.

    Inherits from BaseSettings to automatically read configuration from environment
    variables and .env files. Centralizes all application configuration.
    """

    DATABASE_URL: str

    class Config:
        """
        Inner configuration class for Settings.

        Specifies configuration options for the Settings class, including the
        environment file location and case sensitivity.
        """

        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


# Instantiate a single settings object to be used across the application
settings = Settings()
