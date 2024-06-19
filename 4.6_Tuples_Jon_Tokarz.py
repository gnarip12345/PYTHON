# 4.6 - Create and Use Tuples - Jon Tokarz - Assignment


# The main function
def main():
    # The main tuple as a list of the classes
    programming_classes = ('Intro to Python', 'Advanced Python', 'Database Essentials', 'Web Development Basics', 'Data Structures in Python', 'Web Design Fundamentals')

    # Printing a list of the classes in the tuple
    print("List of programming classes:")
    # Printing each of the courses in the tuple
    for course in programming_classes:
        print(course)

    # Assigning a local variable to the number of classes, and printing that variable/number
    num_classes = len(programming_classes)
    
    print(f"\nTotal number of classes: {num_classes}")




if __name__ == "__main__":
    main()




# 4.6 - Create and Use Tuples - Jon Tokarz - Assignment