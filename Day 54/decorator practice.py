# def add(n1, n2):
#     return n1 + n2
#
#
# def subtract(n1, n2):
#     return n1 - n2
#
#
# def multiply(n1, n2):
#     return n1 * n2
#
#
# def divide(n1, n2):
#     return n1 / n2
#
#
# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)


# print(calculate(calc_function=multiply, n1=6, n2=2))


# def outer_function():
#     print("I am outer")
#
#     def nested_function():
#         print("I am inner")


# def outer_function():
#     print("I am outer")
#
#     def nested_function():
#         print("I am inner")
#
#     return nested_function
#
#
# inner_function = outer_function()
# inner_function()

# Python decorator
import time

#
#
# def delay_decorator(another_func):
#     def wrapper_function():
#         time.sleep(2)
#         another_func()
#
#     return wrapper_function
#
#
# @delay_decorator
# def say_hello():
#     print("hello")
#
#
# @delay_decorator
# def say_bye():
#     print("bye")
#
#
# def say_greeting():
#     print("greeting")
#
#
# say_hello()
# say_bye()
# say_greeting()

# measuring the speed of a function

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        x = time.time()
        function()
        print(f"{function.__name__} executed in {time.time() - x} second")

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        var = i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        var = i * i


fast_function()
slow_function()
