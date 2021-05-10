from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL


class ExerciseForm(FlaskForm):
    """Form for adding a new exercise"""
    #Exercise name
    name = StringField('Name', validators=[DataRequired()])
    #Body part worked
    bodyPart = SelectField('Type', choices=[('Core','Arms','Back','Chest','Legs','Shoulders','Other','Full Body', 'Cardio')])
    #Type of exercise
    category = SelectField('Category', choices=[('Barbell','Dumbbell','Machine/Other','Weighted Bodyweight','Assisted Bodyweight','Reps Only','Cardio','Duration')])

class RoutineForm(FlaskForm):
    """Form for adding a new routine"""
    #Routine Name
    name = StringField('Name', validators=[DataRequired()])
    #TODO: I want the choices to be a list of the pre-existing workouts already stored in the datavse.
    exercise = SelectField('Exercise 1', choices)
    #List of Exercises One to Many or Many to Many
    #Book & Genre exercise will help!