from setup import db, ma
from marshmallow import fields
from sqlalchemy import ForeignKeyConstraint

class Attraction(db.Model):
    __tablename__ = "attractions"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    price = db.Column(db.String, default=[])
   
    # Define ForeignKey with constraints
    location_id = db.Column(db.Integer, nullable=False)
    location = db.relationship('Location', back_populates='restaurants')

    # Add ForeignKeyConstraint
    __table_args__ = (ForeignKeyConstraint(['location_id'], ['locations.id']),)

class AttractionSchema(ma.Schema):
    location = fields.Nested('LocationSchema')
    class Meta:
        fields = ("id", "cuisine", "price", "rating", "location_id")