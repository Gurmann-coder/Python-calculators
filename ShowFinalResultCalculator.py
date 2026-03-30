check = True
inputList = []

try:
    n1 = int(input("Enter your first number:"))
except ValueError:
    print("Error: Please enter valid integers!")

inputList.append(n1)

while(check):
    op = input("Enter the operator you want to perform:")

    try:
        n2 = int(input("Enter your second number:"))
    except ValueError:
        print("Error: Please enter valid integers!")
        continue
    
    if op == '+':
        result = n1 + n2

    elif op == '-':
        result = n1 - n2

    elif op == '*':
        result = n1 * n2

    elif op == '/':
        if n2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            result = n1 / n2
    else:       
        print("Error: Invalid operator! Please use +, -, *, or /.")
        continue

    inputList.append(op)
    inputList.append(n2)
    n1 = result
    
    check = input("Do you want to continue (True/False [default: True]):")
    check = check == "" or check.lower() == "true"
        
print(f"{inputList} = {result}")
print("Thank you for using the calculator!")