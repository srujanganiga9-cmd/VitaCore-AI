def calculate_bmi(weight, height):
    
    height = height / 100

    bmi = weight / (height * height)

    return round(bmi, 1)