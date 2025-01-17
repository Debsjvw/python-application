# greet_and_square.py

# Function to greet the user
def greet_user():
    name = input("What is your name? ")
    print(f"Hello, {name}! Welcome to the Python script.")

# Function to calculate the square of a number
def calculate_square():
    try:
        number = float(input("Enter a number to square: "))
        square = number ** 2
        print(f"The square of {number} is {square}.")
    except ValueError:
        print("That's not a valid number. Please enter a valid number.")

# Main function to control the flow of the application
def main():
    greet_user()  # Call function to greet the user
    calculate_square()  # Call function to calculate the square

# Entry point of the script
if __name__ == "__main__":
    main()  # Call the main function to start the program
