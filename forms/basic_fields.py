from flask import Flask, render_template, request, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
 RadioField, SelectField, TextField,
 TextAreaField, SubmitField)

from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'


class InfoForm(FlaskForm):


    breed = StringField("What Breed are you?", validators = [DataRequired()])

    neutered = BooleanField("Have you been neuetered?")

    mood = RadioField("Please choose your mood: ", choices = [('mood_one', 'happy'), ('mood_two', 'excited')])

    food_choice = SelectField( "Pick your Favorite Food: ", choices = [('chi', 'Chicken'), ('bf', "Beef"), ('fish', 'fish')])

    feedback = TextAreaField()

    submit = SubmitField('Submit')

@app.route('/', methods = ['POST', 'GET'])
def index():

    form = InfoForm()

    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data


        return redirect(url_for('thankyou'))

    return render_template('index_fields.html', form = form)


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou_field.html')


if __name__ == '__main__':
    app.run(debug = True)