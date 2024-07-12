# 3.5.1 - OOP Fundamentals - Jon Tokarz - July 12, 2024 - Employee Class

# Write an Employee class
class Employee:

    # With the following attributes : name and employee number
    def __init__(self, name, emp_number):
        self.name = name
        self.emp_number = emp_number

    # Get and set name and employee number
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_emp_number(self):
        return self.emp_number
    
    def set_emp_number(self, emp_number):
        self.emp_number = emp_number

# Create a subclass named ProductionWorker that inherits from Employee
class ProductionWorker(Employee):
    def __init__(self, name, emp_number, shift_number, hourly_pay_rate):
        super().__init__(name, emp_number)
        self.shift_number = shift_number
        self.hourly_pay_rate = hourly_pay_rate

    # Get and set methods for the shift_number and hourly_pay_rate
    def get_shift_number(self):
        return self.shift_number
    
    def set_shift_number(self, shift_number):
        self.shift_number = shift_number

    def get_hourly_pay_rate(self):
        return self.hourly_pay_rate
    
    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.hourly_pay_rate = hourly_pay_rate

    # Shift number - 1 for day, and 2 for night, else return a "Invalid Shift"
    def get_shift_name(self):
        if self.shift_number == 1:
            return "Day"
        elif self.shift_number == 2:
            return "Night"
        else:
            return "Invalid Shift"
    





# 3.5.1 - OOP Fundamentals - Jon Tokarz - July 12, 2024 - Employee Class