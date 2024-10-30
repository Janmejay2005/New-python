a = int(input("Enter First number: "))
b = int(input("Enter Second number: "))
operator = input("Enter the operator ")

if operator == '+':
    print("Your answer is:",a + b)
elif operator == '-':
    print("Your answer is:",a - b)
elif operator == '*':
    print("Your answer is:",a * b)
elif operator == '/':
    print("Your answer is:",a / b)
else:
    print("Invalid operator")
