from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

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


#class Favorites(db.Model):
#    __tablename__ = 'favorites'
#    id = db.Column (db.Integer, unique=True, primary_key=True)
#    character_post_id = db.Column (db.Integer, ForeignKey('characters.id'))
#    characters = relationship(Character)
#    vehicles_post_id = db.Column (db.Integer, ForeignKey('vehicles.id'))
#    vehicles = relationship(Vehicles)
#    planets_post_id = db.Column (db.Integer, ForeignKey('planets.id'))
#    planets = relationship(Planets)
#    user_id = db.Column (db.Integer, ForeignKey('user.id'))
#    user = relationship(User)