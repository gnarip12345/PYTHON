# 3.6 - Custom Exception Creation - Jon Tokarz - July 14, 2024


# Define a new exception class named NotNumericError that inherits from the base Exception class
class NotNumericError(Exception):
    pass

# A function that prompts the user to input a number 
def main():
    while True:
        # Use the try-except-else-finally block
        # Try should contain a logic check to check if the input is a number
        try:
            user_input = input("Please enter a number: ")
            # Attempts to convert the input to a float
            number = float(user_input)

        # Except should catch NotNumericError and print an error message
        except ValueError:
            if not user_input.isnumeric():
                raise NotNumericError("Input is not numeric")
            else:
                print("Unexpected error: Input is numeric but failed to convert to float")
        except NotNumericError as e:
            print(f"Error: {e}")
        # Else should print a confirmation message if input is valid
        else:
            print(f"Input '{user_input}' is a valid number.")
        # Finally should print a message indicating end of the program
        finally:
            print("End of this iteration\n")


# Run if the script is being run as the main program
if __name__ == "__main__":
    main()







# 3.6 - Custom Exception Creation - Jon Tokarz - July 14, 2024