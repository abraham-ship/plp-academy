# Basic calculator

num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
operator = input("please enter mathematical operation; [eg +, -, *, /]: ")
# Handling operators 
validOperator = [ "+", "-","/","*" ]
total = 0

if operator == "+":
    total = num1 + num2
elif operator == "-":
    total = num1 - num2
elif operator == "*":
    total = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("can't divide by zero")
    total = num1 / num2 
else:
    print("please enter a valid operator and try again!")   

print(num1, operator, num2, "=", total)