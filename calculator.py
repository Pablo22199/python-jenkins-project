
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
   
    if b == 0:
        return "Error: Division by zero"
    return a / b


num1 = float(input("Enter the first number: ")) 
num2 = float(input("Enter the second number: "))


print("\nChoose the operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter your choice (1/2/3/4): ")


if choice == '1':
    result = add(num1, num2)
    print(f"\nResult: {num1} + {num2} = {result}")

elif choice == '2':
    result = subtract(num1, num2)
    print(f"\nResult: {num1} - {num2} = {result}")

elif choice == '3':
    result = multiply(num1, num2)
    print(f"\nResult: {num1} * {num2} = {result}")

elif choice == '4':
    result = divide(num1, num2)
    print(f"\nResult: {num1} / {num2} = {result}")

else:
    print("\nInvalid input. Please choose from 1 to 4.")

'''
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

if __name__ == "__main__":
    print("Add: ", add(10, 5))
    print("Subtract: ", subtract(10, 5))
    print("Multiply: ", multiply(10, 5))
    print("Divide: ", divide(10, 5))
'''