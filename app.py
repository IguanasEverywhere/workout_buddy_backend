import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

from sqlalchemy.sql import func

from LLM_Call import call_groq

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(6))

    workouts = db.relationship('Workout', back_populates='user', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            "id": self.id,
            "username":self.username,
            "gender":self.gender
        }

class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.String(50), nullable=False)
    weight = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime(timezone=True), server_default=func.now())
    notes = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', back_populates='workouts')

    def to_dict(self):
        return {
            "id": self.id,
            "exercise_name": self.exercise_name,
            "weight": self.weight,
            "reps": self.reps,
            "notes": self.notes,
            "timestamp": self.timestamp,
            "user_id": self.user_id
        }

class Workout_Data:
    def __init__(self, exercises, AI_feedback):
        self.exercises = exercises
        self.AI_feedback = AI_feedback


@app.route('/data/<user_id>', methods=('GET', 'POST'))
def user_workout_data(user_id):
    if request.method == 'GET':
        workouts_resp = Workout.query.filter(Workout.user_id==user_id).all()
        user_workouts = [workout.to_dict() for workout in workouts_resp]
        return user_workouts

@app.route('/next-workout/<user_id>', methods=('GET', 'POST)'))
def next_workout_suggestion(user_id):
     if request.method == 'GET':
        recent_workouts_resp = Workout.query.filter(Workout.user_id==user_id).limit(2).all()
        recent_workouts = [workout.to_dict() for workout in recent_workouts_resp]
        workouts_obj = Workout_Data(recent_workouts, '')
        call_groq(workouts_obj)
        return {"workout_advice": workouts_obj.AI_feedback}





if __name__ == '__main__':
        app.run(port=5555)


