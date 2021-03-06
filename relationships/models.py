import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.dirname(os.path.dirname(__name__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


class Puppy(db.Model):

    __tablename__ = 'puppies'

    id=db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    #One-2-Many relationship. Puppy to many toys.
    toys = db.relationship('Toy', backref = 'puppy', lazy = 'dynamic')

    #one-2-one one puppy to one owner
    owner = db.relationship('Owner', backref = 'puppy', uselist = False)


    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Puppy name is {self.name} and owner is {self.owner.name}."
        else:
            return f"Puppy name is {self.name} and has no owner yet."

    def report_toys(self):
        print("Here are my toys:")
        for toy in self.toys:
            print(toy.item_name)

class Toy(db.Model):
    __tabename__ = 'toys'

    id = db.Column(db.Integer, primary_key = True)
    item_name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, item_name, puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id


class Owner(db.Model):
    __table__bame = 'owners'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)

    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))


    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id