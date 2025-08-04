def calculator():
    print("Simple Calculator")

    # Input numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Menu
    print("\nChoose operation:")
    print("1. + (Addition)")
    print("2. - (Subtraction)")
    print("3. * (Multiplication)")
    print("4. / (Division)")

    # Get user's choice
    operation = input("Enter operation (1/2/3/4): ")

    # Perform operation
    if operation == '1':
        print(f"\nResult: {num1} + {num2} = {num1 + num2}")
    elif operation == '2':
        print(f"\nResult: {num1} - {num2} = {num1 - num2}")
    elif operation == '3':
        print(f"\nResult: {num1} * {num2} = {num1 * num2}")
    elif operation == '4':
        if num2 != 0:
            print(f"\nResult: {num1} / {num2} = {num1 / num2}")
        else:
            print("\nError: Division by zero is not allowed.")
    else:
        print("\nInvalid operation selected.")

# Run the calculator
calculator()