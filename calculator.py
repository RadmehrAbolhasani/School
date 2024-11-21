# calculator.py

import math


def calculator():
    while True:
        print("\nSelect Operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (x^y)")
        print("6. Square Root (√x)")
        print("7. Factorial (x!)")
        print("8. Trigonometric Functions (sin, cos, tan)")
        print("9. Exit")

        choice = input("\nEnter your choice (1-9): ")

        if choice == "1":
            x, y = get_two_numbers()
            print(f"Result: {x} + {y} = {x + y}")

        elif choice == "2":
            x, y = get_two_numbers()
            print(f"Result: {x} - {y} = {x - y}")

        elif choice == "3":
            x, y = get_two_numbers()
            print(f"Result: {x} * {y} = {x * y}")

        elif choice == "4":
            x, y = get_two_numbers()
            if y == 0:
                print("Error: Division by zero is undefined!")
            else:
                print(f"Result: {x} / {y} = {x / y}")

        elif choice == "5":
            x, y = get_two_numbers()
            print(f"Result: {x} ^ {y} = {math.pow(x, y)}")

        elif choice == "6":
            x = get_one_number()
            if x < 0:
                print("Error: Cannot compute the square root of a negative number!")
            else:
                print(f"Result: √{x} = {math.sqrt(x)}")

        elif choice == "7":
            x = get_one_number()
            if x < 0 or not x.is_integer():
                print("Error: Factorial is only defined for non-negative integers!")
            else:
                print(f"Result: {int(x)}! = {math.factorial(int(x))}")

        elif choice == "8":
            print("\nSelect Trigonometric Function:")
            print("a. Sine (sin)")
            print("b. Cosine (cos)")
            print("c. Tangent (tan)")

            trig_choice = input("\nEnter your choice (a-c): ").lower()
            x = get_one_number()

            if trig_choice == "a":
                print(f"Result: sin({x}) = {math.sin(math.radians(x))}")
            elif trig_choice == "b":
                print(f"Result: cos({x}) = {math.cos(math.radians(x))}")
            elif trig_choice == "c":
                print(f"Result: tan({x}) = {math.tan(math.radians(x))}")
            else:
                print("Invalid choice for trigonometric function!")

        elif choice == "9":
            print("Exiting the calculator. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option.")


def get_two_numbers():
    """Prompt the user to enter two numbers."""
    try:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        return x, y
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return get_two_numbers()


def get_one_number():
    """Prompt the user to enter a single number."""
    try:
        x = float(input("Enter the number: "))
        return x
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        return get_one_number()


if __name__ == "__main__":
    calculator()
