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
from models import db, User, Character, Vehicles, Planets
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

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200


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
        serialized_planets.append(vehicle.serialize())

    return(jsonify(serialized_planets))


@app.route('/planets/<int:id>', methods=['GET'])
def get_planets_by_id(id):
    
    planet = planets.get_planets_by_id(id)
    
    return(jsonify(vehicle.serialize()))


@app.route('/character', methods=['GET'])
def get_all_chars():
    
    characters = Character.get_all_chars()
    serialized_characters = []
    for character in characters:
        serialized_characters.append(character.serialize())

    return(jsonify(serialized_characters))


@app.route('/character/<int:id>', methods=['GET'])
def get_character_by_id(id):
    
    character = Character.get_chars_by_id(id)
    
    return(jsonify(character.serialize()))





# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
