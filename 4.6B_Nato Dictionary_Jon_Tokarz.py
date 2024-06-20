# 4.6B - Nato Dictionary - Jon Tokarz - June 20, 2024



# Defining a function for creating a NATO phonetic alphabet
def create_nato_alphabet():
    nato_alphabet = {
        'A': 'Alpha',
        'B': 'Bravo',
        'C': 'Charlie',
        'D': 'Delta',
        'E': 'Echo',
        'F': 'Foxtrot',
        'G': 'Golf',
        'H': 'Hotel',
        'I': 'India',
        'J': 'Juliett',
        'K': 'Kilo',
        'L': 'Lima',
        'M': 'Mike',
        'N': 'November',
        'O': 'Oscar',
        'P': 'Papa',
        'Q': 'Quebec',
        'R': 'Romeo',
        'S': 'Sierra',
        'T': 'Tango',
        'U': 'Uniform',
        'V': 'Victor',
        'W': 'Whiskey',
        'X': 'X-ray',
        'Y': 'Yankee',
        'Z': 'Zulu'
    }
    # A return to the NATO alphabet
    return nato_alphabet

# The spelling program within a function
def phonetic_spelling(word, nato_alphabet):

    # Phonetic output as an empty list
    phonetic_output = []
    
    for char in word.upper():
    # Appending each character to a list as the NATO alphabet
        if char in nato_alphabet:
            phonetic_output.append(nato_alphabet[char])
        else:
            phonetic_output.append(char)
    return phonetic_output

# Defining a main function for running the NATO alphabet
def main():
    nato_dict = create_nato_alphabet()
    word = input("Enter a word: ")
    phonetic_output = phonetic_spelling(word, nato_dict)
    for phonetic_term in phonetic_output:
        print(phonetic_term)


# Prompting the main function
if __name__ == "__main__":
    main()













# 4.6B - Nato Dictionary - Jon Tokarz - June 20, 2024