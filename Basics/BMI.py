def check_bmi(weight, height):
    bmi = weight / (height ** 2)
    match bmi:
        case bmi if bmi < 18.5:
            return "Underweight"
        case bmi if 18.5 <= bmi < 25:
            return "Normal weight"
        case bmi if 25 <= bmi < 30:
            return "Overweight"
        case _:
            return "Obesity"

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
result = check_bmi(weight, height)
print(f"Your BMI category is: {result}")