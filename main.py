def calculate_bmi(weight, height_cm):
    """
    Calculate the Body Mass Index (BMI) using the weight (in kilograms) and height (in centimeters).
    Formula: BMI = weight / ((height / 100) * (height / 100))
    """
    height_m = height_cm / 100  
    bmi = weight / (height_m ** 2)
    rounded_bmi = round(bmi, 2) 
    return rounded_bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def main():
    weight = float(input("Enter your weight in kilograms: "))
    height_cm = float(input("Enter your height in centimeters: "))

    bmi = calculate_bmi(weight, height_cm)
    print("Your BMI is:", bmi)
    
    bmi_category = interpret_bmi(bmi)
    print("You are classified as:", bmi_category)

if __name__ == "__main__":
    main()
