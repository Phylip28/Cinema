import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_NAME = os.getenv("DATABASE_NAME")

def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def close_connection(conn):
    conn.close()