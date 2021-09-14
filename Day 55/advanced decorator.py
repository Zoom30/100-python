# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False
#
#
# def check_login(function):
#     def wrapper_function(*args, **kwargs):
#         if args[0].is_logged_in:
#             function(args[0])
#     return wrapper_function
#
#
# @check_login
# def create_blog_post(user):
#     print(f"This is {user.name} post")
#
#
# p1 = User(name="Daniel")
# p1.is_logged_in = True
# create_blog_post(p1)

# Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapper(*args, **kwargs):
        x = function(args[0], args[1])
        return f"You called {function.__name__}{args} and it returned {x}"

    return wrapper


@logging_decorator
def add(n1, n2):
    return n1 + n2


# Use the decorator 👇

print(add(5, 4))
