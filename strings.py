# 2.2 - Strings Practice - Jon Tokarz - June 29, 2024

def main():
    # Example string
    example_string = "Hello, Python programmers!"

    # Iterate through the string and print each character
    print("Iterating through the string:")
    for char in example_string:
        print(char)

    # Find and print the character with the minimum ASCII value in the string
    min_char = min(example_string, key=ord)
    
    print("\nCharacter with the minimum ASCII value: ")
    print("'",min_char,"'")

    # Find and print the character with the maximum ASCII value in the string
    max_char = max(example_string, key=ord)

    print("\nCharacter with the maximum ASCII value:")
    print("'",max_char,"'")

    # Find and print the index of the first occurrence of 'o' in the string
    index = example_string.find('o')
    print("\nIndex of 'o':", index)

    # Convert the string into a list of characters and print the list
    char_list = list(example_string)
    print("\nConverting string to a list of characters:", char_list)

    # Count and print the number of occurrences of 'o' in the string
    count_o = example_string.count('o')
    print("\nCount of 'o' in the string:", count_o)

main()










# 2.2 - Strings Practice - Jon Tokarz - June 29, 2024