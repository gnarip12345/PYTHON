# 3.3 - Vet Office Pet System - Jon Tokarz - July 11, 2024

# Define a pet class
class Pet:

    # Creating private properties for each category with pet_type a default value as "Dog"
    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    # Getter and setter methods for all properties
    def get_owner_first_name(self):
        return self.__owner_first_name
    
    def get_owner_last_name(self):
        return self.__owner_last_name
    
    def get_pet_id(self):
        return self.__pet_id
    
    def get_pet_name(self):
        return self.__pet_name
    
    def get_pet_type(self):
        return self.__pet_type
    
    def set_owner_first_name(self, owner_first_name):
        self.__owner_first_name = owner_first_name

    def set_owner_last_name(self, owner_last_name):
        self.__owner_last_name = owner_last_name

    def set_pet_id(self, pet_id):
        self.__pet_id = pet_id

    def self_pet_name(self, pet_name):
        self.__pet_name = pet_name

    def set_pet_type(self, pet_type):
        self.__pet_type = pet_type

    # A class variable with the name of the veterinary office
    vet_name = "Sample Vet Office"

    # A display method to print all the details of the pet and owner
    def display_pet_info(self):
        print("Pet Information:")
        print(f"Owner: {self.__owner_first_name} {self.__owner_last_name}")
        print(f"Pet ID: {self.__pet_id}")
        print(f"Pet Name: {self.__pet_name}")
        print(f"Pet Type: {self.__pet_type}")
        print(f"Veterinary: {Pet.vet_name}")
        print("\n")

# Three pet objects with different details
pet1 = Pet("Aaron", "Rodgers", 1, "Cheese", "Mouse")
pet2 = Pet("Tom", "Brady", 2, "Patriot")
pet3 = Pet("Patrick", "Mahomes", 3, "Chief", "Horse")

# Using a setter method
pet2.set_pet_type("Bald Eagle")

# A function check_property to verify that a property exists in a pet object
def check_property(pet_obj, property_name):
    if hasattr(pet_obj, property_name):
        print(f"{property_name} exists for this pet.")
    else:
        print(f"{property_name} does not exist for this pet.")

# Use display_pet_info to print details for each pet
pet1.display_pet_info()
pet2.display_pet_info()
pet3.display_pet_info()

# Show examples of check_property being used on various properties and pets
print("Checking property existence: ")
check_property(pet1, "pet_name")
check_property(pet2, "owner_first_name")
check_property(pet2, "owner_last_name")




# 3.3 - Vet Office Pet System - Jon Tokarz - July 11, 2024