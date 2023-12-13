from setup import db, ma
# from models.hotel import Hotel
# from models.restaurant import Food
# from models.attraction import Attraction

class Location(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    restaurants = db.relationship('Restaurant', back_populates='location')

    # I don't think I need this code below
    # hotel_id = db.Column(db.Integer, db.ForeignKey('hotels.id'), nullable=False)
    # food_id = db.Column(db.Integer, db.ForeignKey('food.id'), nullable=False)
    # attraction_id = db.Column(db.Integer, db.ForeignKey('attraction.id'), nullable=False)

    # hotels = db.relationship('Hotel', back_populates='hotel')
    # foods = db.relationship('Food', back_populates='food')
    # attractions = db.relationship('Attraction', back_populates='attraction')

class LocationSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "description")