from flask_sqlalchemy import SQLAlchemy
from PIL import Image

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(80), nullable=False, default="user")
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    avatar = db.Column(db.String(256), nullable=True,
                       default=f'static/images/default_avatar.jpg')

    def __repr__(self):
        return f"{self.username} - {self.email}"

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at,
        }
