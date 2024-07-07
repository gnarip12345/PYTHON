# 3.2 - Programming Your First Class - Jon Tokarz - July 7, 2024

# Class definition for a Person
class Person:

    # Creating an initializer of the object, the person information
    def __init__(self, name, address, age, phone):
        self.name = name
        self.address = address
        self.age = age
        self.phone = phone
    
    # Getter for the name 
    def get_name(self):
        return self.name
    
    # Getter for the address
    def get_address(self):
        return self.address
    
    # Getter for the age
    def get_age(self):
        return self.age
    
    # Getter for the phone number
    def get_phone(self):
        return self.phone
    
    # Setter for the name
    def set_name(self, name):
        self.name = name
    
    # Setter for the address
    def set_address(self, address):
        self.address = address
    
    # Setter for the age
    def set_age(self, age):
        self.age = age
    
    # Setter for the phone number
    def set_phone(self, phone):
        self.phone = phone

# Creating variables for 3 Sample people
person1 = Person("Aaron Rodgers", "100 Cheese Street, Wisconsin, USA", 30, "+15551002000")
person2 = Person("Frank Thomas", "200 Baseball Drive, Chicago, USA", 25, "+14442003000")
person3 = Person("Barry Bonds", "300 Giants Avenue, San Francisco, USA", 35, "+13331005000")

# Displaying the information for each sample person
print("Person 1:")
print("Name:", person1.get_name())
print("Address:", person1.get_address())
print("Age:", person1.get_age())
print("Phone:", person1.get_phone())
print()

print("Person 2:")
print("Name:", person2.get_name())
print("Address:", person2.get_address())
print("Age:", person2.get_age())
print("Phone:", person2.get_phone())
print()

print("Person 3:")
print("Name:", person3.get_name())
print("Address:", person3.get_address())
print("Age:", person3.get_age())
print("Phone:", person3.get_phone())





# 3.2 - Programming Your First Class - Jon Tokarz - July 7, 2024