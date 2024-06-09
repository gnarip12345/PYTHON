# 3.6 - Jon Tokarz - Seat List Assignment - June 08, 2024

# list of numbers in the seat list
seat_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# show list of seats available and prompt for user input to choose a seat number
while seat_list:
    print("Seats Available: ", seat_list)
    seat = int(input("Enter the seat you would like to purchase and press Enter or type 0 if done: "))
    
# if the seat is in the list, remove it    
    if seat in seat_list:
        seat_list.remove(seat)
    
# Otherwise, tell the user that the seat is not available
    else:
        print("Seat is not in the list.")
    
# if 0 is pressed prompt the user to have a nice day
    if seat == 0:
        print("\n Thank you for your purchase. Have a nice day.\n")

# when the list is empty, show user that no seats are available
else:
    print("No more seats are available.")


# 3.6 - Jon Tokarz - Seat List Assignment - June 08, 2024