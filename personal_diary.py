# 4.2 - Personal Diary - Jon Tokarz - July 21, 2024

import os

# Create this in a main function
def main():
    # Prompt the user to enter the current date and time, then a diary entry
    current_datetime = input("Enter the date and time (example '2024-01-01 12:30'): ")
    diary_entry = input("Enter your diary entry: ")

    #Open diary.txt in append mode using open()
    with open('diary/diary.txt', 'a') as diary_file:
        # Write date and time into the .txt file
        diary_file.write(current_datetime + '\n')
        # Write the diary entry into the .txt file
        diary_file.write(diary_entry + '\n')
        # Write a blank line after the entry to separate it from the others
        diary_file.write('\n')

# Run if the script is being run as the main program
if __name__ == "__main__":
    main()












# 4.2 - Personal Diary - Jon Tokarz - July 21, 2024