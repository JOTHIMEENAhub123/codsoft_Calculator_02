# Simple Calculator Program

print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter your choice (1/2/3/4) or 'q' to quit: ")

    if choice == 'q':
        break

    try:
        choice = int(choice)
    except ValueError:
        print("Invalid choice. Please enter a number (1-4) or 'q' to quit.")
        continue

    if choice < 1 or choice > 4:
        print("Invalid choice. Please enter a number (1-4) or 'q' to quit.")
        continue

    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        result = num1 + num2
    elif choice == 2:
        result = num1 - num2
    elif choice == 3:
        result = num1 * num2
    elif choice == 4:
        if num2 == 0:
            print("Error: Division by zero is not allowed")
            continue
        result = num1 / num2

    print("Result: ", result)