

# print("Welcome to Dani's Theme Park")


# number = int(input("insert a number: \n"))
# if number % 2 == 0 :
#     print("number is even")
# else :
#     print("number is odd")#

# height = float(input("what is your height? \n"))
# bill = 0
# if height > 120 :
#     print("You Can Ride the Rollercoaster")
#     age = int(input("What is your age? \n"))


# ------------------------------------------------------------
# if age > 18 :
#     print("Pay £18")
# elif age <= 18 and age > 12 :
#     print("Pay 7")
# else :
#     print("Pay 5")
# ------------------------------------------------------------

#     if age < 12 : 
#         bill = 5

#     elif age <= 18 : 
#          bill = 7

#     else :
#         if age >= 45 and age <= 55 :
#             bill = 0
#         else :
#             bill = 18

#     wantsPhoto = input("Do you want pictures? (y/n) \n")


#     if wantsPhoto == "y" :
#         bill += 3
#         print(f"Your final bill is {bill}")

#     else :
#         print(f"Your final bill is {bill}")

# else :
#     print("You Can Not Right the Rollercoaster")


# height = float(input("What is your height? \n"))
# weight = float(input("What is your weight? \n"))
# bmi = round(weight / height ** 2, 2)

# #elif conditions comparing two values can be written based on the previous condition, so no need to add 'and' & 'or'#
# if bmi < 18.5 :
#     print("You are underweight, bmi: ", bmi)
# elif bmi >= 18.5 and bmi < 25 :
#     print("You are of normal weight, bmi: ", bmi)
# elif bmi >= 25 and bmi < 30 :
#     print("You are overweight, bmi: ", bmi)
# elif bmi >= 30 and bmi < 35 :
#     print("You are obese, bmi: ", bmi)
# else :
#     print("You are clinically obese")

# Leap Year Challenge
# year = int(input("Enter a year to see if it is leap year or not: \n"))

# if year % 4 == 0 :
#     if year % 100 == 0 :
#         if year % 400 == 0 :
#             print("it is leap year")
#         else :
#             print("it is not leap year")
#     else :
#         print("it is leap year")
# else :
#     print("not leap year")

# print('''
# ---------------------------
# | Welcome to trashy pizza |
# ---------------------------
# Small pizza : £15
# Medium pizza : £20
# Large pizza : £25

# Pepperoni for small pizza : +£2
# Pepperoni for medium or large pizza : +£3

# Extra cheese for any size pizza: +£1
# ''')
# total = 0
# size = input("What size pizza do you want? (S, M, L) \n")
# addPepperoni = input("Do you want pepperoni? (y/n) \n")
# extraCheese = input("Do you want extra cheese? (y/n) \n")

# if size == "S" :
#     total = 15
# elif size == "M" :
#     total = 20
# else :
#     total = 25

# if addPepperoni == "y" :
#     if size == "S" :
#         total += 2
#     else :
#         total += 3

# if extraCheese == "y" :
#     total += 1

# print("total is ", total)


# print("Welcome to trashy love calculator")
# yourName = input("What is your name? \n")
# theirName = input("What is their name? \n")
# combinedString = yourName + theirName
# lowerCaseString = combinedString.lower()
# t = lowerCaseString.count("t")
# r = lowerCaseString.count("r")
# u = lowerCaseString.count("u")
# e = lowerCaseString.count("e")
# true = t + r + u + e

# l = lowerCaseString.count("l")
# o = lowerCaseString.count("o")
# v = lowerCaseString.count("v")
# e = lowerCaseString.count("e")
# love = l + v + o + e

# love_score = str(true) + str(love)
# print(love_score)

# if (int(love_score) < 10) or (int(love_score) > 90):
#     print("cheesy stuff")
# else :
#     print("nah")

# print("Welcome to Treasure Island... find the damn treasure")
# decision_1 = input("left or right? \n").lower()
# if decision_1 == "right":
#     print("game over")
# else:
#     decision_2 = input("swim or wait? \n").lower()
#     if decision_2 == "swim":
#         print("game over")
#     else:
#         decision_3 = input("which door? (red, blue or yellow) \n").lower()
#         if decision_3 == "red" or decision_3 == "blue":
#             print("game over")
#         else:
#             print("You win")
