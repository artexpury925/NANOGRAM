# models.py – replace your current User class with this
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import os

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    
    # NEW FIELDS
    profile_pic = db.Column(db.String(200), default="default.jpg")  # filename
    phone = db.Column(db.String(20), nullable=True, unique=True)     # optional
    email = db.Column(db.String(120), nullable=True, unique=True)   # optional
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)