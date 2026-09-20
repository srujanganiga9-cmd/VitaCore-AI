from datetime import date,datetime
from utils.chatbot_ai import ask_fitness_ai
from utils.diet_ai import generate_diet_plan
from flask import Flask, render_template, request, redirect, url_for, flash, session,jsonify
from flask_bcrypt import Bcrypt

from models import db, User, WaterIntake, WorkoutProgress,Activity,WaterHistory,WorkoutSession,Workout,FoodLog
from utils.bmi import calculate_bmi
from utils.calorie import calculate_calories, calculate_protein
from utils.workout import get_workout_plan
from flask import Response
import cv2
from utils.pose_detector import PoseDetector
from utils.squat_counter import SquatCounter
from utils.shoulder_press_counter import ShoulderPressCounter
from utils.arm_raise_counter import ArmRaiseCounter
from utils.jumping_counter import JumpingCounter
from flask import send_file
import tempfile

from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch


from utils.nutrition_search import search_food, get_food

app = Flask(__name__)

app.config["SECRET_KEY"] = "fitai_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
bcrypt = Bcrypt(app)

# ---------------- CAMERA ---------------- #

camera = cv2.VideoCapture(0)
camera_running = True
detector = PoseDetector()
squat_counter = SquatCounter()
shoulder_counter = ShoulderPressCounter()
arm_counter = ArmRaiseCounter()
jumping_counter = JumpingCounter()
# Current selected exercise
selected_exercise = "Squat"
# Live exercise statistics
exercise_stats = {

    "reps": 0,

    "accuracy": 0,

    "calories": 0,

    "status": "Waiting for camera...",

    "tips": [

        "Stand in front of the camera.",

        "Make sure your full body is visible."

    ]

}

# Create database tables
with app.app_context():
    db.create_all()


# ---------------- HOME ---------------- #

@app.route("/")
def home():
    return redirect(url_for("login"))


# ---------------- REGISTER ---------------- #

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        age = int(request.form["age"])
        gender = request.form["gender"]
        height = float(request.form["height"])
        weight = float(request.form["weight"])
        goal = request.form["goal"]

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash("Email already exists!")
            return redirect(url_for("register"))

        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        new_user = User(
            name=name,
            email=email,
            password=hashed_password,
            age=age,
            gender=gender,
            height=height,
            weight=weight,
            goal=goal
        )

        db.session.add(new_user)
        db.session.commit()

        # Create Water Intake Record
        water = WaterIntake(
            user_id=new_user.id,
            amount=0
        )

        db.session.add(water)
        db.session.commit()

        flash("Registration Successful! Please Login.")
        return redirect(url_for("login"))

    return render_template("register.html")


# ---------------- LOGIN ---------------- #

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):

            session["user_id"] = user.id

            return redirect(url_for("dashboard"))

        flash("Invalid Email or Password")

    return render_template("login.html")


@app.route("/forgot_password", methods=["GET", "POST"])
def forgot_password():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        # Check if email exists
        user = User.query.filter_by(email=email).first()

        if not user:

            flash("Email not found.")
            return redirect(url_for("forgot_password"))

        # Check passwords
        if password != confirm_password:

            flash("Passwords do not match.")
            return redirect(url_for("forgot_password"))

        # Update password
        user.password = bcrypt.generate_password_hash(password).decode("utf-8")

        db.session.commit()

        flash("Password updated successfully. Please login.")

        return redirect(url_for("login"))

    return render_template("forgot_password.html")


# ---------------- DASHBOARD ---------------- #

@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("login"))

    user = User.query.get(session["user_id"])

    bmi = calculate_bmi(user.weight, user.height)

    calories = calculate_calories(
        user.age,
        user.gender,
        user.height,
        user.weight
    )

    protein = calculate_protein(
        user.weight,
        user.goal
    )
    # ===========================
    # Today's Nutrition Progress
    # ===========================

    today_foods = FoodLog.query.filter(

         FoodLog.user_id == user.id,
         db.func.date(FoodLog.created_at) == date.today()
    ).all()
    

    total_calories = sum(food.calories for food in today_foods)
    total_protein = sum(food.protein for food in today_foods)


    calorie_goal = calories
    protein_goal = protein

    # Values shown on the dashboard (stop increasing after goal is reached)
    display_calories = min(total_calories, calorie_goal)
    display_protein = min(total_protein, protein_goal)

    calorie_progress = int((total_calories / calorie_goal) * 100) if calorie_goal else 0
    protein_progress = int((total_protein / protein_goal) * 100) if protein_goal else 0

    calorie_progress = min(calorie_progress, 100)
    protein_progress = min(protein_progress, 100)

    calorie_completed = total_calories >= calorie_goal
    protein_completed = total_protein >= protein_goal

    remaining_calories = max(0, calorie_goal - total_calories)
    remaining_protein = max(0, protein_goal - total_protein)

    extra_calories = max(0, total_calories - calorie_goal)
    extra_protein = max(0, total_protein - protein_goal)
     # ---------------------------------
    # Daily Water Requirement
    # ---------------------------------

    daily_water_goal = user.weight * 35

    # Adjust based on user's goal
    if user.goal == "Muscle Gain":
        daily_water_goal += 300

    elif user.goal == "Weight Loss":
        daily_water_goal += 200

    # Optional adjustment based on age
    if user.age and user.age >= 50:
        daily_water_goal += 100

    daily_water_goal = round(daily_water_goal)

    # Water Tracker
    water = WaterIntake.query.filter_by(user_id=user.id).first()

    if water is None:


        water = WaterIntake(

            user_id=user.id,
            amount=0,
            last_updated=date.today()
        )

        db.session.add(water)
        db.session.commit()

    # ===============================
    # Automatic Daily Reset
    # ===============================

    if water.last_updated != date.today():


        water.amount = 0

        water.last_updated = date.today()

        db.session.commit()

# ===============================

    progress = round((water.amount / daily_water_goal) * 100)

    if progress > 100:
        progress = 100

    # ===========================
    # Weekly Workout Progress
     # ===========================

    

    completed_workouts = WorkoutProgress.query.filter_by(
         user_id=user.id,
         completed=True
     ).all()

    completed_days = [w.workout_day for w in completed_workouts]

    completed_count = len(completed_days)

    weekly_progress = int((completed_count / 7) * 100)

    


    # ===========================
    # Today's Water History
    # ===========================
    water_history = WaterHistory.query.filter(

         WaterHistory.user_id == user.id,
         db.func.date(WaterHistory.created_at) == date.today()
     ).order_by(
         WaterHistory.created_at.desc()
     ).all()

     

       

    # ===========================
    # Recent Activities
    # ===========================

    activities = Activity.query.filter_by(
        user_id=user.id
    ).order_by(
        Activity.created_at.desc()
    ).limit(10).all()

    return render_template (
        "dashboard.html",
        user=user,
        bmi=bmi,
        calories=calories,
        protein=protein,
        water=water.amount,
        daily_water_goal=daily_water_goal,
        progress=progress,

        completed_days=completed_days,
        completed_count=completed_count,
        weekly_progress=weekly_progress,
        water_history=water_history,

        activities=activities,
        total_calories=round(total_calories, 1),
        total_protein=round(total_protein, 1),

        calorie_goal=round(calorie_goal, 1),
        protein_goal=round(protein_goal, 1),

        calorie_progress=calorie_progress,
        protein_progress=protein_progress,

        calorie_completed=calorie_completed,
        protein_completed=protein_completed,

        remaining_calories=round(remaining_calories, 1),
        remaining_protein=round(remaining_protein, 1),
        display_calories=round(display_calories, 1),
        display_protein=round(display_protein, 1),
        extra_calories=round(extra_calories, 1),
        extra_protein=round(extra_protein, 1)
    )

@app.route("/water_tracker")
def water_tracker():

    if "user_id" not in session:
        return redirect(url_for("login"))

    user = User.query.get(session["user_id"])

    # ===========================
    # Daily Water Requirement
    # ===========================

    daily_water_goal = user.weight * 35

    if user.goal == "Muscle Gain":
        daily_water_goal += 300

    elif user.goal == "Weight Loss":
        daily_water_goal += 200

    if user.age and user.age >= 50:
        daily_water_goal += 100

    daily_water_goal = round(daily_water_goal)

    # ===========================
    # Current Water Intake
    # ===========================

    water = WaterIntake.query.filter_by(
        user_id=user.id
    ).first()

    if water is None:

        water = WaterIntake(
            user_id=user.id,
            amount=0
        )

        db.session.add(water)
        db.session.commit()

    progress = round((water.amount / daily_water_goal) * 100)

    if progress > 100:
        progress = 100

    # ===========================
    # Today's Water History
    # ===========================

    water_history = WaterHistory.query.filter(

        WaterHistory.user_id == user.id,
        db.func.date(WaterHistory.created_at) == date.today()

    ).order_by(

        WaterHistory.created_at.desc()

    ).all()

    return render_template(

        "water_tracker.html",

        user=user,

        water=water.amount,

        daily_water_goal=daily_water_goal,

        progress=progress,

        water_history=water_history

    )

@app.route("/nutrition")
def nutrition():

    return render_template("nutrition.html")


@app.route("/search_food")
def search_food_route():

    query = request.args.get("q", "")

    return jsonify(search_food(query))

@app.route("/food_details")
def food_details():

    food = request.args.get("food", "")

    return jsonify(get_food(food))

@app.route("/add_food", methods=["POST"])
def add_food():

    data = request.get_json()

    # Replace this with your actual logged-in user's ID later
    if "user_id" not in session:
        return {
        "success": False,
        "message": "User not logged in"
    }, 401

    user_id = session["user_id"]

    food = FoodLog(
        user_id=user_id,
        food_name=data["food_name"],
        meal=data["meal"],
        quantity=data["quantity"],
        calories=data["calories"],
        protein=data["protein"],
        carbs=data["carbs"],
        fat=data["fat"]
    )

    db.session.add(food)
    db.session.commit()
    print("Food saved successfully!")

    all_foods = FoodLog.query.all()

    print("Total foods in database:", len(all_foods))

    for food in all_foods:

         print(food.id, food.food_name, food.user_id)

    return {
        "success": True,
        "message": "Food added successfully!"
    }

from collections import defaultdict
@app.route("/today_intake")
def today_intake():



    user_id = session["user_id"]
   


    foods = FoodLog.query.filter_by(user_id=user_id).all()

    grouped = defaultdict(list)

    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fat = 0

    for food in foods:

        grouped[food.meal].append(food)

        total_calories += food.calories
        total_protein += food.protein
        total_carbs += food.carbs
        total_fat += food.fat


        

    return render_template(

        "today_intake.html",

        grouped=grouped,

        total_calories=total_calories,

        total_protein=total_protein,

        total_carbs=total_carbs,

        total_fat=total_fat

    )

@app.route("/delete_food/<int:food_id>", methods=["POST"])
def delete_food(food_id):

    food = FoodLog.query.get_or_404(food_id)

    db.session.delete(food)

    db.session.commit()

    return {
        "success": True
    }

# ---------------- WORKOUT ---------------- #
@app.route("/workout")
def workout():

    if "user_id" not in session:
        return redirect(url_for("login"))

    user = User.query.get(session["user_id"])

    workout_plan = get_workout_plan(user.goal)

    completed = WorkoutProgress.query.filter_by(
        user_id=user.id,
        completed=True
    ).all()

    completed_days = [w.workout_day for w in completed]

    return render_template(
        "workout.html",
        user=user,
        workout=workout_plan,
        completed_days=completed_days
    )

@app.route("/workout/<day>")
def workout_day(day):

    if "user_id" not in session:
        return redirect(url_for("login"))

    user = User.query.get(session["user_id"])

    workout_plan = get_workout_plan(user.goal)

    if day not in workout_plan:
        return redirect(url_for("workout"))

    workout = workout_plan[day]

    progress = WorkoutProgress.query.filter_by(
        user_id=user.id,
        workout_day=day
    ).first()

    completed = progress.completed if progress else False

    return render_template(
        "workout_day.html",
        user=user,
        day=day,
        title=workout["title"],
        exercises=workout["exercises"],
        completed=completed
    )

@app.route("/workout/complete/<day>")
def complete_workout_day(day):

    if "user_id" not in session:
        return redirect(url_for("login"))

    user = User.query.get(session["user_id"])

    progress = WorkoutProgress.query.filter_by(
        user_id=user.id,
        workout_day=day
    ).first()

    if progress:
        progress.completed = True
        progress.completed_at = datetime.now()
    else:
        progress = WorkoutProgress(
            user_id=user.id,
            workout_day=day,
            completed=True,
            completed_at=datetime.now()
        )

        db.session.add(progress)

    db.session.commit()

    flash(f"🎉 {day} Workout Completed Successfully!", "success")

    return redirect(url_for("workout"))
# ---------------- COMPLETE WORKOUT ---------------- #
@app.route("/complete_workout")
def complete_workout():

    if "user_id" not in session:
        return redirect(url_for("login"))

    today = date.today()

    workout = WorkoutProgress.query.filter_by(
        user_id=session["user_id"],
        workout_date=today
    ).first()

    if workout is None:

        workout = WorkoutProgress(
            user_id=session["user_id"],
            workout_date=today,
            completed=True
        )

        db.session.add(workout)

    else:

        workout.completed = True

    db.session.commit()

    flash("🎉 Workout Completed Successfully!")

    return redirect(url_for("dashboard"))


# ---------------- WATER TRACKER ---------------- #

@app.route("/add_water")
def add_water():

    if "user_id" not in session:
        return redirect(url_for("login"))

    user = User.query.get(session["user_id"])

    # Calculate today's water goal
    daily_water_goal = user.weight * 35

    if user.goal == "Muscle Gain":
        daily_water_goal += 300

    elif user.goal == "Weight Loss":
        daily_water_goal += 200

    if user.age and user.age >= 50:
        daily_water_goal += 100

    daily_water_goal = round(daily_water_goal)

    # Get water record
    water = WaterIntake.query.filter_by(
        user_id=user.id
    ).first()
    # ===============================
    # Automatic Daily Reset
    # ===============================

    if water.last_updated != date.today():


        water.amount = 0

        water.last_updated = date.today()

    if water:

        # Read amount from URL (default to 250 if missing)
        amount = request.args.get("amount", default=250, type=int)

        # Add only up to the goal
        previous_amount = water.amount
        water.amount = min(previous_amount + amount, daily_water_goal)

        # Save today's date whenever water is added
        water.last_updated = date.today()

        actual_added = water.amount - previous_amount
        # Save water history
        history = WaterHistory(

             user_id=user.id,
             amount=actual_added
        )

        db.session.add(history)

        # Save activity
        activity = Activity(
            user_id=user.id,
            title="Water Intake",
            description=f"Added {actual_added} ml water"
        )

        db.session.add(activity)
        db.session.commit()

    return redirect(url_for("water_tracker"))


@app.route("/reset_water")
def reset_water():

    if "user_id" not in session:
        return redirect(url_for("login"))

    user_id = session["user_id"]

    water = WaterIntake.query.filter_by(
        user_id=user_id
    ).first()

    if water:

        water.amount = 0

        # Update reset date
        water.last_updated = date.today()

    # Delete today's water history
    WaterHistory.query.filter_by(
        user_id=user_id
    ).delete()

    db.session.commit()

    return redirect(url_for("water_tracker"))


@app.route("/diet")
def diet():

    if "user_id" not in session:
        return redirect(url_for("login"))

    user = User.query.get(session["user_id"])

    diet_plan = generate_diet_plan(user)

    return render_template(
        "diet.html",
        user=user,
        diet_plan=diet_plan
    )


FITNESS_KEYWORDS = [
    "fitness", "gym", "workout", "exercise", "diet",
    "nutrition", "protein", "calories", "bmi",
    "weight", "muscle", "fat", "cardio",
    "strength", "health", "water", "supplement",
    "pushup", "push-up", "pullup", "pull-up",
    "squat", "deadlift", "bench press",
    "running", "walking", "jogging",
    "yoga", "stretch", "bodybuilding",
    "abs", "chest", "shoulder", "biceps",
    "triceps", "legs", "back","chest","chicken breast","egg","fish","whey protein","creatine",
    "omega 3"
]

@app.route("/chatbot", methods=["GET", "POST"])
def chatbot():

    if "user_id" not in session:
        return redirect(url_for("login"))

    # Get logged-in user
    user = User.query.get(session["user_id"])

    answer = ""

    if request.method == "POST":

       question = request.form["question"]


       # Check if the question is related to fitness
       if any(keyword in question.lower() for keyword in FITNESS_KEYWORDS):
            

             answer = ask_fitness_ai(question)

       else:
            


             answer = (
                 
                 
                " I'm your Fitness Coach.💪\n\n"
                "I can only answer fitness-related questions.\n\n"
                "Please ask me about workouts, diet, nutrition, "
                "muscle gain, weight loss, BMI, calories, or exercise."
             )

    return render_template(
        "chatbot.html",
        user=user,
        answer=answer
    )

# ---------------- LOGOUT ---------------- #

@app.route("/logout")
def logout():

    session.clear()

    flash("Logged out successfully!")

    return redirect(url_for("login"))


@app.route("/exercise")
def exercise():

    if "user_id" not in session:
        return redirect(url_for("login"))

    return render_template("exercise.html")

@app.route("/set_exercise/<exercise>")
def set_exercise(exercise):

    global selected_exercise
    global exercise_stats

    selected_exercise = exercise

    if exercise in ["Arm Raises", "Shoulder Press"]:

        exercise_stats = {
            "reps": 0,
            "accuracy": 0,
            "calories": 0,
            "status": "📷 Upper Body Not Visible",
            "tips": [
                "Stand in front of the camera.",
                "Keep your upper body visible."
            ]
        }

    else:

        exercise_stats = {
            "reps": 0,
            "accuracy": 0,
            "calories": 0,
            "status": "📷 Full Body Not Visible",
            "tips": [
                "Stand back until your full body is visible.",
                "Face the camera."
            ]
        }

    print("Selected Exercise:", selected_exercise)

    return "OK"

@app.route("/start_workout")
def start_workout():

    global squat_counter
    global shoulder_counter
    global arm_counter
    global jumping_counter

    squat_counter.started = True
    shoulder_counter.started = True
    arm_counter.started = True
    jumping_counter.started = True

    return "OK"

@app.route("/stop_workout")
def stop_workout():

    global squat_counter
    global shoulder_counter
    global arm_counter
    global jumping_counter

    squat_counter.started = False
    shoulder_counter.started = False
    arm_counter.started = False
    jumping_counter.started = False

    return "OK"

@app.route("/open_camera")
def open_camera():

    global camera
    global camera_running

    if not camera_running:

        camera = cv2.VideoCapture(0)
        camera_running = True

    return "OK"

@app.route("/close_camera")
def close_camera():

    global camera
    global camera_running

    if camera_running:

        camera.release()
        camera_running = False

    return "OK"



def upper_body_visible(landmarks):
    
    required = [0, 11, 12]  # Nose, Left Shoulder, Right Shoulder

    for idx in required:

        if landmarks[idx].visibility < 0.50:
            return False

    return True


def full_body_visible(landmarks):

    required = [0, 11, 12, 23, 24, 25, 26, 27, 28]

    for idx in required:

        if landmarks[idx].visibility < 0.50:
            return False

    return True



def generate_frames():
    
    global exercise_stats

    while True:

        success, frame = camera.read()

        if not success:
            break

        # Get frame and landmarks
        frame, landmarks = detector.find_pose(frame)

        # ---------------------------------
        # Person detected
        # ---------------------------------

        if landmarks:


            # ===============================
            # Upper Body Exercises
            # ===============================

            if selected_exercise in ["Arm Raises", "Shoulder Press"]:

                if not upper_body_visible(landmarks):

                    exercise_stats = {

                        "reps": 0,
                        "accuracy": 0,
                        "calories": 0,

                        "status": "📷 Upper Body Not Visible",

                        "tips": [

                            "Stand in front of the camera.",

                            "Keep your shoulders and face visible."

                        ]

                    }

                else:

                    if selected_exercise == "Arm Raises":

                        exercise_stats = arm_counter.process(landmarks)

                    else:

                        exercise_stats = shoulder_counter.process(landmarks)

            # ===============================
            # Full Body Exercises
            # ===============================

            else:

                if not full_body_visible(landmarks):

                    exercise_stats = {

                        "reps": 0,
                        "accuracy": 0,
                        "calories": 0,

                        "status": "📷 Full Body Not Visible",

                        "tips": [

                            "Move back from the camera.",

                            "Keep your full body visible."

                        ]

                    }

                else:

                    if selected_exercise == "Squat":

                        exercise_stats = squat_counter.process(landmarks)

                    else:

                        exercise_stats = jumping_counter.process(landmarks)

        # ---------------------------------
        # No person detected
        # ---------------------------------

        else:

            if selected_exercise in ["Arm Raises", "Shoulder Press"]:

                exercise_stats = {

                    "reps": 0,
                    "accuracy": 0,
                    "calories": 0,

                    "status": "📷 Upper Body Not Visible",

                    "tips": [

                        "Stand in front of the camera.",

                        "Keep your upper body visible."

                    ]

                }

            else:

                exercise_stats = {

                    "reps": 0,
                    "accuracy": 0,
                    "calories": 0,

                    "status": "📷 Full Body Not Visible",

                    "tips": [

                        "Move back from the camera.",

                        "Keep your full body visible."

                    ]

                }

        # Convert image to JPEG
        ret, buffer = cv2.imencode(".jpg", frame)

        frame = buffer.tobytes()

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' +
            frame +
            b'\r\n'
        )
# ---------------- CAMERA PAGE ---------------- #

@app.route("/camera")
def camera_page():

    if "user_id" not in session:
        return redirect(url_for("login"))

    return render_template("camera.html")


# ---------------- VIDEO FEED ---------------- #

@app.route("/video_feed")
def video_feed():

    return Response(
        generate_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )        
from flask import jsonify


@app.route("/exercise_stats")
def get_exercise_stats():

    global exercise_stats

    return jsonify(exercise_stats)


@app.route("/reset_exercise")
def reset_exercise():

    global exercise_stats
    global squat_counter
    global shoulder_counter
    global arm_counter
    global jumping_counter

    # Reset all counters
    squat_counter = SquatCounter()
    shoulder_counter = ShoulderPressCounter()
    arm_counter = ArmRaiseCounter()
    jumping_counter = JumpingCounter()

    exercise_stats = {
        "reps": 0,
        "accuracy": 0,
        "calories": 0,
        "status": "Waiting for camera..."
    }

    return "OK"

@app.route("/save_workout", methods=["POST"])
def save_workout():

    try:

        if "user_id" not in session:
            return jsonify({
                "success": False,
                "message": "User not logged in"
            })

        data = request.get_json()

        workout = Workout(

            user_id=session["user_id"],

            exercise=data["exercise"],

            reps=int(data["reps"]),

            calories=float(data["calories"]),

            accuracy=float(data["accuracy"]),

            duration=data["duration"],

            date=datetime.now().strftime("%d-%m-%Y")

        )

        db.session.add(workout)
        db.session.commit()

        return jsonify({"success": True})

    except Exception as e:

        db.session.rollback()

        print("❌ SAVE WORKOUT ERROR:", e)

        return jsonify({
            "success": False,
            "message": str(e)
        })



@app.route("/workout_history")
def workout_history():

    if "user_id" not in session:

        return redirect(url_for("login"))

    workouts = Workout.query.filter_by(

        user_id=session["user_id"]

    ).order_by(

        Workout.id.desc()

    ).all()

    return render_template(

        "workout_history.html",

        workouts=workouts

    )

# ---------------- DELETE WORKOUT ---------------- #

@app.route("/delete_workout/<int:id>")
def delete_workout(id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    workout = Workout.query.filter_by(
        id=id,
        user_id=session["user_id"]
    ).first()

    if workout:

        db.session.delete(workout)
        db.session.commit()
    flash("✅ Workout deleted successfully!", "success")
    return redirect(url_for("workout_history"))

@app.route("/download_workout_pdf/<int:id>")
def download_workout_pdf(id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    # ----------------------------
    # Fetch User & Workout
    # ----------------------------

    user = User.query.get_or_404(session["user_id"])

    workout = Workout.query.filter_by(
        id=id,
        user_id=session["user_id"]
    ).first_or_404()

    # ----------------------------
    # Create PDF
    # ----------------------------

    temp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    )

    doc = SimpleDocTemplate(
        temp.name,
        leftMargin=40,
        rightMargin=40,
        topMargin=35,
        bottomMargin=35
    )

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    title_style.alignment = TA_CENTER

    heading_style = styles["Heading2"]

    normal_style = styles["BodyText"]

    elements = []

    # =====================================
    # HEADER
    # =====================================

    elements.append(
        Paragraph(
            "<b>VitaCore AI</b>",
            title_style
        )
    )

    elements.append(
        Paragraph(
            "<b>PERSONAL FITNESS REPORT </b>",
            title_style
        )
    )

    elements.append(
        Spacer(1, 12)
    )

    elements.append(
        Paragraph(
            "=" * 95,
            normal_style
        )
    )

    elements.append(
        Spacer(1, 10)
    )

    # =====================================
    # REPORT INFORMATION
    # =====================================

    report_id = f"FAC-{datetime.now().strftime('%Y%m%d')}-{workout.id:04d}"

    elements.append(
        Paragraph(
            f"<b>Report ID</b> : {report_id}",
            normal_style
        )
    )

    elements.append(
        Paragraph(
            f"<b>Generated On</b> : {datetime.now().strftime('%d-%m-%Y %I:%M %p')}",
            normal_style
        )
    )

    elements.append(
        Spacer(1, 10)
    )

    elements.append(
        Paragraph(
            "=" * 95,
            normal_style
        )
    )

    elements.append(
        Spacer(1, 15)
    )

    # =====================================
    # USER INFORMATION
    # =====================================

    elements.append(
        Paragraph(
            "<b>USER INFORMATION</b>",
            heading_style
        )
    )

    elements.append(
        Spacer(1, 8)
    )

    user_info = [

        ("Name", user.name),

        ("Email", user.email),

        ("Age", user.age),

        ("Gender", user.gender),

        ("Height", f"{user.height} cm"),

        ("Weight", f"{user.weight} kg"),

        ("Fitness Goal", user.goal)

    ]

    user_info = [

         ["Name", user.name],
         ["Email", user.email],
         ["Age", user.age],
         ["Gender", user.gender],
         ["Height", f"{user.height} cm"],
         ["Weight", f"{user.weight} kg"],
         ["Fitness Goal", user.goal]
    ]

    info_table = Table(

        user_info,
        colWidths=[170, 250]
    )

    info_table.setStyle(TableStyle([


          ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
         ("FONTSIZE", (0, 0), (-1, -1), 11),
         ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
         ("LEFTPADDING", (0, 0), (-1, -1), 0),
         ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ]))

    elements.append(info_table)

    elements.append(
            Spacer(1, 4)
    )

    elements.append(
        Spacer(1, 8)
    )

    elements.append(
        Paragraph(
            "=" * 95,
            normal_style
        )
    )
    elements.append(
        Spacer(1, 15)
    )

    # =====================================
    # HEALTH INFORMATION
    # =====================================

    elements.append(
        Paragraph(
            "<b>HEALTH INFORMATION</b>",
            heading_style
        )
    )

    elements.append(
        Spacer(1, 8)
    )

    # -----------------------------
    # Calculate Health Details
    # -----------------------------

    bmi = calculate_bmi(
        user.weight,
        user.height
    )

    maintenance_calories = calculate_calories(
        user.age,
        user.gender,
        user.height,
        user.weight
    )

    protein = calculate_protein(
        user.weight,
        user.goal
    )

   

    # -----------------------------
    # Display Health Information
    # -----------------------------
    daily_water_goal = user.weight * 35

    if user.goal == "Muscle Gain":
        daily_water_goal += 300

    elif user.goal == "Weight Loss":
          daily_water_goal += 200

    if user.age and user.age >= 50:
           daily_water_goal += 100

    daily_water_goal = round(daily_water_goal)

    health_info = [


         ("BMI", bmi),

         ("Maintenance Calories / Day",
         f"{maintenance_calories} kcal"),

         ("Protein Intake / Day",
         f"{protein} g"),

         ("Water Intake / Day",
         f"{daily_water_goal} ml")

    ]

    health_data = [


         ["BMI", f"{bmi}"],

         ["Maintenance Calories / Day", f"{maintenance_calories} kcal"],

         ["Protein Intake / Day", f"{protein} g"],

         ["Water Intake / Day", f"{daily_water_goal} ml"]

    ]

    health_table = Table(


         health_data,

         colWidths=[220, 220]

    )

    health_table.setStyle(TableStyle([


         ("FONTNAME", (0,0), (-1,-1), "Helvetica"),

         ("FONTSIZE", (0,0), (-1,-1), 11),

         ("BOTTOMPADDING", (0,0), (-1,-1), 8),

         ("LEFTPADDING", (0,0), (-1,-1), 0),

         ("RIGHTPADDING", (0,0), (-1,-1), 0),

    ]))

    elements.append(health_table)


    elements.append(
            Spacer(1, 4)
    )

    elements.append(
        Spacer(1, 8)
    )
    # =====================================
    # Today's Intake
    # =====================================

    today_foods = FoodLog.query.filter(


        FoodLog.user_id == user.id,
        db.func.date(FoodLog.created_at) == date.today()

    ).all()

    total_calories = sum(food.calories for food in today_foods)
 
    total_protein = sum(food.protein for food in today_foods)

    water = WaterIntake.query.filter_by(

        user_id=user.id
    ).first()

    if water is None:

        water_amount = 0
    else:

        water_amount = water.amount


    elements.append(

       Paragraph(
           
           "<b>CURRENT INTAKE (TODAY)</b>",
           heading_style
       )
    )

    elements.append(

        Spacer(1, 8)
    )

    current_intake_data = [


        ["Calories Intake (Today)", f"{round(total_calories,1)} kcal"],

        ["Protein Intake (Today)", f"{round(total_protein,1)} g"],

        ["Water Intake (Today)", f"{water_amount} ml"]

    ]

    current_intake_table = Table(


        current_intake_data,

        colWidths=[220, 220]

    )

    current_intake_table.setStyle(TableStyle([


        ("FONTNAME", (0,0), (-1,-1), "Helvetica"),

        ("FONTSIZE", (0,0), (-1,-1), 11),

        ("BOTTOMPADDING", (0,0), (-1,-1), 8),

        ("LEFTPADDING", (0,0), (-1,-1), 0),

        ("RIGHTPADDING", (0,0), (-1,-1), 0),

    ]))

    elements.append(current_intake_table)


    elements.append(

       Spacer(1, 10)
    )

    elements.append(

        Paragraph(

            "=" * 95,
            normal_style
        )
    )

    elements.append(

       Spacer(1, 15)
    )
   
    # =====================================
    # WORKOUT INFORMATION
    # =====================================

    elements.append(
        Paragraph(
            "<b>WORKOUT INFORMATION</b>",
            heading_style
        )
    )

    elements.append(
        Spacer(1, 8)
    )

    workout_info = [

        ("Exercise", workout.exercise),

        ("Repetitions", workout.reps),

        ("Calories Burned", f"{workout.calories} kcal"),

        ("Accuracy", f"{workout.accuracy}%"),

        ("Workout Duration", workout.duration),

        ("Workout Date", workout.date)

    ]

    workout_data = [


         ["Exercise", workout.exercise],

         ["Repetitions", workout.reps],

         ["Calories Burned", f"{workout.calories} kcal"],

         ["Accuracy", f"{workout.accuracy}%"],

         ["Workout Duration", workout.duration],

         ["Workout Date", workout.date]

    ]

    workout_table = Table(


         workout_data,

         colWidths=[220, 220]

    )

    workout_table.setStyle(TableStyle([


         ("FONTNAME", (0,0), (-1,-1), "Helvetica"),

         ("FONTSIZE", (0,0), (-1,-1), 11),

         ("BOTTOMPADDING", (0,0), (-1,-1), 8),

         ("LEFTPADDING", (0,0), (-1,-1), 0),

        ("RIGHTPADDING", (0,0), (-1,-1), 0),

    ]))

    elements.append(workout_table)
    elements.append(
            Spacer(1, 4)
        )

    elements.append(
        Spacer(1, 15)
    )

    elements.append(
        Paragraph(
            "=" * 95,
            normal_style
        )
    )

    elements.append(
        Spacer(1, 15)
    )

    # =====================================
    # FOOTER
    # =====================================

    footer_style = styles["BodyText"]
    footer_style.alignment = TA_CENTER

    elements.append(
        Paragraph(
            "<b>Generated by VitaCore AI </b>",
            footer_style
        )
    )

    # =====================================
    # BUILD PDF
    # =====================================

    doc.build(elements)

    filename = f"VitaCore_AI_Report.pdf"
    return send_file(

        temp.name,

        as_attachment=True,

        download_name=filename,

        mimetype="application/pdf"

    )
# ---------------- RUN ---------------- #

import webbrowser

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True)

