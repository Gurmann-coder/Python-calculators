
check = True
try:
            n1 = int(input("Enter your first number:"))
except ValueError:
            print("Error: Please enter valid integers!")
while(check):
        op = input("Enter the operator you want to perform:")
        try:
            n2 = int(input("Enter your second number:"))
        except ValueError:
            print("Error: Please enter valid integers!")
            continue
        
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
            continue


        n1 = result
        
        check = input("Do you want to continue (True/False):").lower() == "true"

print("Thank you for using the calculator!")