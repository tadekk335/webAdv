from webapp import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class TravelPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140),nullable=False)
    data = db.Column(db.String(10000),nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    posts = db.relationship('TravelPost',backref='author')
