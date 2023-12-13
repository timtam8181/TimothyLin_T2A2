from flask import Blueprint, request
from setup import db
from models.hotel import HotelSchema, Hotel
from models.location import Location

hotels_bp = Blueprint("hotel", __name__, url_prefix="/hotels")

# Get all hotels
@hotels_bp.route("/")
def all_hotels():
    stmt = db.select(Hotel)
    hotels = db.session.scalars(stmt).all()
    return HotelSchema(many=True).dump(hotels)

# Get one hotel
@hotels_bp.route('/<int:id>')
def one_hotel(id):
    stmt = db.select(Hotel).filter_by(id=id)
    hotel = db.session.scalar(stmt)
    if hotel:
        return HotelSchema().dump(hotel)
    else:
        return {'error': 'Hotel not found'}, 404


# Create a new hotel
@hotels_bp.route("/", methods=["POST"])
def create_hotel():
    try:
        hotel_info = HotelSchema().load(request.json)
        location_id = hotel_info.get("location_id")

        # Check if location_id is provided
        if location_id is None:
            return {"error": "location_id is required"}, 400

        # Check if the provided location_id corresponds to an existing Location
        if not Location.query.get(location_id):
            return {"error": f"Location with ID {location_id} not found"}, 404
        
        hotel = Hotel(
            name=hotel_info["name"],
            description=hotel_info["description"],
            price=hotel_info["price"],
            location_id=location_id
        )
        db.session.add(hotel)

        db.session.commit()

        # Return the serialized hotel information
        return HotelSchema().dump(hotel), 201

    except Exception as e:
        # Handle validation or database-related errors
        return {"error": str(e)}, 400


# Update a hotel
@hotels_bp.route("/<int:hotel_id>", methods=["PUT", "PATCH"])
def update_hotel(hotel_id):
    hotel_info = HotelSchema.load(request.json)
    stmt = db.select(Hotel).filter_by(id=hotel_id) 
    hotel = db.session.scalar(stmt)
    if hotel:
        hotel.name = hotel_info.get("name", hotel.name)
        hotel.description = hotel_info.get("description", hotel.description)
        hotel.price = hotel_info.get("price", hotel.price)
        db.session.commit()
        return HotelSchema().dump(hotel)
    else:
        return {"error": "Hotel not found"}, 404


# Delete a hotel
@hotels_bp.route("/<int:hotel_id>", methods=["DELETE"])
def delete_hotel(hotel_id):
    stmt = db.select(Hotel).filter_by(id=hotel_id)  
    hotel = db.session.scalar(stmt)
    if hotel:
        db.session.delete(hotel_id)
        db.session.commit()
        return {}, 200
    else:
        return {"error": "Hotel not found"}, 404