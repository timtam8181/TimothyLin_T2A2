from flask import Blueprint, request
from setup import db
from models.location import LocationSchema, Location
from auth import authorize

locations_bp = Blueprint('locations', __name__, url_prefix='/locations')

# Get all locations
@locations_bp.route("/")
def all_locations():
    stmt = db.select(Location)  
    locations = db.session.scalars(stmt).all()
    return LocationSchema(many=True).dump(locations)

# Get one location
@locations_bp.route('/<int:id>')
def one_location(id):
    stmt = db.select(Location).filter_by(id=id)
    location = db.session.scalar(stmt)
    if location:
        return LocationSchema().dump(location)
    else:
        return {'error': 'That is not a location!'}, 404

# Create a new location
@locations_bp.route('/', methods=['POST'])
def create_location():
    location_details = LocationSchema(exclude=['id']).load(request.json)
    location = Location(
        name = location_details['name'],
        description = location_details.get('description')
    )
    db.session.add(location)
    db.session.commit()
    return LocationSchema().dump(location), 201

# Update a location
@locations_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def update_location(id):
    location_info = LocationSchema(exclude=['id']).load(request.json)
    stmt = db.select(Location).filter_by(id=id)
    location = db.session.scalar(stmt)
    if location:
        location.name = location_info.get('name', location.name)
        location.description = location_info.get('description', location.description)
        db.session.commit()
        return LocationSchema().dump(location)
    else:
        return {'error': 'Location can not be found'}, 404

# Delete a location
@locations_bp.route('/<int:id>', methods=['DELETE'])
def delete_location(id):
    stmt = db.select(Location).filter_by(id=id)
    location = db.session.scalar(stmt)
    if location:
        db.session.delete(location)
        db.session.commit()
        return {}, 200
    else:
        return {'error': 'Location not found'}, 404
