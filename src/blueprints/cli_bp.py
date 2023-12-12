from flask import Blueprint
from setup import db, bcrypt
from models.daily_plan import DailyPlan
from models.user import User
from datetime import date

db_commands = Blueprint('db', __name__)

@db_commands.cli.command("create")
def db_create():
    db.drop_all()
    db.create_all()
    print("Created tables")


@db_commands.cli.command("seed")
def db_seed():
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
            attractions="Melbourne Zoo",
            user_id=2
        ),
        DailyPlan(
            restaurant="KFC",
            hotel="HolidayInn",
            attractions="Melbourne Museum",
            user_id=2
        ),
        DailyPlan(
            restaurant="Subway",
            hotel="Hilton",
            attractions="Melbourne Aquarium",
            user_id=2
        )
    ]

    db.session.add_all(daily_plans)
    db.session.commit()