

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

while True:
    print("\n1.Add  2.Subtract  3.Multiply  4.Divide  5.Exit")
    choice = input("Choose operation: ")

    if choice == "5":
        print("Exiting...")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", sub(num1, num2))
    elif choice == "3":
        print("Result:", mul(num1, num2))
    elif choice == "4":
        print("Result:", div(num1, num2))
    else:
        print("Invalid choice")
