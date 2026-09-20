from flask_sqlalchemy import SQLAlchemy
from datetime import date,datetime

db = SQLAlchemy()


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(100), unique=True, nullable=False)

    password = db.Column(db.String(200), nullable=False)

    age = db.Column(db.Integer)

    gender = db.Column(db.String(10))

    height = db.Column(db.Float)

    weight = db.Column(db.Float)

    goal = db.Column(db.String(50))
    activities = db.relationship("Activity", backref="user", lazy=True)


class WaterIntake(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    amount = db.Column(
        db.Integer,
        default=0
    )

    last_updated = db.Column(
        db.Date,
        default=date.today
    )

class WaterHistory(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    amount = db.Column(db.Integer, nullable=False)

    created_at = db.Column(
        db.DateTime,
        default=datetime.now
    )

class WorkoutSession(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    exercise = db.Column(db.String(100))

    reps = db.Column(db.Integer)

    calories = db.Column(db.Float)

    accuracy = db.Column(db.Integer)

    duration = db.Column(db.String(20))

    created_at = db.Column(
        db.DateTime,
        default=datetime.now
    )


class WorkoutProgress(db.Model):
    
    __tablename__ = "workout_progress"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    workout_day = db.Column(db.String(20), nullable=False)

    completed = db.Column(db.Boolean, default=False)

    completed_at = db.Column(db.DateTime)

class Activity(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    title = db.Column(db.String(100), nullable=False)

    description = db.Column(db.String(200))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Workout(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    exercise = db.Column(db.String(100))

    reps = db.Column(db.Integer)

    calories = db.Column(db.Float)

    accuracy = db.Column(db.Float)

    duration = db.Column(db.String(20))

    date = db.Column(db.String(30))    

class FoodLog(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )
    meal = db.Column(
    db.String(20),
    nullable=False,
    default="Breakfast"
)

    food_name = db.Column(db.String(100), nullable=False)

    quantity = db.Column(db.Float, nullable=False)

    calories = db.Column(db.Float, nullable=False)

    protein = db.Column(db.Float, nullable=False)

    carbs = db.Column(db.Float, nullable=False)

    fat = db.Column(db.Float, nullable=False)

    from datetime import datetime

    created_at = db.Column(
        db.DateTime,
        default=lambda:datetime.now()
    )    
    