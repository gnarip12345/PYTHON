# 2.4 - Book Title Sorter - Jon Tokarz - June 29, 2024




# Defining the main function
def main():

    # Creating an empty list for the book titles
    book_titles = []
    
    # Setting the count of the list to 0
    count = 0

    # Prompting the user to input a title up to 10, for in the list
    while count < 10:
        title = input(f"Enter book title {count + 1}: ")
        
        # Appending the input title for capitalization of each word
        title = title.strip().title()
        
        # Appending the title to the book title list
        book_titles.append(title)
        
        # Adding 1 to the count of titles for each one entered
        count += 1
    
    # Sorting the book title list alphabetically
    sorted_titles = sorted(book_titles)
    
    # Displaying the book title list after it has been sorted
    print("\nSorted list of book titles:")
    for title in sorted_titles:
        print(title)

# Running the main function
if __name__ == "__main__":
    main()






# 2.4 - Book Title Sorter - Jon Tokarz - June 29, 2024