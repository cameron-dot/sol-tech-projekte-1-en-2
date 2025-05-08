# POS wat hardloop in command line
# It alows users to add items to a list, display all the items 
# with their prices, and total.
# delete the output , and exit the program useing a sentinel variable.

# List to store items and their prices
items = []

# Function to add an item to the list
def add_item():
    # Prompt the user for item name and price
    name = input("Enter the item name:")
    try:
        price = float(input("Enter the item price:"))
        # Append the item as a tuple (name, price) to the list
        items.append((name, price))
        print(f"{name} has been added to the list.")
    except ValueError:
        print("Invalid price. Please enter a numeric value.")

# Function to disply all items and the total price
def display_items():
    if not items:
        print("No items in the list.")
        return
    total = 0
    print("\nItems in the list:")
    for name, price in items:
        print(f"{name} R{price:.2f}")
        total += price
    print("-------------")
    print(f"Total: R{total:.2f}\n")

# Function to clear all items from the list
def clear_items():
    items.clear()
    print("All items have been cleared.")

# Main function to run the POS system
def main():
    print("Welcome to the Point of Sale (POS) system!")
    print("Options: [1] Add Item  [2] Display Items  [3] Clear Items  [4] Exit")

    while True: # Sentinel-controlled loop
        try:
            choice = input("\nEnter your choice (1-4): ")
            if choice == '1':
                add_item()
            elif choice == '2':
                display_items()
            elif choice == '3':
                clear_items()
            elif choice == '4':
                print("Exiting the POS system. Goodbye!")
                break # Exit the loop
            else:
                print("Invalid choice. Please select a valid option (1-4).")
        except Exception as e:
            print(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()