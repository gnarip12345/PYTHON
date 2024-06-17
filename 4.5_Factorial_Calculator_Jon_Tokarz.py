# 4.5 - Factorial Calculator - Jon Tokarz - June 16, 2024

# Define a function to calculate factorial recursively
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial(n-1)
    else:
        return n * factorial(n - 1)

# Define the main function
def main():
    try:
        # Prompt user for input
        n = int(input("Enter a non-negative integer to calculate its factorial: "))
        
        # Check if the input is non-negative
        if n < 0:
            print("Error: Please enter a non-negative integer.")
        else:
            # Calculate factorial using the factorial function
            result = factorial(n)
            # Print the result
            print(f"The factorial of {n} is {result}.")
    
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")

# Call the main function to run the program
if __name__ == "__main__":
    main()




    # 4.5 - Factorial Calculator - Jon Tokarz - June 16, 2024