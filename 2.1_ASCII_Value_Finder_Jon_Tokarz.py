# 2.1 ASCII Value Finder - Jon Tokarz - June 28, 2024

# Defining a main function
def main():
    # Asking for user input
    user_input = input("Enter a character: ")
    
    # A loop that prompts when the input is incorrect
    while len(user_input) != 1:
        print("Please enter exactly one character.")
        user_input = input("Enter a character: ")

    # Displaying the results of the ascii value
    ascii_value = ord(user_input)
    print(f"The ASCII value of {user_input} is {ascii_value}")
    
    # Prompt again for the user
    main()

if __name__ == "__main__":
    main()













# 2.1 ASCII Value Finder - Jon Tokarz - June 28, 2024