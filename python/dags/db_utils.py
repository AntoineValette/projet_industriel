"""
# db_utils.py
import psycopg2
import os
from contextlib import contextmanager

POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_DB = os.getenv("POSTGRES_DB", "postgres")
POSTGRES_USER = os.getenv("POSTGRES_USER", "admin")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "admin")

@contextmanager
def get_db_connection():
    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        dbname=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD
    )
    try:
        yield conn
    finally:
        conn.close()
"""

# db_utils.py
import os
from contextlib import contextmanager
from sqlalchemy import create_engine

POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_DB = os.getenv("POSTGRES_DB", "postgres")
POSTGRES_USER = os.getenv("POSTGRES_USER", "admin")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "admin")

POSTGRES_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Create the SQLAlchemy engine (you can adjust additional engine options as needed)
engine = create_engine(POSTGRES_URL)

@contextmanager
def get_db_connection():
    """Context manager that yields a SQLAlchemy connection."""
    conn = engine.connect()  # Establish a connection using SQLAlchemy
    try:
        yield conn
    finally:
        conn.close()