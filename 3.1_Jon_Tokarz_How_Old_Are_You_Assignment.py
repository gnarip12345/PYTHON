# Ask the user how old they are.

age = int(input("How old are you?"))

# Check to see if the user can drive, vote, buy alcohol, or receive a senior discount.

if age >= 16:
    print("Old enough to drive.")
else:
    print("Not old enough to drive.")

if age >= 18:
    print("Old enough to vote.")
else:
    print("Not old enough to vote.")

if age >= 21:
    print("Old enough to buy alcohol.")
else:
    print("Not old enough to buy alcohol.")

if age >= 65:
    print("Old enough to receive a senior discount.")
else:
    print("Not old enough to receive a senior discount.")





# Jon Tokarz Lesson 3.1 May 23, 2024