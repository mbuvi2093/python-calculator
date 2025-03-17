def calculator():
    """
    This function performs basic arithmetic operations in a loop.
    """
    print("Basic Arithmetic Calculator")
    print("----------------------------")

    while True:
        try:
            num1 = input("Enter the first number (or 'q' to quit): ")
            if num1.lower() == 'q':
                print("Exiting the calculator. Goodbye!")
                break
            num1 = float(num1)

            num2 = input("Enter the second number: ")
            num2 = float(num2)

            operation = input("Enter an operation (+, -, *, /): ")

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1/num2
            else:
                print("Invalid operation. Please enter +, -, *, or /.")
                continue

            print(f"{num1} {operation} {num2} = {result}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")

calculator()
