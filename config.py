import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "nanogram-secret-2025")
    
    # Main database (users, posts, likes, comments)
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///nanogram.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Your personal MEGA account – used as unlimited media storage
    MEGA_EMAIL = os.getenv("MEGA_EMAIL", "arnoldkipruto193@gmail.com")
    MEGA_PASSWORD = os.getenv("MEGA_PASSWORD", "marnold6001")