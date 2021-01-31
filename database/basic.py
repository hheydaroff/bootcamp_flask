import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Get the absolute path of the current file
basedir = os.path.abspath(os.path.dirname(__file__))

# Create the flask app object
app = Flask(__name__)

# Define the Database path by joining sqlite host path with the current file's directory and database name
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# Disable the modifications tracking as it is not needed to be seen
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  False

# Define the database object
db = SQLAlchemy(app)

# add on migration capabilities
migrate= Migrate(app, db)
################################
# Define the Puppy class with database model inherited
class Puppy(db.Model):

    #manual table name choice
    __tablename__ = 'puppies'

    # Define an id column with integer unique identifier
    id = db.Column(db.Integer, primary_key = True)
    # Define name column
    name = db.Column(db.Text)
    # Define integer age column
    age = db.Column(db.Integer)

    # Define breed
    breed = db.Column(db.Text)


    # Def Main Model with variables
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self):
        return f"Puppy {self.name} is {self.age} year/s old"
