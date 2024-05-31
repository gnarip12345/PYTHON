# 3.3 - Jon-Tokarz - Logical Operations Assignment - May 31, 2024

# Asking for user input for 2 numbers

first_number = int(input("What is the first number?"))
second_number = int(input("What is the second number?"))

# Printing the results for each number

print("Both numbers are greater than 0:")
if first_number > 0 and second_number > 0:
    print("True")
else:
    print("False")

print("Both numbers are less than 100:")
if first_number < 100 and second_number < 100:
    print("True")
else:
    print("False")

print("Both numbers are even:")
if first_number % 2 == 0 and second_number % 2 == 0:
    print("True")
else:
    print("False")

print("Either number is even:")
if first_number % 2 == 0 or second_number % 2 == 0:
    print("True")
else:
    print("False")

print("Both numbers aren't 0:")
if first_number != 0 and second_number != 0:
    print("True")
else:
    print("False")

print("The first number is greater than the second number:")
if not first_number <= second_number:
    print("True")
else:
    print("False")

