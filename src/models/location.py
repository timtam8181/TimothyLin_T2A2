from setup import db, ma
from wtforms import ValidationError

ALLOWED_CITIES = ["Melbourne", "Geelong", "Ballarat"]

class Location(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    restaurants = db.relationship('Restaurant', back_populates='location')
    hotels = db.relationship('Hotel', back_populates='location')
    attractions = db.relationship('Attraction', back_populates='location')

class LocationSchema(ma.Schema):
    def validate_name(self, value):
        if value not in ALLOWED_CITIES:
            raise ValidationError(f"Invalid city: {value}. Allowed cities are {', '.join(ALLOWED_CITIES)}.")
    class Meta:
        fields = ("id", "name", "description")