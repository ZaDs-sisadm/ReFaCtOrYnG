def calculate(num1, num2, operator):
    if operator == '+':
        return summa_of_two_nums(num1, num2)
    elif operator == '-':
        return subtraction_of_two_nums(num1, num2)
    elif operator == '*':
        return multiplication_of_two_nums(num1, num2)
    elif operator == '/':
        return division_of_two_nums(num1, num2)
    #Suggestion:Removal this part of conditional that could shrink this part only for calculation,not to deliberate about possible pitfalls
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

def main():
    num1, num2 = couple_nums_validation()
    operator = operator_logic_implementation()
    result = calculate(num1, num2, operator)
    print("Result:", result)


def operator_logic_implementation():
    operator = input("Enter operator (+, -, *, /): ")
    # Possible implementation of business logic
    return operator


def couple_nums_validation():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        exit()
    return num1, num2


if __name__ == "__main__":
    main()

