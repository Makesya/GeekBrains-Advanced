from flask_sqlalchemy import SQLAlchemy
from enum import Enum
from uuid import uuid4

db = SQLAlchemy()

status = Enum("status", ["unactive", "active", "banned", "deleted"])


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(80), nullable=False, default="user")
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    status = db.Column(db.Enum(status), nullable=False, default="unactive")
    level = db.Column(db.String(80), nullable=False, default="Рядовой")
    token = db.Column(db.String(32), nullable=True,
                      default=lambda: uuid4().hex)
    # ... existing code ...
    avatar = db.Column(db.String(256), nullable=True,
                       default=f'/static/images/default_avatar.jpg')

    def __repr__(self):
        return f"{self.username} - {self.email}"

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at,
        }


class SocialNetworks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    website = db.Column(db.String(80), default="None")
    github = db.Column(db.String(80), default="None")
    instagram = db.Column(db.String(80), default="None")
    vk = db.Column(db.String(80), default="None")
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return f"{self.website} - {self.github}"

    def serialize(self):
        return {
            "id": self.id,
            "website": self.website,
            "github": self.github,
            "instagram": self.instagram,
            "vk": self.vk
        }
