# 2.5 - Password Validator - Jon Tokarz - June 30, 2024

# Importing the string constants module
import string

# Defining the main function
def main():
    while True:
        try:
            # Prompting the user to input a password
            password = input("Enter a password: ")
            
            # Checking the password variable for number of characters
            if (8 <= len(password) <= 20 and
                # Checking password variable for required upper case letter
                any(char.isupper() for char in password) and
                # Checking password variable for required lower case letter
                any(char.islower() for char in password) and
                # Checking password variable for required number digit
                any(char.isdigit() for char in password) and
                
                # Checking password variable for required punctuation
                any(char in string.punctuation for char in password)):
                
                # Prompt the user to confirm the password
                password_confirm = input("Confirm your password: ")
                
                # Compare the original with new password variable
                if password == password_confirm:
                # Prompt if the passwords are the same
                    print("Password set successfully!")
                    break
                # Prompt for re-try if the passwords do not match
                else:
                    print("Passwords do not match. Please try again.")
            # If the requirements aren't met, prompt to re-enter a new password
            else:
                print("Password must be between 8 to 20 characters long and include at least one uppercase letter, one lowercase letter, one number, and one symbol (!@#$%&*). Please try again.")
        
        # Error message if the original prompt does not initialize
        except Exception as e:
            print(f"An error occurred: {e}")
            continue

# Running the main function
if __name__ == "__main__":
    main()







    # 2.5 - Password Validator - Jon Tokarz - June 30, 2024