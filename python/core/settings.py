import os
import sys

class Settings():
    PROJECT_NAME = 'smartETL'

    # variable pour postgres
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
    POSTGRES_DB = os.getenv("POSTGRES_DB", "postgres")
    POSTGRES_USER = os.getenv("POSTGRES_USER", "supever")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "Azerty01+")

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

settings = Settings()