# 4.1 - Generators, Iterators, and Closures - Jon Tokarz - July 18, 2024


# Define a generator function two_letter_combinations that takes a list of characters as an argument
# Use nested loops within the generator function to iterate of the list of characters.
def two_letter_combinations(characters):

    for char1 in characters:
        for char2 in characters:

            combo = char1 + char2

            yield combo

# Run if the script is being run as the main program
if __name__ == "__main__":
    main()

    # A sample list of characters
    char_list = ['a', 'e', 'i', 'o', 'u']

    # Using the generator function for the char_list
    combinations = two_letter_combinations(char_list)

    # Print the combo yield from the two_letter_combinations function
    for combo in combinations:
        print(combo)








# 4.1 - Generators, Iterators, and Closures - Jon Tokarz - July 18, 2024
