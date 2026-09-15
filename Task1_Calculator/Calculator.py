def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero!"
    return num1 / num2


while True:

    print("================================")
    print("       PYTHON CALCULATOR")
    print("================================")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = add(num1, num2)
        print("Result:", result)

    elif choice == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = subtract(num1, num2)
        print("Result:", result)

    elif choice == "3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = multiply(num1, num2)
        print("Result:", result)

    elif choice == "4":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = divide(num1, num2)
        print("Result:", result)

    elif choice == "5":
        print("Thank you for using Python Calculator!")
        break

    else:
        print("Invalid choice!")