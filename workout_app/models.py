from workout_app import db
from sqlalchemy_utils import URLType
from flask_login import UserMixin

class Exercise(db.Model):
    """Exercise Model"""
    #Import data from Exercise Form as to which category & body part worked
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    bodyPart = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    routines = db.relationship('Routine', secondary='routine_exercise', back_populates='exercises')


    def __repr__(self):
        return self.name
    #If I want pounds and reps to be contingent on the type of category, make nullable set to true.
    #I want to hide certain form fields (FrontEnd work)
    #If i want to reject information on back end i could use a validator to reject form based on category.

routine_exercise = db.Table('routine_exercise',
    db.Column('exercise_id', db.Integer, db.ForeignKey('exercise.id')),
    db.Column('routine_id', db.Integer, db.ForeignKey('routine.id'))
)


class Routine(db.Model):
    """Routine Model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    exercises = db.relationship('Exercise', secondary='routine_exercise', back_populates='routines')


    def __repr__(self):
        return self.name
    #How do I set up a many to many exercise routine


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<User: {self.username}>'