# 1. Define The Main Menu Function

def main_menu():
    print("Menu:")
    while True:
        try:
            print("\n\nWelcome! You can create new email entries, change email addresses, delete entries, or display entries.")
            print("1. Create a new entry")
            print("2. Display an entry by last name")
            print("3. Update an existing entry")
            print("4. Remove an entry")
            print("5. Quit")
            choice = int(input("Please enter the number of your selection: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("That is not a valid number. Try again.")
        except ValueError:
            print("That is not a valid number. Try again.")


# 2. Create The Placeholder Functions

def check():
    print("Checking the system...")

def create():
    print("Creating a new entry...")

def read():
    print("Reading an entry...")

def update():
    print("Updating an entry...")

def delete():
    print("Deleting an entry...")



# 3. Develop The Check Function

def check():
    try:
        with open("customer_list.txt", 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print("Customer list does not exist. Creating a new file...")
        return []
    

# 4. Implement Create And Save Functions

def create():
    customer = check()
    fname = input("Please enter the customer\'s first name: ")
    lname = input("Please enter the customer\'s last name: ")
    phone = input("Please enter the customer\'s phone: ")
    email = input("Please enter the customer\'s email: ")
    entry = f"{fname}, {lname}, {phone}, {email}\n"
    customer.append(entry)
    save(customer)

def save(output):
    with open("customer_list.txt", 'w') as file:
        file.writelines(output)
    print("File updated.")



# 5. Implement, Read, Delete, and Update Functions

def read():
    lname = input("Enter the last name to search for: ")
    customer = check()
    found = False
    for entry in customer:
        if entry.split(', ')[1] == lname:
            print(entry.strip())
            found = True
    if not found:
        print("No entry found with that last name.")



# Delete Function

def delete():
    lname = input("Enter the last name of the entry to delete: ")
    customer = check()
    new_customer = [entry for entry in customer if entry.split(', ')[1] != lname]
    if len(new_customer) < len(customer):
        save(new_customer)
        print("Entry deleted.")
    else:
        print("No entry found with that last name.")


# Update Function

def update():
    lname = input("Enter the last name of the entry to update: ")
    customer = check()
    updated_customer = []
    found = False
    for entry in customer:
        if entry.split(', ')[1] == lname:
            fname = input("Enter the new first name: ")
            phone = input("Enter the new phone: ")
            email = input("Enter the new email: ")
            updated_entry = f"{fname}, {lname}, {phone}, {email}\n"
            updated_customer.append(updated_entry)
            found = True
        else:
            updated_customer.append(entry)
    if found:
        save(updated_customer)
        print("Entry updated.")
    else:
        print("No entry found with that last name.")


# 6. Main Function

def main():
    while True:
        choice = main_menu()
        if choice == 1:
            create()
        elif choice == 2:
            read()
        elif choice == 3:
            update()
        elif choice == 4:
            delete()
        elif choice == 5:
            print("Quitting the program.")
            break

if __name__ == "__main__":
    main()




# Jon Tokarz - August 23, 2024