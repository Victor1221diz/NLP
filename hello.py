try:
    user_input = int(input("Enter an integer: "))
    print("You entered:", user_input)
except ValueError:
    print("Invalid input. Please enter an integer.")
