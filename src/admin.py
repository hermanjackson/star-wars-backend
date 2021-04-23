import os
from flask_admin import Admin
from models import db, User
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')


    Base = declarative_base()
favorites = Table('favorite', Base.metadata,
    db.Column('user_id', Integer, ForeignKey('user.id')),
    db.Column('people_id', Integer, ForeignKey('people.id')),
    db.Column('vehicle_id', Integer, ForeignKey('vehicle.id'))
)


class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(250), nullable=False)
    email = db.Column(String(250), nullable=False)
    password = db.Column(String(250), nullable=False)
    username = db.Column(String(250), nullable=False)
    favorite_people = relationship("People",
                    secondary=favorites)
    favorite_vehicles = relationship("Vehicles",
                    secondary=favorites)
    


class People(Base):
    __tablename__ = 'peolple'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(250))
    height = db.Column(String(250))
    eyecolor = db.Column(String(250), nullable=False)
    weight = db.Column(Integer, ForeignKey('person.id'))
    



    def to_dict(self):
        return {}
class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(250), nullable=False)
    model = db.Column(String(250), nullable=False)
    



    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))