from setup import db, ma
from marshmallow import fields
from marshmallow.validate import Length
from models.daily_plan import DailyPlanSchema


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
     
    daily_plans = db.relationship('DailyPlan', back_populates='user')


class UserSchema(ma.Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=Length(min=10, error='Password must be at least 10 characters'))
    daily_plans = fields.Nested(DailyPlanSchema, many=True, exclude=['user'])

    class Meta:
        model = User
        fields = ("id", "name", "email", "password", "is_admin", "daily_plans")        

