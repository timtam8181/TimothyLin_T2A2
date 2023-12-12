from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

# set the database URI via SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://db_dev:123456@localhost:5000/travel_plan_db"

# create the database object
db = SQLAlchemy(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"