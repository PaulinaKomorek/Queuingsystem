from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class Appointment(db.Model):
    def __init__(self, purpose_idx: int, firstname: str, lastname: str):
        self.purpose_idx = purpose_idx
        self.firstname = firstname
        self.lastname = lastname

    __tablename__ = "appointment"
    idx = db.Column(db.Integer, primary_key=True)
    purpose_idx = db.Column(db.Integer, db.ForeignKey("purpose.idx"))
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    added_date=db.Column(db.DateTime, default=datetime.utcnow)


class Purpose(db.Model):
    __tablename__ = "purpose"
    idx = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))

    appointments = db.relationship("Appointment", backref="purpose", lazy=True)
