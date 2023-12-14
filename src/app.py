from setup import app
from blueprints.cli_bp import db_commands
from blueprints.users_bp import users_bp
from blueprints.attractions_bp import attractions_bp
from blueprints.daily_plans_bp import daily_plans_bp
from blueprints.hotels_bp import hotels_bp
from blueprints.locations_bp import locations_bp
from blueprints.restaurants_bp import restaurants_bp

app.register_blueprint(db_commands)
app.register_blueprint(users_bp)
app.register_blueprint(attractions_bp)
app.register_blueprint(daily_plans_bp)
app.register_blueprint(hotels_bp)
app.register_blueprint(locations_bp)
app.register_blueprint(restaurants_bp)

print(app.url_map)
