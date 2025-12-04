import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "nanogram-secret-2025")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///nanogram.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False