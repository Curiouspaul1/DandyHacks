from core import db


class EnergyProfile(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(100))
    type_ = db.Column(db.String(50), default='city')
    daily_consumption = db.Column(db.Float)
    profile = db.relationship('EnergyProfile', backref='consumer')
