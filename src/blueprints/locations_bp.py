from flask import Blueprint, request
from setup import db
from models.location import LocationSchema, Location
from auth import authorize
from flask_jwt_extended import jwt_required

locations_bp = Blueprint('locations', __name__, url_prefix='/locations')

ALLOWED_CITIES = ["Melbourne", "Geelong", "Ballarat"]

# Get all locations
@locations_bp.route("/")
@jwt_required()
def all_locations():
    stmt = db.select(Location)  
    locations = db.session.scalars(stmt).all()
    return LocationSchema(many=True).dump(locations)

# Get one location
@locations_bp.route('/<int:id>')
@jwt_required()
def one_location(id):
    stmt = db.select(Location).filter_by(id=id)
    location = db.session.scalar(stmt)
    if location:
        return LocationSchema().dump(location)
    else:
        return {'error': 'That is not a location!'}, 404

# Create a new location
@locations_bp.route('/', methods=['POST'])
@jwt_required()
def create_location():
    authorize()
    location_details = LocationSchema(exclude=['id']).load(request.json)

    # Check if the provided city is allowed
    if location_details['name'] not in ALLOWED_CITIES:
        return {'error': 'Invalid city, choose from "Melbourne", "Geelong", "Ballarat"'}, 400    

    location = Location(
        name = location_details['name'],
        description = location_details.get('description')
    )
    db.session.add(location)
    db.session.commit()
    return LocationSchema().dump(location), 201

# Update a location
@locations_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_location(id):
    authorize()
    location_info = LocationSchema(exclude=['id']).load(request.json)
    stmt = db.select(Location).filter_by(id=id)
    location = db.session.scalar(stmt)
    if not location:
        return {'error': 'Location not found'}, 404

    # Check if the provided city is allowed
    new_city = location_info.get('name', location.name)
    if new_city not in ALLOWED_CITIES:
        return {'error': 'Invalid city, choose from "Melbourne", "Geelong", "Ballarat"'}, 400

    location.name = new_city
    location.description = location_info.get('description', location.description)
    db.session.commit()
    return LocationSchema().dump(location)

# Delete a location
@locations_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_location(id):
    authorize()
    stmt = db.select(Location).filter_by(id=id)
    location = db.session.scalar(stmt)
    if location:
        db.session.delete(location)
        db.session.commit()
        return {}, 200
    else:
        return {'error': 'Location not found'}, 404
