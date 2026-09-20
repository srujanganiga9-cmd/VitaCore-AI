from utils.angle_utils import calculate_angle


class ShoulderPressCounter:

    def __init__(self):

        self.reps = 0
        self.stage = "WAIT"
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

        left_elbow = landmarks[13]
        right_elbow = landmarks[14]

        left_wrist = landmarks[15]
        right_wrist = landmarks[16]

        # ----------------------------
        # Elbow Angles
        # ----------------------------

        left_angle = calculate_angle(
            [left_shoulder.x, left_shoulder.y],
            [left_elbow.x, left_elbow.y],
            [left_wrist.x, left_wrist.y]
        )

        right_angle = calculate_angle(
            [right_shoulder.x, right_shoulder.y],
            [right_elbow.x, right_elbow.y],
            [right_wrist.x, right_wrist.y]
        )

        avg_angle = (left_angle + right_angle) / 2

        # ----------------------------
        # Ready Position
        # ----------------------------

        elbows_at_shoulder = (

            abs(left_elbow.y - left_shoulder.y) < 0.08 and
            abs(right_elbow.y - right_shoulder.y) < 0.08

        )

        elbows_bent = (

            70 < left_angle < 110 and
            70 < right_angle < 110

        )

        ready = elbows_at_shoulder and elbows_bent

        # ----------------------------
        # Press Position
        # ----------------------------

        arms_up = (

            left_wrist.y < nose.y - 0.05 and
            right_wrist.y < nose.y - 0.05 and

            left_angle > 165 and
            right_angle > 165

        )

        # ----------------------------
        # Rep Counter
        # ----------------------------

        status = "💪 Bring Elbows to Shoulder Level"

        if ready:

            self.stage = "READY"

            status = "💪 Ready"

        elif arms_up and self.stage == "READY":

            self.stage = "UP"

            self.reps += 1

            status = "✅ Excellent Rep"

        elif self.stage == "UP":

            status = "⬇ Lower Slowly"

        # ----------------------------
        # Accuracy
        # ----------------------------

        if arms_up:

            accuracy = 100

        elif ready:

            accuracy = 95

        elif avg_angle > 130:

            accuracy = 90

        else:

            accuracy = 82

        # ----------------------------
        # Calories
        # ----------------------------

        calories = round(self.reps * 0.4, 1)

        # ----------------------------
        # AI Coaching Tips
        # ----------------------------

        if status == "✅ Excellent Rep":

            tips = [

                "Excellent shoulder press form.",

                "Fully extend your arms overhead."

            ]

        elif status == "💪 Ready":

            tips = [

                "Great starting position.",

                "Press upward in a controlled motion."

            ]

        elif status == "⬇ Lower Slowly":

            tips = [

                "Lower your arms slowly.",

                "Keep your elbows under control."

            ]

        else:

            tips = [

                "Bring your elbows to shoulder level.",

                "Keep your back straight."

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