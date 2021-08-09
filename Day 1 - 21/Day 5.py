import math
import random

# for loop
# ========================================================================
# fruits = ["Apple", "Peach", "Pear"]
# for index in range(len(fruits)):
#     print(fruits[index], "Pie")
# ========================================================================
# student_heights = input("Input a list of student heights \n").split()
# for n in range(len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
# total = 0
# for height in student_heights:
#     total += height
# number_of_items = 0
# for _ in student_heights:
#     number_of_items += 1
# average = total / number_of_items
# print("Average height is ", math.ceil(average))

# heighest_score = 0
# for score in student_heights:
#     if score > heighest_score:
#         heighest_score = score
# print(heighest_score)

# max = 0
# for index in range(number_of_items):
#     if student_heights[index] > max:
#         max = student_heights[index]
# print("the heighest is ", max)
# ========================================================================
# total = 0
# for number in range(0, 101, 2):

#     total += number

# print(total)
# ========================================================================
# fizzbuzz
# say = "0"
# for n in range(1, 101):

#     if n % 5 == 0 and n % 3 == 0:
#         say = "FizzBuzz"
#         print(say, n)
#     else:

#         if n % 3 == 0:
#             say = "Fizz"
#             print(say, n)

#         else:
#             if n % 5 == 0:
#                 say = "Buzz"
#                 print(say, n)
#             else: 
#                 print(n)
# ========================================================================
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
total_password_size = nr_letters + nr_symbols + nr_numbers
letter_list = []

for n in range(0, nr_letters):
    letter_list.append(random.choice(letters))
print(letter_list)

symbol_list = []
for n in range(0, nr_symbols):
    symbol_list.append(random.choice(symbols))
print(symbol_list)

number_list = []
for n in range(0, nr_numbers):
    number_list.append(random.choice(numbers))
print(number_list)

password_list = letter_list + symbol_list + number_list
print(password_list)


def returnRandom():
    return random.random()


random.shuffle(password_list)
print("Password is: ", "".join(password_list))

# combination = []
# combination.extend([letter_list, number_list, symbol_list])
# print("".join(combination[0]))

# password = []
# for n in range(0, total_password_size):
#     password.append(combination[random.randint(0, len(combination)-1)][])

# letterPass = ["A", "B", "C"]
# numPass = ["1", "2", "3"]
# symbolPass = ["(", ")", "#"]
# combination = [letterPass, numPass, symbolPass]
# password =  []
# for n in range(0, 3):
#     password.append(combination[random.randint(0,2)][random.randint(0,2)])
# finalPassword = "".join(password)
# print(finalPassword)


# ========================================================================
# list = [1, 2, 3, 4]
# list.extend([7, 4, 5, 8])
# finalPassword = "".join(str(list))
# print(list)
