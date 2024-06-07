# 3.5 - Jon Tokarz - Bubble List Assignment - June 07, 2024

# accept five names from the user
first_name = input("What is the first name?")
second_name = input("What is the second name?")
third_name = input("What is the third name?")
fourth_name = input("What is the fourth name?")
fifth_name = input("What is the fifth name?")

# list each of the names in the order they were entered
print(first_name, second_name, third_name, fourth_name, fifth_name)

# creating a list of the names
name_list = [first_name, second_name, third_name, fourth_name, fifth_name]

# flag to see if a swap has occurred
swapped = True

# making all names lower-case
for i in range(0, len(name_list)):
    name_list[i] = name_list[i].lower()

# continuing looping until no swaps occur
while swapped:
    swapped = False # reset the flag at the start of each iteration
    for i in range(len(name_list) - 1):
        if name_list[i] > name_list[i + 1]: # compare adjacent elements
            swapped = True                  # a swap is needed

            name_list[i], name_list[i + 1] = name_list[i + 1], name_list[i]  # swap the elements

# print the sorted list
print(name_list)

# reverse the list
name_list.reverse()

# print the reversed list
print(name_list)
    




# 3.5 - Jon Tokarz - Bubble List Assignment - June 07, 2024