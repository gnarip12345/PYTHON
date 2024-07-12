# 3.5.1 - Second Script - main

from employee import ProductionWorker

# Prompt the user for each attribute's data
def main():
    print("Enter the following details of the Employee")
    print("----------------------------------------------")
    name = input("Enter Employee Name: ")
    emp_number = input("Enter Employee Number: ")
    pay_rate = float(input("Enter Pay Rate: "))
    shift_number = int(input("Enter Shift Number (1 for Day, 2 for Night): "))

    # Create an instance of ProductionWorker
    worker = ProductionWorker(name, emp_number, shift_number, pay_rate)

    # Display the data using object methods
    print("---------------------------------------")
    print("Details of Employee: ")
    print("---------------------------------------")
    print(f"Name: {worker.get_name()}")
    print(f"Employee Number: {worker.get_emp_number()}")
    print(f"Shift: {worker.get_shift_name()}")
    print(f"Pay Rate: {worker.get_hourly_pay_rate()}")

# To run the main function
if __name__ == "__main__":
    main()