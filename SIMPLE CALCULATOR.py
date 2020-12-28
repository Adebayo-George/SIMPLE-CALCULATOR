# Displays operations to be performed
print("1. Add")
print("2. Subtract")
print("3. Multiplication")
print("4. Division")

# Ask user the operation they want to choose 
choice = input("Enter 1/2/3/4: ")

# This performs addition 
def Add(x,y,z):
    return x + y + z

# This performs subtraction
def Subtract(x, y, z):
    return x - y - z

# This performs multiplication
def Multiply( x, y, z):
    return  x * y * z

# This performs division
def Divide( x, y, z):
    return  x/y/z

# These ask user for values to be used in each operation
num = eval(input("Enter the first number: "))
num1 = eval(input("Enter the second number: "))
num2 = eval(input("Enter the third number: "))

# When choice is any of the operation from above, the operation is performed
# Hence the result is displayed
if choice == "1":
    print(num, "+", num1, "+", num2, "=", Add(num, num1, num2))
elif choice == "2":
    print(num, "-", num1, "-", num2, "=", Subtract(num, num1, num2))
elif choice == "3":
    print(num, "*", num1, "*", num2, "=", Multiply(num, num1, num2))
elif choice == "4":
    print(num, "/", num1, "/", num2, "=", Divide(num, num1, num2))

