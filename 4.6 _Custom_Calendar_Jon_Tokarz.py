# 4.6 - Custom Calendar - Jon Tokarz - July 28,2024

# Start by importing calendar and datetime modules
import calendar
import datetime

# Program should be contained within a main function
def main():
    # Inside main(), get the current year using datetime.datetime.now().year
    current_year = datetime.datetime.now().year

    # Ask the user to enter their birth month and store it in a variable
    while True:
        try:
            birth_month = int(input("What is your birth month (as a number)? "))
            if 1<= birth_month <= 12:
                return birth_month
                break

            # Ensure your program can handle invalid inputs gracefully
            else:
                print("Month should be a number between 1 and 12.")
        except ValueError:
            print("Invalid input - Please enter a number between 1 and 12.")

    # Ask the calendar module to generate the calendar for the given month and year
    month_calendar = calendar.month(current_year, birth_month)
    month_name = calendar.month_name[birth_month]

    # Use Python's datetime module to find the current year

    #Print the calendar to the console in a readable format
    print(f"\nCalendar for {month_name} {current_year}:")
    print(month_calendar)

# Initiate if the script is being run as the main program
if __name__ == "__main__":
    main()




# 4.6 - Custom Calendar - Jon Tokarz - July 28,2024
