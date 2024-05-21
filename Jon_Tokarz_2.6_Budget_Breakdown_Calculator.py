# Jon Tokarz Lesson 2.6 Budget Breakdown Calculator
# May 21, 2024

#Getting inputs from the user about Monthly Budget Amounts
print("Welcome to the Budget Breakdown Calculator.")
housing_cost = float(input("Housing: "))
housing_cost = int(housing_cost)
utilities = float(input("Utilities: "))
utilities = int(utilities)
groceries = float(input("Groceries: "))
groceries = int(groceries)
transportation = float(input("Transportation: "))
transportation = int(transportation)
health_care = float(input("Health Care: "))
health_care = int(health_care)
personal_care = float(input("Personal Care: "))
personal_care = int(personal_care)
clothing = float(input("Clothing: "))
clothing = int(clothing)
debt = float(input("Debt: "))
debt = int(debt)


# Calculating a Total Expenses Amount from Inputs
total_expenses = int(housing_cost + utilities + groceries + transportation + health_care + personal_care + clothing + debt)

# Displaying Results
print("Total Expenses = " + str(total_expenses))

# Displaying Results of Percentages
print("Percentage Of Each Category: ")
housing_cost_percentage = float(housing_cost / total_expenses)
print(f"Housing Cost: " + str(housing_cost_percentage * 100) + "%")
utilities_percentage = float(utilities / total_expenses)
print(f"Utilities: " + str(utilities_percentage * 100) + "%")
groceries_percentage = float(groceries / total_expenses)
print(f"Groceries: " + str(groceries_percentage * 100) + "%")
transportation_percentage = float(transportation / total_expenses)
print(f"Transportation: " + str(transportation_percentage * 100) + "%")
health_care_percentage = float(health_care / total_expenses)
print(f"Health Care: " + str(health_care_percentage * 100) + "%")
personal_care_percentage = float(personal_care / total_expenses)
print(f"Personal Care: " + str(personal_care_percentage * 100) + "%")
clothing_percentage = float(clothing / total_expenses)
print(f"Clothing: " + str(clothing_percentage * 100) + "%")
debt_percentage = float(debt / total_expenses)
print(f"Debt: " + str(debt_percentage * 100) + "%")






