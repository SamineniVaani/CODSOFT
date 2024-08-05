def calculator():
    # Prompt the user to input the first number
    num1 = float(input("Enter the first number: "))

    # Prompt the user to input the second number
    num2 = float(input("Enter the second number: "))

    # Prompt the user to choose an operation
    operation = input("Choose an operation (+, -, *, /): ")

    # Perform the calculation based on the operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero is not allowed."
    else:
        result = "Error: Invalid operation."

    # Display the result
    print(f"The result is: {result}")

# Call the calculator function to run the program
calculator()
