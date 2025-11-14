def get_number(prompt):
    """Safely get a number from the user."""
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_operator():
    """Get a valid operator from the user."""
    operators = {
        "1": "+",
        "2": "-",
        "3": "/",
        "4": "*",
        "5": "//",
        "6": "%",
        "7": "**",
        "+": "+",
        "-": "-",
        "/": "/",
        "*": "*",
        "//": "//",
        "%": "%",
        "**": "**",
    }

    print("""
Select an operator:
1. +
2. -
3. /
4. *
5. //
6. %
7. **
You may type the symbol directly, e.g., +, -, /, *, etc.
    """)

    while True:
        op = input("Enter operator: ").strip()
        if op in operators:
            return operators[op]
        else:
            print("Invalid operator. Try again.")


def calculate(num1, num2, operator):
    """Perform calculation with error handling."""
    try:
        return eval(f"{num1} {operator} {num2}")
    except Exception as e:
        return f"Error: {e}"


print("Welcome to Calculator Version 2 (Error-Proof Edition!)")

while True:
    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")
    operator = get_operator()

    result = calculate(num1, num2, operator)
    print(f"\nResult: {result}\n")

    again = input("Do you want to calculate again? (y/n): ").lower()
    if again == "n":
        print("Goodbye!")
        break
