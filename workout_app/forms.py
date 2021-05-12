from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, URL
from workout_app import db
from workout_app.models import Exercise, Routine


class ExerciseForm(FlaskForm):
    """Form for adding a new exercise"""
    #Exercise name
    name = StringField('Name', validators=[DataRequired()])
    #Body part worked
    bodyPart = SelectField('Body Part', choices=[('Core','Core'),('Arms','Arms'),('Back','Back'),('Chest','Chest'),('Legs','Legs'),('Shoulders','Shoulders'),('Other','Other'),('Olympic','Olypmic'),('Full Body','Full Body'),('Cardio','Cardio')])
    #Type of exercise
    category = SelectField('Category', choices=[('Barbell','Barbell'),('Dumbbell','Dumbell'),('Machine/Other','Machine/Other'),('Weighted Bodyweight','Weighted Bodyweight'),('Assisted Bodyweight','Assisted Bodyweight'),('Reps Only','Reps Only'),('Cardio','Cardio'),('Duration','Duration')])
    submit = SubmitField('Submit')

#Access the data held within Exercise form import it
#Make sure form labels match models

class RoutineForm(FlaskForm):
    """Form for adding a new routine"""
    #Routine Name
    name = StringField('Name', validators=[DataRequired()])
    #TODO: I want the choices to be a list of the pre-existing workouts already stored in the datavse.
    exercise = QuerySelectMultipleField('Exercise',
        query_factory=lambda: Exercise.query)
    submit = SubmitField('Submit')
    #List of Exercises One to Many or Many to Many
    #Book & Genre exercise will help!