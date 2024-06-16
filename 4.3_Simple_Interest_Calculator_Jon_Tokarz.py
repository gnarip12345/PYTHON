# 4.3 - Simple Interest Calculator - Jon Tokarz - June 15, 2024

# Getting input to calculate the simple interest rate = (principal * rate * time / 100)
def calculate_interest(principal, rate, time):
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the interest rate as a whole number (5% would be 5): "))
    time = float(input("Enter the investment time in whole years: "))
    total = ((principal * rate * time)/100)
    print(f"\nThe simple interest for a principal amount of ${principal:.2f} \nat an interest rate of {rate:.2f}% \nover a period of {time} years \nis ${total:.2f}\n")
    return total 


calculate_interest(1, 1, 1)



# 4.3 - Simple Interest Calculator - Jon Tokarz - June 15, 2024
