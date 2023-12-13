from flask import Blueprint, request
from setup import db
from models.restaurant import RestaurantSchema, Restaurant
from models.location import Location

restaurants_bp = Blueprint("restaurant", __name__, url_prefix="/restaurants")

# Get all restaurants
@restaurants_bp.route("/")
def all_restaurants():
    stmt = db.select(Restaurant)
    restaurants = db.session.scalars(stmt).all()
    return RestaurantSchema(many=True).dump(restaurants)

# Get one comment
@restaurants_bp.route('/<int:id>')
def one_restaurant(id):
    stmt = db.select(Restaurant).filter_by(id=id)
    restaurant = db.session.scalar(stmt)
    if restaurant:
        return RestaurantSchema().dump(restaurant)
    else:
        return {'error': 'Restaurant not found'}, 404


# Create a new restaurant
@restaurants_bp.route("/", methods=["POST"])
def create_restaurant():
    try:
        restaurant_info = RestaurantSchema().load(request.json)
        location_id = restaurant_info.get("location_id")

        # Check if location_id is provided
        if location_id is None:
            return {"error": "location_id is required"}, 400

        # Check if the provided location_id corresponds to an existing Location
        if not Location.query.get(location_id):
            return {"error": f"Location with ID {location_id} not found"}, 404
        
        restaurant = Restaurant(
            cuisine=restaurant_info["cuisine"],
            price=restaurant_info["price"],
            rating=restaurant_info["rating"],
            location_id=location_id
        )
        db.session.add(restaurant)

        db.session.commit()

        # Return the serialized restaurant information
        return RestaurantSchema().dump(restaurant), 201

    except Exception as e:
        # Handle validation or database-related errors
        return {"error": str(e)}, 400


# Update a restaurant
@restaurants_bp.route("/<int:restaurant_id>", methods=["PUT", "PATCH"])
def update_restaurant(restaurant_id):
    restaurant_info = RestaurantSchema.load(request.json)
    stmt = db.select(Restaurant).filter_by(id=restaurant_id) 
    restaurant = db.session.scalar(stmt)
    if restaurant:
        restaurant.cuisine = restaurant_info.get("cuisine", restaurant.cuisine)
        restaurant.price = restaurant_info.get("price", restaurant.price)
        restaurant.rating = restaurant_info.get("rating", restaurant.rating)
        db.session.commit()
        return RestaurantSchema().dump(restaurant)
    else:
        return {"error": "Restaurant not found"}, 404


# Delete a restaurant
@restaurants_bp.route("/<int:restaurant_id>", methods=["DELETE"])
def delete_restaurant(restaurant_id):
    stmt = db.select(Restaurant).filter_by(id=restaurant_id)  
    restaurant = db.session.scalar(stmt)
    if restaurant:
        db.session.delete(restaurant)
        db.session.commit()
        return {}, 200
    else:
        return {"error": "Restaurant not found"}, 404