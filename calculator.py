print("Hello, welcome to our simple calculator")

while True:
    num1 = int(input('Enter the first number: '))
    num2 = int(input("Enter the second number: "))
    operator = int(input("""Select a number:
1. +
2. -
3. /
4. *
5. //
6. %
7. pow
"""))

    result = None

    match operator:
        case 1:
            result = num1 + num2
        case 2:
            result = num1 - num2
        case 3:
            if num2 == 0:
                result = "Can't divide by zero"
            else:
                result = num1 / num2
        case 4:
            result = num1 * num2
        case 5:
            if num2 == 0:
                result = "Can't divide by zero"
            else:
                result = num1 // num2
        case 6:
            if num2 == 0:
                result = "Can't divide by zero"
            else:
                result = num1 % num2
        case 7:
            result = num1 ** num2
        case _:
            result = "Invalid number or operator"

    print(f"The result is: {result}")

    nt = input("Will you calculate again? (y/n): ")
    if nt.lower() == 'n':
        break