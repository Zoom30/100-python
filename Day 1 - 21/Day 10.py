# def format_name(first_name, last_name):
#     if first_name == "" or last_name == "":
#         return "no valid entries"
#     else:
#         f_name = str(first_name).capitalize()
#         l_name = str(last_name).title()
#         return f"Welcome {f_name} {l_name}"
#
#
# print(format_name("", ""))
# ========================================================================

# def is_leap(year):
#     if year % 4 == 0 :
#         if year % 100 == 0 :
#             if year % 400 == 0 :
#                 print("it is leap year")
#                 return True
#             else :
#                 print("it is not leap year")
#                 return False
#         else :
#             print("it is leap year")
#             return True
#     else :
#         print("not leap year")
#         return False
#
#
# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) and month == 2:
#         return 29
#     else:
#         return month_days[month - 1]
#
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)
# ========================================================================

# Calculator

def add(n1: float, n2: float):
    sum_value = n1 + n2
    return sum_value


def subtract(n1: float, n2: float):
    difference_value = n1 - n2
    return difference_value


def multiply(n1: float, n2: float):
    product_value = n1 * n2
    return product_value


def divide(n1: float, n2: float):
    if n2 != 0:
        remainder_value = n1 / n2
        return remainder_value
    else:
        print("cannot divide by zero")
        return


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def print_operation_signs():
    for operator in operations:
        print(operator)


# is_calculating = True
# while is_calculating:
    #or
def calculator():

    num1 = float(input("What is the first number: "))
    print_operation_signs()
    operator = input("Pick an operation from above: ")

    num2 = float(input("What is the second number: "))
    op_function = operations[operator]
    temp_answer = op_function(num1, num2)
    print(f"{num1} {operator} {num2} = {temp_answer}")

    still_calculating = True
    while still_calculating:
        choice = input(f"Type 'y' to continue calculating with {temp_answer} or type 'n' to start new calculation: ")
        if choice == "y":
            num1 = temp_answer
            print_operation_signs()
            operator = input("Pick an operation from above: ")
            op_function = operations[operator]
            num3 = float(input("What is the second number: "))
            temp_answer = op_function(num1, num3)
            print(f"{num1} {operator} {num3} = {temp_answer}")
        else:
            still_calculating = False
            calculator()


calculator()

