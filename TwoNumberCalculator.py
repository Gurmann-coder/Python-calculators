try:
            n1 = int(input("Enter your first number:"))
except ValueError:
            print("Error: Please enter valid integers!")
op = input("Enter the operator you want to perform:")
try:
    n2 = int(input("Enter your second number:"))
except ValueError:
    print("Error: Please enter valid integers!")
    

if op == '+':
    result = n1 + n2
    print(f"{n1} + {n2} = {result}")

elif op == '-':
    result = n1 - n2
    print(f"{n1} - {n2} = {result}")

elif op == '*':
    result = n1 * n2
    print(f"{n1} x {n2} = {result}")

elif op == '/':
    if n2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        result = n1 / n2
        print(f"{n1} ÷ {n2} = {result}")
else:       
    print("Error: Invalid operator! Please use +, -, *, or /.")

print("Thank you for using the calculator!")