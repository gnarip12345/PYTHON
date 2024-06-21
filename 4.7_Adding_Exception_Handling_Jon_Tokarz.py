# 4.7 - Adding Exception Handling - Jon Tokarz - June 21, 2024



    
# Defining the function to square a number input
def square_number():
    # Adding a while true break to return an error if the number is not an integer
    while True:
        try:
            # Prompting for input of the number
            number = input("Enter a number to square: ")

            # Try to convert the input to an integer
            number = int(number)
            squared_number = number **2
            print(f"The square of {number} is {squared_number}.")
            break
        except ValueError:
            print("Error: Pleas enter a valid integer.")
            # Loops continues until a valid input is provided

# Prompting the square number function
square_number()













# 4.7 - Adding Exception Handling - Jon Tokarz - June 21, 2024