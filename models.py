from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
import bcrypt

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Integer, primary_key=True)
    username = db.String(80), unique=True, nullable=False)
    email = db.String(120), unique=True, nullable=False)
    password_hash = db.String(128), nullable=False)
    profile_pic = db.String(200), default="default.jpg")
    bio = db.Text, nullable=True)
    created_at = db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))