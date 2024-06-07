# 3.4 - Jon Tokarz - Lists Assignment - Step Counter For Each Day Of The Week - June 06, 2024

# creating a list of each day of the week 
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# ask for input of steps for each day
sunday_steps = int(input("How many steps did you take on Sunday?"))
monday_steps = int(input("How many steps did you take on Monday?"))
tuesday_steps = int(input("How many steps did you take on Tuesday?"))
wednesday_steps = int(input("How many steps did you take on Wednesday?"))
thursday_steps = int(input("How many steps did you take on Thursday?"))
friday_steps = int(input("How many steps did you take on Friday?"))
saturday_steps = int(input("How many steps did you take on Saturday?"))

# creating an empty line between input and printing
print()

# creating a list from the user input for number of steps
user_steps_list = [sunday_steps, monday_steps, tuesday_steps, wednesday_steps, thursday_steps, friday_steps, saturday_steps]

for i in range(len(days)):
# retrieving the day from the days list
    day = days[i]
# retrieving the steps from the steps list
    steps = user_steps_list[i]
# print the day and its number of steps from user input
    print(f"You took {steps} steps on {day}")


# calculate and display total steps for the week
total_steps = (sunday_steps + monday_steps + tuesday_steps + wednesday_steps + thursday_steps + friday_steps + saturday_steps)
print(f"\nTotal steps: ", total_steps)
# calculate and display average steps per day
average_steps = (total_steps / 7)
print(f"Average steps: ", average_steps)






# 3.4 - Jon Tokarz - Lists Assignment - Step Counter For Each Day Of The Week - June 06, 2024