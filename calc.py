def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return "Invalid operator"

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
operator = input("Enter operator (+, -, *, /): ")

result = calculate(num1, num2, operator)
print("Result:", result)
