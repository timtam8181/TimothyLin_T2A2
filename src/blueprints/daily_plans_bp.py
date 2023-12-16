from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from setup import db
from models.daily_plan import DailyPlanSchema, DailyPlan
from auth import authorize
from flask_jwt_extended import jwt_required

daily_plans_bp = Blueprint('daily_plans', __name__, url_prefix='/daily_plans')

# Get all daily_plans
@daily_plans_bp.route("/")
@jwt_required()
def all_daily_plans():
    stmt = db.select(DailyPlan)
    daily_plans = db.session.scalars(stmt).all()
    return DailyPlanSchema(many=True, exclude=['user.daily_plans']).dump(daily_plans)

# Get one specific daily plan
@daily_plans_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def a_daily_plan(id):
    stmt = db.select(DailyPlan).filter_by(id=id) 
    daily_plan = db.session.scalar(stmt)
    if daily_plan:
        return DailyPlanSchema().dump(daily_plan)
    else:
        return {'error': 'daily plan not found'}, 404

# Create new daily plans
@daily_plans_bp.route('/', methods=['POST'])
@jwt_required()
def create_daily_plan():
    daily_plan_details = DailyPlanSchema(exclude=['id', 'date']).load(request.json)
    daily_plan = DailyPlan(
        restaurant = daily_plan_details['restaurant'],
        hotel = daily_plan_details.get('hotel'),
        attraction = daily_plan_details.get('attraction'),
        user_id = get_jwt_identity()
    )
    db.session.add(daily_plan)
    db.session.commit()
    return DailyPlanSchema().dump(daily_plan), 201

# Update daily plans
@daily_plans_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_daily_plan(id):
    daily_plan_details = DailyPlanSchema(exclude=['id', 'date_created']).load(request.json)
    stmt = db.select(DailyPlan).filter_by(id=id) 
    daily_plan = db.session.scalar(stmt)
    if daily_plan:
        authorize(daily_plan.user_id)
        daily_plan.restaurant = daily_plan_details.get('restaurant', daily_plan.restaurant)
        daily_plan.hotel = daily_plan_details.get('hotel', daily_plan.hotel)
        daily_plan.attraction = daily_plan_details.get('attraction', daily_plan.attractions)
        db.session.commit()
        return DailyPlanSchema().dump(daily_plan)
    else:
        return {'error': 'Card not found'}, 404

# Delete a daily plan
@daily_plans_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_daily_plan(id):
    stmt = db.select(DailyPlan).filter_by(id=id) 
    daily_plan = db.session.scalar(stmt)
    if daily_plan:
        authorize(daily_plan.user_id)
        db.session.delete(daily_plan)
        db.session.commit()
        return {"Deleted!"}, 200
    else:
        return {'error': 'Daily Plan could not be found!'}, 404