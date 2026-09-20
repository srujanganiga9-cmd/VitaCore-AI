def calculate_calories(age, gender, height, weight):
    
    # BMR (Mifflin-St Jeor Equation)
    if gender == "Male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    # Default activity multiplier (Moderate)
    calories = bmr * 1.55

    return round(calories)


def calculate_protein(weight, goal):

    if goal == "Muscle Gain":
        return round(weight * 2)

    elif goal == "Weight Loss":
        return round(weight * 1.6)

    return round(weight * 1.2)