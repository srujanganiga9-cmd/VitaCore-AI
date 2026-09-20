class JumpingCounter:
    
    def __init__(self):

        self.reps = 0
        self.stage = "CLOSED"
        self.body_detected = False
        self.started = False
        

    def process(self, landmarks):
        if not self.started:

    
             return {
                 

                 "reps": self.reps,

                 "accuracy": 0,

                 "calories": round(self.reps * 0.5, 1),

                 "status": "▶ Press Start to Begin",

                 "tips": [ 
                      

                     "Click the Start button to begin workout.",
 
                     "AI is waiting..."

                 ]

             }

        # ----------------------------
        # Landmarks
        # ----------------------------

        nose = landmarks[0]

        left_shoulder = landmarks[11]
        right_shoulder = landmarks[12]

        left_wrist = landmarks[15]
        right_wrist = landmarks[16]

        left_ankle = landmarks[27]
        right_ankle = landmarks[28]

        

        # ----------------------------
        # Arms Above Head
        # ----------------------------

        arms_up = (

            left_wrist.y < nose.y + 0.03 and
            right_wrist.y < nose.y + 0.03

        )

        # ----------------------------
        # Adaptive Leg Distance
        # ----------------------------

        shoulder_width = abs(left_shoulder.x - right_shoulder.x)

        leg_distance = abs(left_ankle.x - right_ankle.x)

        legs_apart = leg_distance > shoulder_width * 1.7

        legs_closed = leg_distance < shoulder_width * 1.0

        # ----------------------------
        # Rep Counter
        # ----------------------------

        status = "🙆 Jump Wider"

        if legs_closed and not arms_up:

            self.stage = "READY"

            status = "🧍 Ready"

        elif arms_up and legs_apart and self.stage == "READY":

            self.stage = "OPEN"

            self.reps += 1

            status = "✅ Excellent Rep"

        elif legs_closed and self.stage == "OPEN":

            self.stage = "READY"

            status = "🧍 Ready"

        # ----------------------------
        # Accuracy
        # ----------------------------

        if arms_up and legs_apart:

            accuracy = 100

        elif legs_apart:

            accuracy = 95

        elif arms_up:

            accuracy = 92

        else:

            accuracy = 88

        # ----------------------------
        # Calories
        # ----------------------------

        calories = round(self.reps * 0.6, 1)

        # ----------------------------
        # AI Coaching Tips
        # ----------------------------

        if status == "✅ Excellent Rep":

            tips = [

                "Excellent jumping technique.",

                "Raise your hands fully overhead."

            ]

        elif status == "🧍 Ready":

            tips = [

                "Great starting position.",

                "Jump explosively on your next rep."

            ]

        elif status == "🙆 Jump Wider":

            tips = [

                "Spread your legs wider.",

                "Move your arms and legs together."

            ]

        else:

            tips = [

                "Keep your full body visible.",

                "Stand farther from the camera."

            ]

        # ----------------------------
        # Return Result
        # ----------------------------

        return {

            "reps": self.reps,

            "accuracy": accuracy,

            "calories": calories,

            "status": status,

            "tips": tips

        }