# 1.1 - 1.2 - Number Guessing Game - Jon Tokarz - June 28, 2024

# Important a random number generator
import random

# The main function
def main():
    # Choosing a random number from the imported random
    actual_number = random.randint(1, 100)

    while True:
        try:
            #Asking the user for input
            guess = int(input("Enter your guess (between 1 and 100): "))

            # Determine the difference between the guess and the actual number
            difference = abs(guess - actual_number)

            # Hot and Cold spectrum result based on the difference
            if difference <= 5:
                print("Very Hot")
            elif difference <= 15:
                print("Hot")
            elif difference <= 25:
                print("Cool")
            else:
                print("Cold")

            # Congratulate if the guess is correct
            if guess == actual_number:
                print(f"En Fuego! {guess} is the right number!!!")
                break

        except ValueError:
            print("Invalid number. Please enter a number between 1 and 100.")

        


if __name__ == "__main__":
    main()




# 1.1 - 1.2 - Number Guessing Game - Jon Tokarz - June 28, 2024