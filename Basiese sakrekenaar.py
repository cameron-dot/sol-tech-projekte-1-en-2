# Basiese Sakrekenaar
# Hierdie program is 'n eenvoudige sakrekenaar wat basiese wiskundige operasies kan uitvoer.
# Dit kan twee getalle neem en die gebruiker toelaat om 'n operasie te kies: optel, aftrek, vermenigvuldig of deel.

def add(a, b):
    """Voeg twee getalle bymekaar."""
    return a + b

def subtract(a, b):
    """Trek die tweede getal van die eerste af."""
    return a - b

def multiply(a, b):
    """Vermenigvuldig twee getalle."""
    return a * b

def divide(a, b):
    """Deel die eerste getal deur die tweede."""
    if b == 0:
        return "Fout: Kan nie deur nul deel nie."
    return a / b

def clear_screen():
    """Maak die skerm skoon."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

# Hoofprogram
def main():
    sentinel = True # Sentinel variable to control the loop
    while sentinel:
        print("\nBasiese Sakrekenaar")
        print("Select an operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Clear Screen")
        print("6. Exit")

        choice = input("Enter your choice (1-6):")

        if choice == '6': # Exit the program
            print("Exiting the program, Goodbye!")
            sentinel = False
        elif choice == '5': # Clear the screen
            clear_screen()
        elif choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter the first number:"))
                num2 = float(input("Enter the second number:"))

                if choice == '1':
                    print(f"Result: {add(num1, num2)}")
                elif choice == '2':
                    print(f"Result: {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"Result: {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"Result: {divide(num1, num2)}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()





