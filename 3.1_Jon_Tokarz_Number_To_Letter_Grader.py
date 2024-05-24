#Prompt the input of a Number Grade from the user.
grade = int(input("What is the numeric grade out of 100?"))


#Evaluate to determine the Letter Grade.
if grade < 60:
    print("Your grade is an F.")
elif grade < 70:
    print("Your grade is a D.")
elif grade < 80:
    print("Your grade is a C.")
elif grade < 90:
    print("Your grade is a B.")
elif grade <= 100:
    print("Your grade is an A.")


# Jon Tokarz 3.1 Number to Letter Grade Converter - May 23, 2024