# 3.4 Pet Class Creation - Jon Tokarz - July 12, 2024

# Defining a pet class
class Pet:
    # Initialize function with attributes: kind, breed, and name
    def __init__(self, kind, breed, name):
        self.__kind = kind
        self.__breed = breed
        self.__name = name

    # Getter methods
    def get_kind(self):
        return self.__kind
    
    def get_breed(self):
        return self.__breed
    
    def get_name(self):
        return self.__name

    # Setter methods
    def set_kind(self, kind):
        self.__kind = kind

    def set_breed(self, breed):
        self.__breed = breed
    
    def set_name(self, name):
        self.__name = name

    # Add a method for printing the details of the pet called print_details
    def print_details(self):
        print(f"Pet Details:")
        print(f"Kind: {self.__kind}")
        print(f"Breed: {self.__breed}")
        print(f"Name: {self.__name}")
        print("-------------------------")

# Three Objects of the Pet class with different kinds, breeds, and names
pet1 = Pet("Dog", "Beagle", "Sedona")
pet2 = Pet("Bird", "Toucan", "America")
pet3 = Pet("Horse", "Palomino", "Mane")

# Calling print_details method for each object created
pet1.print_details()
pet2.print_details()
pet3.print_details()

# Demonstrating a special method or function

# Display the name of the class using __name__
print(f"Class name: {Pet.__name__}")









# 3.4 Pet Class Creation - Jon Tokarz - July 12, 2024