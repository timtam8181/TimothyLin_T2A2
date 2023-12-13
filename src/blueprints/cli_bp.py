from flask import Blueprint
from setup import db, bcrypt
from models.daily_plan import DailyPlan
from models.user import User
from models.location import Location
from models.restaurant import Restaurant

db_commands = Blueprint('db', __name__)

@db_commands.cli.command("create")
def db_create():
    db.drop_all()
    db.create_all()
    print("Created tables")

@db_commands.cli.command("seed")
def db_seed():
    locations = [
        Location(
            name="Melbourne",
            description="Cultural hub with diverse architecture, culinary delights, and vibrant atmosphere.",
        ),
        Location(
            name="Geelong",
            description="Coastal city near Melbourne, known for waterfront, gardens, and industry.",
        ),
        Location(
            name="Ballarat",
            description="Historic gold rush city with architecture, gardens, and cultural attractions.",
        )
    ]

    db.session.add_all(locations)

    restaurants = [
        Restaurant(
            cuisine="maccas",
            price="expensive",
            rating="good",
            location_id=1
        ),
        Restaurant(
            cuisine="KFC",
            price="Fair",
            rating="good",
            location_id=2
        )
    ]

    db.session.add_all(restaurants)

    users = [
        User(
            name="Tim1",
            email="admin1@gmail.com",
            password=bcrypt.generate_password_hash("12345678910").decode("utf8"),
            is_admin=True
        ),
        User(
            name="Tim2",
            email="user1@gmail.com",
            password=bcrypt.generate_password_hash("12345678910").decode("utf8"),
        ),
        User(
            name="Tim3",
            email="user2@gmail.com",
            password=bcrypt.generate_password_hash("12345678910").decode("utf8"),
        )
    ]

    db.session.add_all(users)

    daily_plans = [
        DailyPlan(
            restaurant="Maccas",
            hotel="Crown",
            attraction="Melbourne Zoo",
            user_id=2
        ),
        DailyPlan(
            restaurant="KFC",
            hotel="HolidayInn",
            attraction="Melbourne Museum",
            user_id=2
        ),
        DailyPlan(
            restaurant="Subway",
            hotel="Hilton",
            attraction="Melbourne Aquarium",
            user_id=2
        )
    ]

    db.session.add_all(daily_plans)
    db.session.commit()