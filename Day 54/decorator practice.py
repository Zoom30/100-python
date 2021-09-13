def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)


print(calculate(calc_function=multiply, n1=6, n2=2))
