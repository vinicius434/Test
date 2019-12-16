import Functions

print("Wellcome to Calculator\n")


print("That's a simple calculator.\nHe just have the functionalities\n")
print("+ Sum\n/ Division\n* Multiplication\n- Subtraction\n")


##Variables and operator
a = float(input("Enter the first number:\n"))

command = input("What operation do you want to do?\n")

b = float(input("Enter the second number:\n"))


if (command == '+'):
    print(f"{Functions.Sum(a, b)}")

elif (command == '-'):
    print(f"{Functions.Subtraction(a, b)}")

elif (command == '/'):
    print(f"{Functions.Division(a, b)}")

elif (command == '*'):
    print(f"{Functions.Multiplication(a, b)}")
