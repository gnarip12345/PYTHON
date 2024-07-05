# 2.7 - Handling List Exceptions - Jon Tokarz - July 5, 2024



# Defining the main function
def main():

    # Creating a list of the top artists
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    
    # Printing to display the top artists list
    print("Current top artists list:", top_artists)
    
    # Prompt for an input, replacing an arist name with a new one
    try:
        index = int(input("Enter the index of the artist to replace: "))
        new_artist = input("Enter the new artist name: ")
        
        # Attempt to replace the artist at the given index
        top_artists[index] = new_artist
        
        # Displaying the new artist list that has been updated
        print("Updated list:", top_artists)
        
    # Displaying an error message if the arist name input is invalid    
    except (ValueError, IndexError):
        print("An input error occurred. Please enter a valid index and artist name.")

    # Re-prompt the user for input
    main()

# Running the main function
if __name__ == "__main__":
    main()



    # 2.7 - Handling List Exceptions - Jon Tokarz - July 5, 2024