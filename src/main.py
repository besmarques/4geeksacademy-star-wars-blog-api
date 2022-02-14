"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Vehicles, Planets, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)



@app.route('/users', methods=['GET'])
def get_all_users():
    
    users = User.get_all_users()
    serialized_users = []
    for user in users:
        serialized_users.append(user.serialize())

    return(jsonify(serialized_users))

@app.route('/users/<int:id>', methods=['GET'])
def get_users_by_id(id):
    
    user = User.get_users_by_id(id)
    
    return(jsonify(user.serialize()))


@app.route('/vehicles', methods=['GET'])
def get_all_vehicles():
    
    vehicles = Vehicles.get_all_vehicles()
    serialized_vehicles = []
    for vehicle in vehicles:
        serialized_vehicles.append(vehicle.serialize())

    return(jsonify(serialized_vehicles))


@app.route('/vehicles/<int:id>', methods=['GET'])
def get_vehicles_by_id(id):
    
    vehicle = Vehicles.get_vehicles_by_id(id)
    
    return(jsonify(vehicle.serialize()))



@app.route('/planets', methods=['GET'])
def get_all_planets():
    
    planets = Planets.get_all_planets()
    serialized_planets = []
    for planet in planets:
        serialized_planets.append(planet.serialize())

    return(jsonify(serialized_planets))


@app.route('/planets/<int:id>', methods=['GET'])
def get_planets_by_id(id):
    
    planet = Planets.get_planets_by_id(id)
    
    return(jsonify(planet.serialize()))


@app.route('/characters', methods=['GET'])
def get_all_chars():
    
    characters = Character.get_all_chars()
    serialized_characters = []
    for character in characters:
        serialized_characters.append(character.serialize())

    return(jsonify(serialized_characters))


@app.route('/characters/<int:id>', methods=['GET'])
def get_character_by_id(id):
    
    character = Character.get_chars_by_id(id)
    
    return(jsonify(character.serialize()))

#Get favorites using user ID| Check if this is the right logic
@app.route('/users/favorites/<int:user_id>', methods=['GET'])
def get_favorites_by_user_id(user_id):
    
    favorite = Favorites.get_favorites_by_user_id(user_id)
    
    return(jsonify(favorite.serialize()))


@app.route('/favorites', methods=['GET'])
def get_all_favorites():
    
    favorites = Favorites.get_all_favorites()
    serialized_favorites = []
    for favorite in favorites:
        serialized_favorites.append(favorite.serialize())

    return(jsonify(serialized_favorites))


@app.route('/favorites/<int:id>', methods=['GET'])
def get_favorites_by_id(id):
    
    favorite = Favorites.get_favorites_by_id(id)
    
    return(jsonify(favorite.serialize()))





@app.route('/favorites', methods=['POST'])
def create_favorite():
    
    favorite = Favorites(
        id = 0,
        #character_post_id = 1,
        #user_id = 1
    )

    favorite.create()






# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
