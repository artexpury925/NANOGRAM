import os

class Config:
    SECRET_KEY = "nanogram-secret-2025"
    SQLALCHEMY_DATABASE_URI = "sqlite:///nanogram.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False