def calculate(num1, num2, operator):
    if operator == '+':
        return summa_of_two_nums(num1, num2)
    elif operator == '-':
        return subtraction_of_two_nums(num1, num2)
    elif operator == '*':
        return multiplication_of_two_nums(num1, num2)
    elif operator == '/':
        return division_of_two_nums(num1, num2)
    else:
        return "Invalid operator"


def division_of_two_nums(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    else:
        return num1 / num2


def summa_of_two_nums(num1, num2):
    return num1 + num2


def subtraction_of_two_nums(num1, num2):
    return num1 - num2


def multiplication_of_two_nums(num1, num2):
    return num1 * num2


try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()
    
operator = input("Enter operator (+, -, *, /): ")

result = calculate(num1, num2, operator)
print("Result:", result)
