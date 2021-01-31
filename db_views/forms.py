from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    owner = StringField('Name of the Owner: ')
    name = StringField('Name of Puppy: ')
    submit = SubmitField('Add Puppy')


class AddOwnerForm(FlaskForm):
    name = StringField('Name of Owner: ')
    pup_id = IntegerField("Id of Puppy: ")
    submit = SubmitField("Add Owner")

class DelForm(FlaskForm):

    id = IntegerField('ID Number of Puppy to Remove: ')


    submit = SubmitField('Remove Puppy')