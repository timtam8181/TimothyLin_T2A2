from flask import Blueprint, request
from models.user import User, UserSchema
from setup import bcrypt, db
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token
from datetime import timedelta

users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.route("/register", methods=["POST"])
def register():
    try:
        user_info = UserSchema(exclude=["id", "is_admin"]).load(request.json)
        user = User(
            email=user_info["email"],
            password=bcrypt.generate_password_hash(user_info["password"]).decode(
                "utf8"
            ),
            name=user_info["name"]
        )

        db.session.add(user)
        db.session.commit()


        return UserSchema(exclude=["password"]).dump(user), 201
    except IntegrityError:
        return {"error": "That email has been used. Try again!"}, 409
    
@users_bp.route("/login", methods=["POST"])
def login():
    user_info = UserSchema(exclude=["id", "name", "is_admin"]).load(request.json)
    stmt = db.select(User).where(User.email == user_info["email"])
    user = db.session.scalar(stmt)
    if user and bcrypt.check_password_hash(user.password, user_info["password"]):
        token = create_access_token(identity=user.id, expires_delta=timedelta(hours=10))
        return {
            "token": token,
            "user": UserSchema(exclude=["password", "is_admin"]).dump(user),
        }
    else:
        return {"error": "Try again. Incorrect email or password."}, 401