from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    #def __repr__(self):
    #    return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
    @classmethod
    def get_all_users(cls):
        users = cls.query.all()
        return users

    @classmethod
    def get_users_by_id(cls, id):
        users_by_id = cls.query.filter_by(id = id).one_or_none()
        return users_by_id

class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column (db.Integer, unique=True, primary_key=True)
    image = db.Column (db.String(250), unique=False, nullable=False)
    name = db.Column (db.String(250), unique=False, nullable=False)
    model = db.Column (db.String(250), unique=False, nullable=False)
    manufacturer = db.Column (db.String(250), unique=False, nullable=False)
    vehicle_class = db.Column (db.String(250), unique=False, nullable=False)
    cost = db.Column (db.Integer, unique=False, nullable=False)
    speed = db.Column (db.Integer, unique=False, nullable=False)
    length = db.Column (db.Integer, unique=False, nullable=False)
    cargo_capacity = db.Column (db.String(250), unique=False, nullable=False)
    crew = db.Column (db.Integer, unique=False, nullable=False)
    passengers = db.Column (db.Integer, unique=False, nullable=False)
    consumables = db.Column (db.Integer, unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "image": self.image,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "vehicle_class": self.vehicle_class,
            "cost": self.cost,
            "speed": self.speed,
            "length": self.length,
            "cargo_capacity": self.cargo_capacity,
            "crew": self.crew,
            "passengers": self.passengers,
            "consumables": self.consumables
        }

    #@classmethod
    #def create(self):
    #    db.session.add(self)
    #    db.session.commit()

    @classmethod
    def get_all_vehicles(cls):
        vehicles = cls.query.all()
        return vehicles

    @classmethod
    def get_vehicles_by_id(cls, id):
        vehicles_by_id = cls.query.filter_by(id = id).one_or_none()
        return vehicles_by_id


class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column (db.Integer, unique=True, primary_key=True)
    image = db.Column (db.String(250), unique=False, nullable=False)
    name = db.Column (db.String(250), unique=False, nullable=False)
    diameter = db.Column (db.String(250), unique=False, nullable=False)
    rotation = db.Column (db.String(250), unique=False, nullable=False)
    orbital_period = db.Column (db.String(250), unique=False, nullable=False)
    gravity = db.Column (db.String(250), unique=False, nullable=False)
    population = db.Column (db.Integer, unique=False, nullable=False)
    climate = db.Column (db.String(250), unique=False, nullable=False)
    terrain = db.Column (db.String(250), unique=False, nullable=False)
    surface_water = db.Column (db.Integer, unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "image": self.image,
            "name": self.name,
            "diameter": self.diameter,
            "rotation": self.rotation,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
        }

    @classmethod
    def get_all_planets(cls):
        planets = cls.query.all()
        return planets

    @classmethod
    def get_planets_by_id(cls, id):
        planets_by_id = cls.query.filter_by(id = id).one_or_none()
        return planets_by_id


class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column (db.Integer, unique=True, primary_key=True)
    image = db.Column (db.String(250), unique=False, nullable=False)
    name = db.Column (db.String(250), unique=False, nullable=False)
    birth_year = db.Column (db.String(250), unique=False, nullable=False)
    height = db.Column (db.Integer, unique=False, nullable=False)
    weight = db.Column (db.Integer, unique=False, nullable=False)
    gender = db.Column (db.String(250), unique=False, nullable=False)
    hair_color = db.Column (db.String(250), unique=False, nullable=False)
    eye_color = db.Column (db.String(250), unique=False, nullable=False)
    skin_color = db.Column (db.String(250), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "image": self.image,
            "name": self.name,
            "birth_year": self.birth_year,
            "height": self.height,
            "weight": self.weight,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "skin_color": self.skin_color
        }

    @classmethod
    def get_all_chars(cls):
        characters = cls.query.all()
        return characters

    @classmethod
    def get_chars_by_id(cls, id):
        character_by_id = cls.query.filter_by(id = id).one_or_none()
        return character_by_id


class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column (db.Integer, unique=True, primary_key=True)
    character_post_id = db.Column (db.Integer, db.ForeignKey('characters.id'))
    characters = db.relationship(Character)
    vehicles_post_id = db.Column (db.Integer, db.ForeignKey('vehicles.id'))
    vehicles = db.relationship(Vehicles)
    planets_post_id = db.Column (db.Integer, db.ForeignKey('planets.id'))
    planets = db.relationship(Planets)
    user_id = db.Column (db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)

    def serialize(self):
        return {
            "id": self.id,
            "character_post_id": self.character_post_id,
            "vehicles_post_id": self.vehicles_post_id,
            "planets_post_id": self.planets_post_id,
            "user_id": self.user_id
        }
    
    def create(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all_favorites(cls):
        favorites = cls.query.all()
        return favorites

    @classmethod
    def get_favorites_by_id(cls, id):
        favorite_by_id = cls.query.filter_by(id = id).one_or_none()
        return favorite_by_id
    
    @classmethod
    def get_favorites_by_user_id(cls, user_id):
        favorite_by_user_id = cls.query.filter_by(user_id = user_id).one_or_none()
        return favorite_by_user_id