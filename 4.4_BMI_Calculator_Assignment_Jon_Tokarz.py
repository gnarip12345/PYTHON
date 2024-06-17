# 4.4 - BMI Calculator Assignment - Jon Tokarz - Scope - June 16, 204


# Convert inputs to metric units
pounds_to_kilograms = 0.453592
inches_to_meters = 0.0254

# A function that calculates BMI
def calculate_bmi(weight_pounds, height_inches):
    try:
        weight_kilograms = weight_pounds * pounds_to_kilograms

        height_meters = height_inches * inches_to_meters

        bmi = weight_kilograms / (height_meters * height_meters)

        return bmi
    
    # Error messages
    except ZeroDivisionError:
        print("Cannot be zero - Please enter a valid number.")
        return None
    except ValueError:
        print("Error - Please enter a valid number.")
        return None

# A function to determine the BMI category
def bmi_category(bmi):
    if bmi is None:
        return "Invalid input"
    elif bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    elif bmi >= 30:
        return "Obese"

    
# Main Function
def main():
    try:
        # Input from the user
        weight_pounds = float(input("What is your weight in pounds? "))
        height_inches = float(input("What is your height in inches? "))

        # Calculate BMI
        bmi = calculate_bmi(weight_pounds, height_inches)

        if bmi is not None:
            print(f"Your BMI is {bmi:.2f}")
            print(f"Your BMI Category is {bmi_category(bmi)}")

    except ValueError:
        print("Invalid input - Please enter a valid number.")
        return
    
if __name__ == "__main__":
    main()





# 4.4 - BMI Calculator Assignment - Jon Tokarz - Scope - June 16, 2024