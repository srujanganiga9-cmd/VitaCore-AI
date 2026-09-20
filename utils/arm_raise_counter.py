from utils.angle_utils import calculate_angle


class ArmRaiseCounter:

    def __init__(self):

        self.reps = 0
        self.stage = "DOWN"
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

       


        # ----------------------------------
        # Landmarks
        # ----------------------------------

        nose = landmarks[0]

        left_shoulder = landmarks[11]
        right_shoulder = landmarks[12]

        left_elbow = landmarks[13]
        right_elbow = landmarks[14]

        left_wrist = landmarks[15]
        right_wrist = landmarks[16]

        # ----------------------------------
        # Elbow Angles
        # ----------------------------------

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

        # ----------------------------------
        # Arm Positions
        # ----------------------------------

        # Arms at sides
        arms_down = (

            left_elbow.y > left_shoulder.y + 0.08 and
            right_elbow.y > right_shoulder.y + 0.08

        )

        # Halfway up
        almost_up = (

            left_elbow.y < left_shoulder.y - 0.10 and
            right_elbow.y < right_shoulder.y - 0.10

        )

        # Elbows reach head level
        arms_up = (

            left_elbow.y <= nose.y + 0.03 and
            right_elbow.y <= nose.y + 0.03

        )

        # ----------------------------------
        # Rep Counter
        # ----------------------------------

        if arms_down:

            self.stage = "DOWN"

            status = "⬇ Arms Down"

        elif almost_up and not arms_up:

            status = "🎯 Almost There"

        elif arms_up:

            if self.stage == "DOWN":

                self.stage = "UP"

                self.reps += 1

                status = "✅ Excellent Rep"

            else:

                status = "🙌 Hold Position"

        else:

            if self.stage == "DOWN":

                status = "🙌 Keep Raising"

            else:

                self.stage = "DOWN"

                status = "⬇ Lower Your Arms"

        # ----------------------------------
        # Accuracy
        # ----------------------------------

        if status == "✅ Excellent Rep":

            accuracy = 100

        elif status == "🙌 Hold Position":

            accuracy = 98

        elif status == "🎯 Almost There":

            accuracy = 95

        elif status == "🙌 Keep Raising":

            accuracy = 90

        elif status == "⬇ Arms Down":

            accuracy = 92

        else:

            accuracy = 85

        # ----------------------------------
        # Calories
        # ----------------------------------

        calories = round(self.reps * 0.3, 1)

        # ----------------------------------
        # AI Coaching Tips
        # ----------------------------------

        if status == "✅ Excellent Rep":

            tips = [

                "Excellent arm raise!",

                "Lower your arms slowly."

            ]

        elif status == "🙌 Hold Position":

            tips = [

                "Perfect position.",

                "Control the movement."

            ]

        elif status == "🎯 Almost There":

            tips = [

                "Raise a little higher.",

                "Bring your elbows to head level."

            ]

        elif status == "🙌 Keep Raising":

            tips = [

                "Lift both elbows together.",

                "Keep moving upward."

            ]

        elif status == "⬇ Arms Down":

            tips = [

                "Great starting position.",

                "Raise both arms together."

            ]

        elif status == "⬇ Lower Your Arms":

            tips = [

                "Lower completely.",

                "Prepare for your next repetition."

            ]

        else:

            tips = [

                "Keep your upper body visible.",

                "Face the camera."

            ]

        # ----------------------------------
        # Return Result
        # ----------------------------------

        return {

            "reps": self.reps,

            "accuracy": accuracy,

            "calories": calories,

            "status": status,

            "tips": tips

        }