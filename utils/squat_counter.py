from utils.angle_utils import calculate_angle


class SquatCounter:

    def __init__(self):

        self.reps = 0
        self.stage = "UP"
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

       

        # ---------------------------------
        # Left Leg
        # ---------------------------------

        left_hip = [
            landmarks[23].x,
            landmarks[23].y
        ]

        left_knee = [
            landmarks[25].x,
            landmarks[25].y
        ]

        left_ankle = [
            landmarks[27].x,
            landmarks[27].y
        ]

        # ---------------------------------
        # Right Leg
        # ---------------------------------

        right_hip = [
            landmarks[24].x,
            landmarks[24].y
        ]

        right_knee = [
            landmarks[26].x,
            landmarks[26].y
        ]

        right_ankle = [
            landmarks[28].x,
            landmarks[28].y
        ]

        # ---------------------------------
        # Knee Angles
        # ---------------------------------

        left_angle = calculate_angle(
            left_hip,
            left_knee,
            left_ankle
        )

        right_angle = calculate_angle(
            right_hip,
            right_knee,
            right_ankle
        )

        angle = (left_angle + right_angle) / 2

        # ---------------------------------
        # Squat Logic
        # ---------------------------------

        status = "🧍 Stand Straight"

        # Bottom Position
        if angle < 100:

            self.stage = "DOWN"

            status = "⬇ Good Depth"

        # Standing Again
        elif angle > 160 and self.stage == "DOWN":

            self.stage = "UP"

            self.reps += 1

            status = "✅ Excellent Rep"

        elif angle < 130:

            status = "⬇ Go Lower"

        elif angle < 160:

            status = "⬆ Almost There"

        else:

            status = "🧍 Stand Straight"

        # ---------------------------------
        # Accuracy
        # ---------------------------------

        if angle < 95:

            accuracy = 100

        elif angle < 105:

            accuracy = 98

        elif angle < 120:

            accuracy = 95

        elif angle < 140:

            accuracy = 90

        elif angle < 160:

            accuracy = 85

        else:

            accuracy = 80

        # ---------------------------------
        # Calories
        # ---------------------------------

        calories = round(self.reps * 0.5, 1)

        # ---------------------------------
        # AI Coaching Tips
        # ---------------------------------

        if status == "✅ Excellent Rep":

             tips = [

                 "Excellent squat technique.",

                 "Keep breathing steadily."

             ]

        elif status == "⬇ Good Depth":

            tips = [

                 "Perfect squat depth.",

                 "Keep your chest up."

             ]

        elif status == "⬇ Go Lower":

                 tips = [

                     "Bend your knees more.",

                     "Push your hips backward."

                 ]

        elif status == "⬆ Almost There":

                 tips = [

                    "Go slightly lower.",

                     "Keep your heels on the ground."

                 ]

        elif status == "🧍 Stand Straight":

                 tips = [

                     "Stand fully upright.",

                     "Prepare for your next squat."

                 ]

        else:

                 tips = [

                     "Move farther from the camera.",

                     "Keep your full body visible."

                 ]
        return {

    "reps": self.reps,

    "accuracy": accuracy,

    "calories": calories,

    "status": status,

    "tips": tips

}         