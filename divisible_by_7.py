# 3.2 - Jon Tokarz - For Loops In Python - Assignment - Find Numbers Divisible By 7

# Use a for loop to iterate through the range of numbers from 1 to 300.
for i in range(1, 300):
 
# Inside the loop, use an if statement to check if a number is divisible by 7. To do this, use the modulus operator (%) and compare the remainder with 0.
    if i % 7 != 0:

# If a number is divisible by 7, print that number.
        continue
    print(i)

# Ensure your program outputs each qualifying number on a separate line.