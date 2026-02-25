from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

# ------------------ User ------------------
class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=True)
    role = db.Column(db.String(20), default='member')
    is_active = db.Column(db.Boolean, default=True)

    places = db.relationship('Place', backref='user', lazy=True)
    logs = db.relationship('SystemLog', backref='user', lazy=True)


# ------------------ Category ------------------
class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    places = db.relationship('Place', backref='category', lazy=True)


# ------------------ Province ------------------
class Province(db.Model):
    __tablename__ = 'province'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    places = db.relationship('Place', backref='province', lazy=True)


# ------------------ Place ------------------
class Place(db.Model):
    __tablename__ = 'place'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    approved = db.Column(db.Boolean, default=False)
    image = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    province_id = db.Column(db.Integer, db.ForeignKey('province.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    images = db.relationship('PlaceImage', backref='place', lazy=True, cascade='all, delete-orphan')


# ------------------ PlaceImage ------------------
class PlaceImage(db.Model):
    __tablename__ = 'place_image'

    id = db.Column(db.Integer, primary_key=True)
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'), nullable=False)
    image_path = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# ------------------ Recommend ------------------
class Recommend(db.Model):
    __tablename__ = 'recommend'

    id = db.Column(db.Integer, primary_key=True)
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'), nullable=False)

    title = db.Column(db.String(200))
    content = db.Column(db.Text)
    image = db.Column(db.String(255))
    approved = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    place = db.relationship('Place', backref='recommends')



# ------------------ Comment ------------------
class Comment(db.Model):
    __tablename__ = "comment"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    place_id = db.Column(db.Integer, db.ForeignKey("place.id"), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

    user = db.relationship("User", backref="user_comments")
    place = db.relationship("Place", backref="comments")


# ------------------ System Log ------------------
class SystemLog(db.Model):
    __tablename__ = 'system_log'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    action = db.Column(db.String(100))
    detail = db.Column(db.Text)
    ip_address = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
