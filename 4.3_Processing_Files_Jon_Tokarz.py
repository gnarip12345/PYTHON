# 4.3 - Processing Files - Jon Tokarz - July 21, 2024

# Setting a main function
def main():
    total = 0.0
    count = 0
    try:
        # Open the sales_totals in read mode
        with open('sales_totals.txt', 'r') as file:
            # Read all the lines using a loop
            lines = file.readlines()

            # Processing each line
            for line in lines:
                try:
                # Strip the newline symbol and convert each line to a float
                number = float(line.strip())
                total += number
                count += 1
                # Format and display each number to two decimal places
                print(f"Number: {number:.2f}")
            # Add a Value Error for skipping a line
            except ValueError:
                print(f"Skipping invalid number: {line.strip()}")
            
        # Calculate the average per line
        if count > 0:
            average = total / count
        else:
            average = 0.0

        # Outside of the loop, format and display the Total, Count, and Average
        print(f"\nTotal: {total:.2f}")
        print(f"Count: {count}")
        print(f"Average: {average:.2f}")

    # Use Try and Except statements to handle the errors
    except FileNotFoundError:
        print("Error: File 'sales_totals.txt' not found.")
    except IOError:
        print("Error: Could not read from 'sales_total.txt'.")
    except Exception as e:
        print(f"Error: {e}")

# Run if the script is being run as the main program
if __name__ == "__main__":
    main()




# 4.3 - Processing Files - Jon Tokarz - July 21, 2024