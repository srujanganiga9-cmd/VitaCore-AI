from datetime import datetime

WORKOUTS = {

    # =====================================================
    # MUSCLE GAIN
    # =====================================================

    "Muscle Gain": {

        "Monday": {
    "title": "Chest & Triceps",
    "exercises": [

        {
            "name": "Push Ups",
            "sets": 4,
            "reps": 15,
            "rest": "60 sec",
            "target": "Chest",

            "difficulty": "Beginner",
            "time": "8 Minutes",

            "tip": "Keep your body in a straight line from head to heels. Lower your chest until it nearly touches the floor.",

            "video": "https://www.youtube.com/watch?v=IODxDxX7oi4"
        },

        {
            "name": "Bench Press",
            "sets": 4,
            "reps": 12,
            "rest": "90 sec",
            "target": "Chest",

            "difficulty": "Intermediate",
            "time": "10 Minutes",

            "tip": "Keep your feet firmly on the floor and lower the bar slowly to your chest before pressing upward.",

            "video": "https://www.youtube.com/watch?v=rT7DgCr-3pg"
        },

        {
            "name": "Incline Dumbbell Press",
            "sets": 3,
            "reps": 12,
            "rest": "60 sec",
            "target": "Upper Chest",

            "difficulty": "Intermediate",
            "time": "8 Minutes",

            "tip": "Press the dumbbells upward in a controlled motion and avoid locking your elbows at the top.",

            "video": "https://www.youtube.com/watch?v=8iPEnn-ltC8"
        },

        {
            "name": "Tricep Dips",
            "sets": 3,
            "reps": 15,
            "rest": "60 sec",
            "target": "Triceps",

            "difficulty": "Beginner",
            "time": "6 Minutes",

            "tip": "Keep your elbows close to your body and lower yourself until your elbows reach about 90 degrees.",

            "video": "https://www.youtube.com/watch?v=0326dy_-CzM"
        }

    ]
},

        "Tuesday": {
    "title": "Back & Biceps",
    "exercises": [

        {
            "name": "Pull Ups",
            "sets": 4,
            "reps": 10,
            "rest": "90 sec",
            "target": "Back",

            "difficulty": "Intermediate",
            "time": "10 Minutes",

            "tip": "Pull your chest toward the bar and avoid swinging your body.",

            "video": "https://www.youtube.com/watch?v=eGo4IYlbE5g"
        },

        {
            "name": "Barbell Row",
            "sets": 4,
            "reps": 12,
            "rest": "90 sec",
            "target": "Back",

            "difficulty": "Intermediate",
            "time": "10 Minutes",

            "tip": "Keep your back flat and pull the bar toward your lower chest using your back muscles.",

            "video": "https://www.youtube.com/watch?v=vT2GjY_Umpw"
        },

        {
            "name": "Bicep Curl",
            "sets": 3,
            "reps": 15,
            "rest": "60 sec",
            "target": "Biceps",

            "difficulty": "Beginner",
            "time": "8 Minutes",

            "tip": "Keep your elbows close to your sides and avoid using momentum to lift the weight.",

            "video": "https://www.youtube.com/watch?v=ykJmrZ5v0Oo"
        }

    ]
},

        "Wednesday": {
    "title": "Shoulders",
    "exercises": [

        {
            "name": "Shoulder Press",
            "sets": 4,
            "reps": 12,
            "rest": "60 sec",
            "target": "Shoulders",

            "difficulty": "Intermediate",
            "time": "10 Minutes",

            "tip": "Press the dumbbells overhead without arching your lower back. Keep your core engaged.",

            "video": "https://www.youtube.com/watch?v=qEwKCR5JCog"
        },

        {
            "name": "Lateral Raise",
            "sets": 3,
            "reps": 15,
            "rest": "45 sec",
            "target": "Side Delts",

            "difficulty": "Beginner",
            "time": "8 Minutes",

            "tip": "Raise the dumbbells only to shoulder height and avoid swinging your body.",

            "video": "https://www.youtube.com/watch?v=3VcKaXpzqRo"
        },

        {
            "name": "Front Raise",
            "sets": 3,
            "reps": 12,
            "rest": "45 sec",
            "target": "Front Delts",

            "difficulty": "Beginner",
            "time": "7 Minutes",

            "tip": "Lift the dumbbells slowly to shoulder height and lower them under control.",

            "video": "https://www.youtube.com/watch?v=-t7fuZ0KhDA"
        },

        {
            "name": "Face Pull",
            "sets": 3,
            "reps": 15,
            "rest": "45 sec",
            "target": "Rear Delts",

            "difficulty": "Intermediate",
            "time": "8 Minutes",

            "tip": "Pull the rope toward your face while keeping your elbows high to target the rear shoulders.",

            "video": "https://www.youtube.com/watch?v=rep-qVOkqgk"
        }

    ]
},

        "Thursday": {
    "title": "Leg Day",
    "exercises": [

        {
            "name": "Barbell Squats",
            "sets": 4,
            "reps": 12,
            "rest": "90 sec",
            "target": "Quadriceps & Glutes",

            "difficulty": "Intermediate",
            "time": "12 Minutes",

            "tip": "Keep your chest up, back straight, and lower until your thighs are parallel to the floor.",

            "video": "https://www.youtube.com/watch?v=ultWZbUMPL8"
        },

        {
            "name": "Leg Press",
            "sets": 4,
            "reps": 12,
            "rest": "60 sec",
            "target": "Quadriceps",

            "difficulty": "Beginner",
            "time": "10 Minutes",

            "tip": "Keep your feet shoulder-width apart and avoid locking your knees at the top.",

            "video": "https://www.youtube.com/watch?v=IZxyjW7MPJQ"
        },

        {
            "name": "Walking Lunges",
            "sets": 3,
            "reps": 12,
            "rest": "60 sec",
            "target": "Glutes & Hamstrings",

            "difficulty": "Intermediate",
            "time": "8 Minutes",

            "tip": "Take controlled steps and keep your front knee aligned with your toes.",

            "video": "https://www.youtube.com/watch?v=wrwwXE_x-pQ"
        },

        {
            "name": "Romanian Deadlift",
            "sets": 3,
            "reps": 10,
            "rest": "75 sec",
            "target": "Hamstrings",

            "difficulty": "Intermediate",
            "time": "10 Minutes",

            "tip": "Keep the bar close to your legs and hinge at the hips while maintaining a neutral spine.",

            "video": "https://www.youtube.com/watch?v=2SHsk9AzdjA"
        },

        {
            "name": "Standing Calf Raises",
            "sets": 4,
            "reps": 20,
            "rest": "45 sec",
            "target": "Calves",

            "difficulty": "Beginner",
            "time": "6 Minutes",

            "tip": "Pause at the top of each repetition and lower your heels slowly for a full stretch.",

            "video": "https://www.youtube.com/watch?v=-M4-G8p8fmc"
        }

    ]
},

        "Friday": {
    "title": "Arms & Abs",
    "exercises": [

        {
            "name": "Hammer Curls",
            "sets": 4,
            "reps": 12,
            "rest": "60 sec",
            "target": "Biceps & Forearms",

            "difficulty": "Beginner",
            "time": "8 Minutes",

            "tip": "Keep your elbows close to your body and lift the dumbbells without swinging.",

            "video": "https://www.youtube.com/watch?v=zC3nLlEvin4"
        },

        {
            "name": "Tricep Pushdown",
            "sets": 4,
            "reps": 12,
            "rest": "60 sec",
            "target": "Triceps",

            "difficulty": "Beginner",
            "time": "8 Minutes",

            "tip": "Keep your elbows fixed at your sides and fully extend your arms at the bottom.",

            "video": "https://www.youtube.com/watch?v=2-LAMcpzODU"
        },

        {
            "name": "Overhead Tricep Extension",
            "sets": 3,
            "reps": 12,
            "rest": "60 sec",
            "target": "Triceps",

            "difficulty": "Intermediate",
            "time": "8 Minutes",

            "tip": "Keep your upper arms close to your head and avoid arching your back.",

            "video": "https://www.youtube.com/watch?v=_gsUck-7M74"
        },

        {
            "name": "Plank",
            "sets": 3,
            "reps": "60 sec",
            "rest": "45 sec",
            "target": "Core",

            "difficulty": "Beginner",
            "time": "6 Minutes",

            "tip": "Keep your body in a straight line and tighten your core throughout the hold.",

            "video": "https://www.youtube.com/watch?v=pSHjTRCQxIw"
        },

        {
            "name": "Bicycle Crunches",
            "sets": 3,
            "reps": 20,
            "rest": "45 sec",
            "target": "Abs",

            "difficulty": "Beginner",
            "time": "6 Minutes",

            "tip": "Rotate your torso and bring your elbow toward the opposite knee without pulling your neck.",

            "video": "https://www.youtube.com/watch?v=9FGilxCbdz8"
        }

    ]
},

        "Saturday": {
    "title": "Full Body & Core",
    "exercises": [

        {
            "name": "Burpees",
            "sets": 3,
            "reps": 15,
            "rest": "60 sec",
            "target": "Full Body",

            "difficulty": "Intermediate",
            "time": "8 Minutes",

            "tip": "Land softly after each jump and maintain a steady rhythm throughout the exercise.",

            "video": "https://www.youtube.com/watch?v=TU8QYVW0gDU"
        },

        {
            "name": "Mountain Climbers",
            "sets": 3,
            "reps": 20,
            "rest": "45 sec",
            "target": "Core",

            "difficulty": "Beginner",
            "time": "6 Minutes",

            "tip": "Keep your hips level and drive your knees toward your chest without bouncing.",

            "video": "https://www.youtube.com/watch?v=nmwgirgXLYM"
        },

        {
            "name": "Kettlebell Swings",
            "sets": 3,
            "reps": 15,
            "rest": "60 sec",
            "target": "Glutes & Hamstrings",

            "difficulty": "Intermediate",
            "time": "8 Minutes",

            "tip": "Use your hips to generate power instead of lifting with your arms.",

            "video": "https://www.youtube.com/watch?v=YSxHifyI5-U"
        },

        {
            "name": "Russian Twists",
            "sets": 3,
            "reps": 20,
            "rest": "45 sec",
            "target": "Obliques",

            "difficulty": "Beginner",
            "time": "6 Minutes",

            "tip": "Rotate your torso slowly and keep your feet slightly raised for more challenge.",

            "video": "https://www.youtube.com/watch?v=wkD8rjkodUI"
        },

        {
            "name": "Jump Squats",
            "sets": 3,
            "reps": 15,
            "rest": "60 sec",
            "target": "Legs",

            "difficulty": "Intermediate",
            "time": "8 Minutes",

            "tip": "Land with your knees slightly bent to reduce impact and protect your joints.",

            "video": "https://www.youtube.com/watch?v=CVaEhXotL7M"
        }

    ]
},
"Sunday": {
    "title": "Recovery & Mobility",
    "exercises": [

        {
            "name": "Full Body Stretching",
            "sets": 1,
            "reps": "20 Minutes",
            "rest": "-",
            "target": "Full Body",

            "difficulty": "Beginner",
            "time": "20 Minutes",

            "tip": "Stretch slowly without bouncing and hold each stretch for 20–30 seconds.",

            "video": "https://www.youtube.com/watch?v=L_xrDAtykMI"
        },

        {
            "name": "Walking",
            "sets": 1,
            "reps": "30 Minutes",
            "rest": "-",
            "target": "Cardio",

            "difficulty": "Beginner",
            "time": "30 Minutes",

            "tip": "Maintain a comfortable pace and focus on relaxed, steady breathing.",

            "video": "https://www.youtube.com/watch?v=njeZ29umqVE"
        },

        {
            "name": "Foam Rolling",
            "sets": 1,
            "reps": "15 Minutes",
            "rest": "-",
            "target": "Muscle Recovery",

            "difficulty": "Beginner",
            "time": "15 Minutes",

            "tip": "Roll slowly over tight muscles and pause for a few seconds on sore areas.",

            "video": "https://www.youtube.com/watch?v=8caF1Keg2XU"
        },

        {
            "name": "Deep Breathing",
            "sets": 3,
            "reps": "10 Breaths",
            "rest": "30 sec",
            "target": "Relaxation",

            "difficulty": "Beginner",
            "time": "5 Minutes",

            "tip": "Inhale deeply through your nose and exhale slowly through your mouth to relax your body.",

            "video": "https://www.youtube.com/watch?v=odADwWzHR24"
        }

    ]
},

        
    },

    # =====================================================
    # WEIGHT LOSS
    # =====================================================

    "Weight Loss": {

        "Monday": {
    "title": "HIIT Cardio",
    "exercises": [

        {
            "name":"Jumping Jacks",
            "sets":4,
            "reps":40,
            "rest":"30 sec",
            "target":"Full Body",

            "difficulty":"Beginner",
            "time":"6 Minutes",

            "tip":"Land softly on your feet and keep a steady rhythm throughout the movement.",

            "video":"https://www.youtube.com/watch?v=c4DAnQ6DtF8"
        },

        {
            "name":"Burpees",
            "sets":4,
            "reps":15,
            "rest":"30 sec",
            "target":"Full Body",

            "difficulty":"Intermediate",
            "time":"8 Minutes",

            "tip":"Keep your core engaged and land with slightly bent knees to reduce impact.",

            "video":"https://www.youtube.com/watch?v=TU8QYVW0gDU"
        },

        {
            "name":"Mountain Climbers",
            "sets":4,
            "reps":25,
            "rest":"30 sec",
            "target":"Core",

            "difficulty":"Beginner",
            "time":"7 Minutes",

            "tip":"Keep your hips level and drive your knees toward your chest without bouncing.",

            "video":"https://www.youtube.com/watch?v=nmwgirgXLYM"
        }

    ]
},

        "Tuesday": {
    "title": "Legs + Cardio",
    "exercises": [

        {
            "name":"Bodyweight Squats",
            "sets":4,
            "reps":20,
            "rest":"45 sec",
            "target":"Quadriceps & Glutes",

            "difficulty":"Beginner",
            "time":"8 Minutes",

            "tip":"Keep your chest up and lower until your thighs are parallel to the floor.",

            "video":"https://www.youtube.com/watch?v=aclHkVaku9U"
        },

        {
            "name":"Walking Lunges",
            "sets":4,
            "reps":15,
            "rest":"45 sec",
            "target":"Glutes & Hamstrings",

            "difficulty":"Intermediate",
            "time":"8 Minutes",

            "tip":"Take controlled steps and keep your front knee aligned with your toes.",

            "video":"https://www.youtube.com/watch?v=wrwwXE_x-pQ"
        },

        {
            "name":"High Knees",
            "sets":4,
            "reps":"45 sec",
            "rest":"30 sec",
            "target":"Cardio",

            "difficulty":"Beginner",
            "time":"6 Minutes",

            "tip":"Lift your knees to waist height while pumping your arms for maximum intensity.",

            "video":"https://www.youtube.com/watch?v=OAJ_J3EZkdY"
        },

        {
            "name":"Jump Squats",
            "sets":3,
            "reps":15,
            "rest":"45 sec",
            "target":"Legs",

            "difficulty":"Intermediate",
            "time":"7 Minutes",

            "tip":"Land softly with bent knees and explode upward using your leg muscles.",

            "video":"https://www.youtube.com/watch?v=CVaEhXotL7M"
        }

    ]
},

        "Wednesday": {
    "title": "Core & Abs",
    "exercises": [

        {
            "name":"Plank",
            "sets":3,
            "reps":"60 sec",
            "rest":"30 sec",
            "target":"Core",

            "difficulty":"Beginner",
            "time":"6 Minutes",

            "tip":"Keep your body in a straight line from head to heels and avoid letting your hips sag.",

            "video":"https://www.youtube.com/watch?v=pSHjTRCQxIw"
        },

        {
            "name":"Crunches",
            "sets":4,
            "reps":20,
            "rest":"30 sec",
            "target":"Upper Abs",

            "difficulty":"Beginner",
            "time":"7 Minutes",

            "tip":"Lift using your abdominal muscles instead of pulling your neck with your hands.",

            "video":"https://www.youtube.com/watch?v=Xyd_fa5zoEU"
        },

        {
            "name":"Russian Twists",
            "sets":3,
            "reps":20,
            "rest":"30 sec",
            "target":"Obliques",

            "difficulty":"Intermediate",
            "time":"7 Minutes",

            "tip":"Rotate your shoulders instead of just your arms and keep your core engaged.",

            "video":"https://www.youtube.com/watch?v=wkD8rjkodUI"
        },

        {
            "name":"Leg Raises",
            "sets":3,
            "reps":15,
            "rest":"45 sec",
            "target":"Lower Abs",

            "difficulty":"Intermediate",
            "time":"8 Minutes",

            "tip":"Lower your legs slowly without letting your lower back lift off the floor.",

            "video":"https://www.youtube.com/watch?v=JB2oyawG9KI"
        },

        {
            "name":"Bicycle Crunches",
            "sets":3,
            "reps":20,
            "rest":"30 sec",
            "target":"Abs",

            "difficulty":"Beginner",
            "time":"6 Minutes",

            "tip":"Bring your elbow toward the opposite knee while keeping the movement slow and controlled.",

            "video":"https://www.youtube.com/watch?v=9FGilxCbdz8"
        }

    ]
},

       "Thursday": {
    "title":"HIIT + Full Body",
    "exercises":[

        {
            "name":"Jump Rope",
            "sets":5,
            "reps":"2 Minutes",
            "rest":"30 sec",
            "target":"Cardio",

            "difficulty":"Beginner",
            "time":"12 Minutes",

            "tip":"Stay on the balls of your feet and keep your jumps low to conserve energy.",

            "video":"https://www.youtube.com/watch?v=u3zgHI8QnqE"
        },

        {
            "name":"Burpees",
            "sets":4,
            "reps":15,
            "rest":"30 sec",
            "target":"Full Body",

            "difficulty":"Intermediate",
            "time":"8 Minutes",

            "tip":"Keep your core tight and land softly after each jump to reduce impact.",

            "video":"https://www.youtube.com/watch?v=TU8QYVW0gDU"
        },

        {
            "name":"Mountain Climbers",
            "sets":4,
            "reps":25,
            "rest":"30 sec",
            "target":"Core",

            "difficulty":"Beginner",
            "time":"7 Minutes",

            "tip":"Maintain a straight back and move your knees quickly while keeping your hips stable.",

            "video":"https://www.youtube.com/watch?v=nmwgirgXLYM"
        },

        {
            "name":"Jumping Jacks",
            "sets":4,
            "reps":40,
            "rest":"30 sec",
            "target":"Full Body",

            "difficulty":"Beginner",
            "time":"6 Minutes",

            "tip":"Swing your arms fully overhead and land softly with slightly bent knees.",

            "video":"https://www.youtube.com/watch?v=c4DAnQ6DtF8"
        },

        {
            "name":"High Knees",
            "sets":4,
            "reps":"45 sec",
            "rest":"30 sec",
            "target":"Cardio",

            "difficulty":"Intermediate",
            "time":"6 Minutes",

            "tip":"Drive your knees high while maintaining a quick pace and active arm movement.",

            "video":"https://www.youtube.com/watch?v=OAJ_J3EZkdY"
        }

    ]
},

        "Friday": {
    "title":"Fat Burn Circuit",
    "exercises":[

        {
            "name":"Jump Squats",
            "sets":4,
            "reps":15,
            "rest":"30 sec",
            "target":"Legs",

            "difficulty":"Intermediate",
            "time":"8 Minutes",

            "tip":"Explode upward with power and land softly with your knees slightly bent.",

            "video":"https://www.youtube.com/watch?v=CVaEhXotL7M"
        },

        {
            "name":"Burpees",
            "sets":4,
            "reps":12,
            "rest":"30 sec",
            "target":"Full Body",

            "difficulty":"Intermediate",
            "time":"8 Minutes",

            "tip":"Maintain a smooth rhythm and keep your core engaged throughout the movement.",

            "video":"https://www.youtube.com/watch?v=TU8QYVW0gDU"
        },

        {
            "name":"Push Ups",
            "sets":3,
            "reps":15,
            "rest":"45 sec",
            "target":"Chest & Arms",

            "difficulty":"Beginner",
            "time":"7 Minutes",

            "tip":"Lower your chest with control and push back up without letting your hips sag.",

            "video":"https://www.youtube.com/watch?v=IODxDxX7oi4"
        },

        {
            "name":"Mountain Climbers",
            "sets":3,
            "reps":30,
            "rest":"30 sec",
            "target":"Core & Cardio",

            "difficulty":"Beginner",
            "time":"7 Minutes",

            "tip":"Drive your knees quickly while keeping your shoulders directly over your hands.",

            "video":"https://www.youtube.com/watch?v=nmwgirgXLYM"
        },

        {
            "name":"Plank",
            "sets":3,
            "reps":"60 sec",
            "rest":"30 sec",
            "target":"Core",

            "difficulty":"Beginner",
            "time":"6 Minutes",

            "tip":"Brace your core and avoid raising or dropping your hips during the hold.",

            "video":"https://www.youtube.com/watch?v=pSHjTRCQxIw"
        }

    ]
},

        "Saturday": {
    "title":"Outdoor Cardio",
    "exercises":[

        {
            "name":"Brisk Walking",
            "sets":1,
            "reps":"45 Minutes",
            "rest":"-",
            "target":"Cardio",

            "difficulty":"Beginner",
            "time":"45 Minutes",

            "tip":"Walk at a pace where you can still talk but feel slightly out of breath.",

            "video":"https://www.youtube.com/watch?v=enYITYwvPAQ"
        },

        {
            "name":"Cycling",
            "sets":1,
            "reps":"30 Minutes",
            "rest":"-",
            "target":"Legs & Cardio",

            "difficulty":"Beginner",
            "time":"30 Minutes",

            "tip":"Maintain a steady cadence and adjust the resistance to keep your heart rate elevated.",

            "video":"https://www.youtube.com/watch?v=ZX3fKolI25Q"
        },

        {
            "name":"Jogging",
            "sets":1,
            "reps":"20 Minutes",
            "rest":"-",
            "target":"Full Body Cardio",

            "difficulty":"Intermediate",
            "time":"20 Minutes",

            "tip":"Land softly on your feet and maintain an upright posture while jogging.",

            "video":"https://www.youtube.com/watch?v=_kGESn8ArrU"
        },

        {
            "name":"Jump Rope",
            "sets":3,
            "reps":"2 Minutes",
            "rest":"45 sec",
            "target":"Cardio",

            "difficulty":"Intermediate",
            "time":"8 Minutes",

            "tip":"Rotate the rope using your wrists instead of your arms and keep your jumps small.",

            "video":"https://www.youtube.com/watch?v=u3zgHI8QnqE"
        },

        {
            "name":"Cool Down Stretch",
            "sets":1,
            "reps":"10 Minutes",
            "rest":"-",
            "target":"Flexibility",

            "difficulty":"Beginner",
            "time":"10 Minutes",

            "tip":"Stretch each major muscle group slowly and never force a stretch beyond a comfortable range.",

            "video":"https://www.youtube.com/watch?v=L_xrDAtykMI"
        }

    ]
},

        "Sunday": {
    "title":"Recovery & Stretching",
    "exercises":[

        {
            "name":"Brisk Walking",
            "sets":1,
            "reps":"30 Minutes",
            "rest":"-",
            "target":"Cardio",

            "difficulty":"Beginner",
            "time":"30 Minutes",

            "tip":"Walk at a comfortable pace while maintaining good posture and steady breathing.",

            "video":"https://www.youtube.com/watch?v=enYITYwvPAQ"
        },

        {
            "name":"Full Body Stretching",
            "sets":1,
            "reps":"20 Minutes",
            "rest":"-",
            "target":"Flexibility",

            "difficulty":"Beginner",
            "time":"20 Minutes",

            "tip":"Hold each stretch for 20–30 seconds without bouncing to improve flexibility safely.",

            "video":"https://www.youtube.com/watch?v=L_xrDAtykMI"
        },

        {
            "name":"Yoga Flow",
            "sets":1,
            "reps":"20 Minutes",
            "rest":"-",
            "target":"Mobility",

            "difficulty":"Beginner",
            "time":"20 Minutes",

            "tip":"Move slowly between poses and focus on controlled breathing throughout the session.",

            "video":"https://www.youtube.com/watch?v=v7AYKMP6rOE"
        },

        {
            "name":"Foam Rolling",
            "sets":1,
            "reps":"15 Minutes",
            "rest":"-",
            "target":"Muscle Recovery",

            "difficulty":"Beginner",
            "time":"15 Minutes",

            "tip":"Roll each muscle group slowly and pause for a few seconds on tight areas.",

            "video":"https://www.youtube.com/watch?v=8caF1Keg2XU"
        },

        {
            "name":"Deep Breathing",
            "sets":3,
            "reps":"10 Breaths",
            "rest":"30 sec",
            "target":"Relaxation",

            "difficulty":"Beginner",
            "time":"5 Minutes",

            "tip":"Take slow, deep breaths through your nose and exhale gently through your mouth to relax your body.",

            "video":"https://www.youtube.com/watch?v=odADwWzHR24"
        }

    ]
},

    },

    # =====================================================
    # MAINTAIN FITNESS
    # =====================================================

    "Maintain Fitness": {

        "Monday": {
    "title":"Upper Body",
    "exercises":[

        {
            "name":"Push Ups",
            "sets":3,
            "reps":12,
            "rest":"60 sec",
            "target":"Chest",

            "difficulty":"Beginner",
            "time":"7 Minutes",

            "tip":"Keep your body straight from head to heels and lower your chest with control.",

            "video":"https://www.youtube.com/watch?v=IODxDxX7oi4"
        },

        {
            "name":"Shoulder Press",
            "sets":3,
            "reps":12,
            "rest":"60 sec",
            "target":"Shoulders",

            "difficulty":"Intermediate",
            "time":"8 Minutes",

            "tip":"Keep your core tight and press the weights overhead without arching your back.",

            "video":"https://www.youtube.com/watch?v=qEwKCR5JCog"
        },

        {
            "name":"Bent Over Row",
            "sets":3,
            "reps":12,
            "rest":"60 sec",
            "target":"Back",

            "difficulty":"Intermediate",
            "time":"8 Minutes",

            "tip":"Keep your back flat and pull the weight toward your waist.",

            "video":"https://www.youtube.com/watch?v=vT2GjY_Umpw"
        },

        {
            "name":"Tricep Dips",
            "sets":3,
            "reps":15,
            "rest":"60 sec",
            "target":"Triceps",

            "difficulty":"Beginner",
            "time":"6 Minutes",

            "tip":"Lower yourself slowly while keeping your elbows close to your body.",

            "video":"https://www.youtube.com/watch?v=0326dy_-CzM"
        }

    ]
},
       "Tuesday": {
    "title":"Lower Body",
    "exercises":[

        {
            "name":"Bodyweight Squats",
            "sets":3,
            "reps":15,
            "rest":"45 sec",
            "target":"Quadriceps & Glutes",

            "difficulty":"Beginner",
            "time":"8 Minutes",

            "tip":"Keep your chest lifted and push your hips back as you squat down.",

            "video":"https://www.youtube.com/watch?v=aclHkVaku9U"
        },

        {
            "name":"Walking Lunges",
            "sets":3,
            "reps":12,
            "rest":"45 sec",
            "target":"Glutes & Hamstrings",

            "difficulty":"Beginner",
            "time":"7 Minutes",

            "tip":"Take controlled steps and keep your front knee aligned with your ankle.",

            "video":"https://www.youtube.com/watch?v=wrwwXE_x-pQ"
        },

        {
            "name":"Glute Bridge",
            "sets":3,
            "reps":15,
            "rest":"45 sec",
            "target":"Glutes",

            "difficulty":"Beginner",
            "time":"6 Minutes",

            "tip":"Squeeze your glutes at the top and avoid arching your lower back.",

            "video":"https://www.youtube.com/watch?v=m2Zx-57cSok"
        },

        {
            "name":"Standing Calf Raises",
            "sets":3,
            "reps":20,
            "rest":"30 sec",
            "target":"Calves",

            "difficulty":"Beginner",
            "time":"5 Minutes",

            "tip":"Pause at the top of each repetition and lower your heels slowly.",

            "video":"https://www.youtube.com/watch?v=-M4-G8p8fmc"
        }

    ]
},

        "Wednesday": {
    "title":"Cardio",
    "exercises":[

        {
            "name":"Brisk Walking",
            "sets":1,
            "reps":"30 Minutes",
            "rest":"-",
            "target":"Cardio",

            "difficulty":"Beginner",
            "time":"30 Minutes",

            "tip":"Maintain a brisk pace where you can still talk but feel your heart rate increase.",

            "video":"https://www.youtube.com/watch?v=enYITYwvPAQ"
        },

        {
            "name":"Cycling",
            "sets":1,
            "reps":"20 Minutes",
            "rest":"-",
            "target":"Legs & Cardio",

            "difficulty":"Beginner",
            "time":"20 Minutes",

            "tip":"Keep a steady pedaling rhythm and avoid hunching your shoulders.",

            "video":"https://www.youtube.com/watch?v=ZX3fKolI25Q"
        },

        {
            "name":"Jump Rope",
            "sets":3,
            "reps":"2 Minutes",
            "rest":"45 sec",
            "target":"Cardio",

            "difficulty":"Intermediate",
            "time":"8 Minutes",

            "tip":"Jump lightly on the balls of your feet and rotate the rope using your wrists.",

            "video":"https://www.youtube.com/watch?v=u3zgHI8QnqE"
        },

        {
            "name":"High Knees",
            "sets":3,
            "reps":"30 sec",
            "rest":"30 sec",
            "target":"Cardio & Legs",

            "difficulty":"Beginner",
            "time":"5 Minutes",

            "tip":"Lift your knees to hip level while keeping a steady rhythm with your arms.",

            "video":"https://www.youtube.com/watch?v=OAJ_J3EZkdY"
        }

    ]
},
        "Thursday": {
    "title":"Core Strength",
    "exercises":[

        {
            "name":"Plank",
            "sets":3,
            "reps":"45 sec",
            "rest":"30 sec",
            "target":"Core",

            "difficulty":"Beginner",
            "time":"6 Minutes",

            "tip":"Keep your body in a straight line and tighten your core throughout the exercise.",

            "video":"https://www.youtube.com/watch?v=pSHjTRCQxIw"
        },

        {
            "name":"Crunches",
            "sets":3,
            "reps":20,
            "rest":"30 sec",
            "target":"Upper Abs",

            "difficulty":"Beginner",
            "time":"6 Minutes",

            "tip":"Lift your shoulders using your abdominal muscles instead of pulling your neck.",

            "video":"https://www.youtube.com/watch?v=Xyd_fa5zoEU"
        },

        {
            "name":"Russian Twists",
            "sets":3,
            "reps":20,
            "rest":"30 sec",
            "target":"Obliques",

            "difficulty":"Intermediate",
            "time":"7 Minutes",

            "tip":"Rotate your upper body slowly while keeping your core engaged.",

            "video":"https://www.youtube.com/watch?v=wkD8rjkodUI"
        },

        {
            "name":"Bird Dog",
            "sets":3,
            "reps":12,
            "rest":"30 sec",
            "target":"Core & Lower Back",

            "difficulty":"Beginner",
            "time":"6 Minutes",

            "tip":"Extend one arm and the opposite leg while keeping your hips stable.",

            "video":"https://www.youtube.com/watch?v=wiFNA3sqjCA"
        },

        {
            "name":"Leg Raises",
            "sets":3,
            "reps":15,
            "rest":"45 sec",
            "target":"Lower Abs",

            "difficulty":"Intermediate",
            "time":"7 Minutes",

            "tip":"Lower your legs slowly and keep your lower back pressed against the floor.",

            "video":"https://www.youtube.com/watch?v=JB2oyawG9KI"
        }

    ]
},

        "Friday": {
    "title":"Full Body",
    "exercises":[

        {
            "name":"Push Ups",
            "sets":3,
            "reps":12,
            "rest":"60 sec",
            "target":"Chest & Triceps",

            "difficulty":"Beginner",
            "time":"7 Minutes",

            "tip":"Keep your body in a straight line and lower your chest with control before pushing back up.",

            "video":"https://www.youtube.com/watch?v=IODxDxX7oi4"
        },

        {
            "name":"Bodyweight Squats",
            "sets":3,
            "reps":15,
            "rest":"45 sec",
            "target":"Legs",

            "difficulty":"Beginner",
            "time":"7 Minutes",

            "tip":"Push your hips back and keep your knees aligned with your toes throughout the movement.",

            "video":"https://www.youtube.com/watch?v=aclHkVaku9U"
        },

        {
            "name":"Dumbbell Shoulder Press",
            "sets":3,
            "reps":12,
            "rest":"60 sec",
            "target":"Shoulders",

            "difficulty":"Intermediate",
            "time":"8 Minutes",

            "tip":"Press the dumbbells overhead without locking your elbows and keep your core tight.",

            "video":"https://www.youtube.com/watch?v=qEwKCR5JCog"
        },

        {
            "name":"Mountain Climbers",
            "sets":3,
            "reps":20,
            "rest":"30 sec",
            "target":"Core & Cardio",

            "difficulty":"Beginner",
            "time":"6 Minutes",

            "tip":"Keep your hips level and drive your knees forward quickly while maintaining good form.",

            "video":"https://www.youtube.com/watch?v=nmwgirgXLYM"
        },

        {
            "name":"Plank",
            "sets":3,
            "reps":"45 sec",
            "rest":"30 sec",
            "target":"Core",

            "difficulty":"Beginner",
            "time":"5 Minutes",

            "tip":"Brace your abdominal muscles and avoid letting your hips rise or sag.",

            "video":"https://www.youtube.com/watch?v=pSHjTRCQxIw"
        }

    ]
},

        "Saturday": {
    "title":"Outdoor Activity",
    "exercises":[

        {
            "name":"Brisk Walking",
            "sets":1,
            "reps":"40 Minutes",
            "rest":"-",
            "target":"Cardio",

            "difficulty":"Beginner",
            "time":"40 Minutes",

            "tip":"Walk at a pace that raises your heart rate while allowing you to comfortably hold a conversation.",

            "video":"https://www.youtube.com/watch?v=enYITYwvPAQ"
        },

        {
            "name":"Cycling",
            "sets":1,
            "reps":"30 Minutes",
            "rest":"-",
            "target":"Legs & Cardio",

            "difficulty":"Beginner",
            "time":"30 Minutes",

            "tip":"Maintain a smooth pedaling rhythm and keep your back relaxed throughout the ride.",

            "video":"https://www.youtube.com/watch?v=ZX3fKolI25Q"
        },

        {
            "name":"Jogging",
            "sets":1,
            "reps":"20 Minutes",
            "rest":"-",
            "target":"Cardio",

            "difficulty":"Intermediate",
            "time":"20 Minutes",

            "tip":"Keep an upright posture, relax your shoulders, and land softly on your feet.",

            "video":"https://www.youtube.com/watch?v=_kGESn8ArrU"
        },

        {
            "name":"Jump Rope",
            "sets":3,
            "reps":"2 Minutes",
            "rest":"45 sec",
            "target":"Cardio",

            "difficulty":"Intermediate",
            "time":"8 Minutes",

            "tip":"Jump lightly on the balls of your feet and let your wrists rotate the rope.",

            "video":"https://www.youtube.com/watch?v=u3zgHI8QnqE"
        },

        {
            "name":"Cool Down Stretch",
            "sets":1,
            "reps":"10 Minutes",
            "rest":"-",
            "target":"Flexibility",

            "difficulty":"Beginner",
            "time":"10 Minutes",

            "tip":"Stretch each major muscle group gently and breathe deeply to improve flexibility.",

            "video":"https://www.youtube.com/watch?v=L_xrDAtykMI"
        }

    ]
},

        "Sunday": {
    "title":"Recovery & Stretching",
    "exercises":[

        {
            "name":"Full Body Stretching",
            "sets":1,
            "reps":"20 Minutes",
            "rest":"-",
            "target":"Flexibility",

            "difficulty":"Beginner",
            "time":"20 Minutes",

            "tip":"Stretch slowly and hold each stretch for 20–30 seconds without bouncing.",

            "video":"https://www.youtube.com/watch?v=L_xrDAtykMI"
        },

        {
            "name":"Yoga Flow",
            "sets":1,
            "reps":"20 Minutes",
            "rest":"-",
            "target":"Mobility",

            "difficulty":"Beginner",
            "time":"20 Minutes",

            "tip":"Move smoothly between poses while focusing on slow, controlled breathing.",

            "video":"https://www.youtube.com/watch?v=v7AYKMP6rOE"
        },

        {
            "name":"Brisk Walking",
            "sets":1,
            "reps":"30 Minutes",
            "rest":"-",
            "target":"Cardio",

            "difficulty":"Beginner",
            "time":"30 Minutes",

            "tip":"Walk at a comfortable pace to improve circulation and aid muscle recovery.",

            "video":"https://www.youtube.com/watch?v=enYITYwvPAQ"
        },

        {
            "name":"Foam Rolling",
            "sets":1,
            "reps":"15 Minutes",
            "rest":"-",
            "target":"Muscle Recovery",

            "difficulty":"Beginner",
            "time":"15 Minutes",

            "tip":"Roll each muscle group slowly and pause on tight areas for a few seconds.",

            "video":"https://www.youtube.com/watch?v=8caF1Keg2XU"
        },

        {
            "name":"Deep Breathing & Relaxation",
            "sets":3,
            "reps":"10 Breaths",
            "rest":"30 sec",
            "target":"Relaxation",

            "difficulty":"Beginner",
            "time":"5 Minutes",

            "tip":"Inhale deeply through your nose and exhale slowly through your mouth to relax your body and mind.",

            "video":"https://www.youtube.com/watch?v=odADwWzHR24"
        }

    ]
},

    }

}


def get_workout_plan(goal):
    
    if goal not in WORKOUTS:
        goal = "Maintain Fitness"

    return WORKOUTS[goal]