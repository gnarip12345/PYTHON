# 2.6 - Flower List Manager - Jon Tokarz - July 3, 2024

# Defining the main function
def main():
    
    # Creating a blank list for the flower names
    flower_list = []
    
    # Prompting the user to enter a flower name - or type done
    print('Please enter a flower name (type "done" when finished):')
    # Putting the result into the flower list
    while True:
        flower = input().strip()

        # Break if done is typed
        if flower.lower() == "done":
            break
        flower_list.append(flower)
    
    # Sort the flower list
    flower_list.sort()
    
    # Print the sorted flower list with index numbers
    print("Sorted list of flowers:")

    for index, flower in enumerate(flower_list, start=1):
        print(f"{index}: {flower}")
    
    # Searching for a specific flower
    search_flower = input("\nEnter a flower to search: ").strip()
    
    # Setting the found variable to false
    found = False

    # If the flower is in the list, print the flower name
    for flower in flower_list:
        if flower.lower() == search_flower.lower():
            print(f"{search_flower} is found in the list.")
            found = True
            break

    # Otherwise print that the flower is not in the list
    if not found:
        print(f"{search_flower} is not found in the list.")
    
    # Access a specific flower by index number
    try:
        # Look up the flower by index in the list
        index = int(input("\nEnter the number of the flower to access: ")) - 1
        if 0 <= index < len(flower_list):
            print(f"Flower at index {index + 1} is: {flower_list[index]}")
        # An invalid message if the flower number is not within index range
        else:
            print("Invalid index. Please enter a number within the range.")
    # An error message for invalid number inputs and out of range
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except IndexError:
        print("Index out of range.")

# For running the main function
if __name__ == "__main__":
    main()





# 2.6 - Flower List Manager - Jon Tokarz - July 3, 2024