from flask import Blueprint, request
from setup import db
from models.attraction import AttractionSchema, Attraction
from models.location import Location

attractions_bp = Blueprint("attraction", __name__, url_prefix="/attractions")

# Get all attractions
@attractions_bp.route("/")
def all_attractions():
    stmt = db.select(Attraction)
    attractions = db.session.scalars(stmt).all()
    return AttractionSchema(many=True).dump(attractions)

# Get one attraction
@attractions_bp.route('/<int:id>')
def one_attraction(id):
    stmt = db.select(attraction).filter_by(id=id)
    attraction = db.session.scalar(stmt)
    if attraction:
        return AttractionSchema().dump(attraction)
    else:
        return {'error': 'attraction not found'}, 404


# Create a new attraction
@attractions_bp.route("/", methods=["POST"])
def create_attraction():
    try:
        attraction_info = AttractionSchema().load(request.json)
        location_id = attraction_info.get("location_id")

        # Check if location_id is provided
        if location_id is None:
            return {"error": "location_id is required"}, 400

        # Check if the provided location_id corresponds to an existing Location
        if not Location.query.get(location_id):
            return {"error": f"Location with ID {location_id} not found"}, 404
        
        attraction = attraction(
            cuisine=attraction_info["cuisine"],
            price=attraction_info["price"],
            rating=attraction_info["rating"],
            location_id=location_id
        )
        db.session.add(attraction)

        db.session.commit()

        # Return the serialized attraction information
        return AttractionSchema().dump(attraction), 201

    except Exception as e:
        # Handle validation or database-related errors
        return {"error": str(e)}, 400


# Update a attraction
@attractions_bp.route("/<int:attraction_id>", methods=["PUT", "PATCH"])
def update_attraction(attraction_id):
    attraction_info = AttractionSchema.load(request.json)
    stmt = db.select(attraction).filter_by(id=attraction_id) 
    attraction = db.session.scalar(stmt)
    if attraction:
        attraction.name = attraction_info.get("name", attraction.name)
        attraction.price = attraction_info.get("price", attraction.price)
        attraction.description = attraction_info.get("description", attraction.description)
        db.session.commit()
        return AttractionSchema().dump(attraction)
    else:
        return {"error": "attraction not found"}, 404


# Delete a attraction
@attractions_bp.route("/<int:attraction_id>", methods=["DELETE"])
def delete_attraction(attraction_id):
    stmt = db.select(attraction).filter_by(id=attraction_id)  
    attraction = db.session.scalar(stmt)
    if attraction:
        db.session.delete(attraction)
        db.session.commit()
        return {}, 200
    else:
        return {"error": "attraction not found"}, 404