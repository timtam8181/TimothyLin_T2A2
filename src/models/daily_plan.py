from setup import db, ma
from datetime import datetime
from marshmallow import fields

class DailyPlan(db.Model):
    __tablename__ = "daily_plans"

    id = db.Column(db.Integer, primary_key=True)

    restaurant = db.Column(db.String())
    hotel = db.Column(db.String())
    attraction = db.Column(db.String())
    date = db.Column(db.Date, default=datetime.now().strftime('%Y-%m-%d'))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


    user = db.relationship('User', back_populates='daily_plans')

class DailyPlanSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['name'])

    class Meta:
        fields = ("id", "restaurant", "hotel", "attraction", "date", "user_id", "user")