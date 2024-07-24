# 4.5 - Birthday Calculator - July 24, 2024

# Importing datetime
from datetime import datetime

# Inside a main function
def main():
   
    print("\n\n")
    try:
        # Importing current date for calculating age
        today = datetime.today()
        # Input for birth-year
        birth_year = int(input("What year were you born?  "))
        # Input for birth- month
        month = int(input("What Month were you born (as a number. May would be 5)  "))
        # Input for birth-day
        day = int(input("What day of the month were you born?  "))

        # just need datetime not datetime.date

        # Calculating age from input and current datetime
        # because we imported datetime from datetime
        birthday = datetime(birth_year, month, day)
        print("Your birthday is: ")
        birthday_output = birthday.strftime("%Y-%m-%d")
        print(birthday_output) 

        delta = today - birthday
        print(f'Difference is {delta.days} days')
        delta_years = delta.days // 365.2425
       
        print(f'You are {delta_years} years old')
       
      
    except Exception as e:
        print(f"ooooops!!!:  {e}") 
        main()
main()






# 4.5 - Birthday Calculator - July 24, 2024