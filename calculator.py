def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):  
    return a * b
def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
def power(a,b):
    return a ** b
def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return a ** 0.5

print("Welcome to the calculator program!")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")     
print("4.DIVIDE")
print("5.POWER")
print("6.SQUARE ROOT")
print("7.EXIT")
while True:
    choice = input("Please select an operation (1-7): ")
    if choice == '7':
        print("Exiting the calculator program.")
        break
    if choice in ['1', '2', '3', '4', '5', '6']:
        try:
            num1 = float(input("Enter first number: "))
            if choice in ['1', '2', '3', '4']:
                num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == '1':
            print(f"The result is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result is: {multiply(num1, num2)}")
        elif choice == '4':
            try:
                print(f"The result is: {divide(num1, num2)}")
            except ValueError as e:
                print(e)
        elif choice == '5':
            print(f"The result is: {power(num1, num2)}")
        elif choice == '6':
            try:
                print(f"The result is: {square_root(num1)}")
            except ValueError as e:
                print(e)
    else:
        print("Invalid selection. Please choose a valid operation.")
