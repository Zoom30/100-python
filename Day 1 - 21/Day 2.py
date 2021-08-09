# print("Daniel"[3])
#


# print("Welcome to the tip calculator")
# totalBill = input("What was the total bill? \n")
# noOfPeople = input("How many people to split the bill? \n")
# percentageTip = input("What percentage tip to give? \n")
# totalToPay = round(((float(100 + int(percentageTip)) * round(float(totalBill), 2)) / 100), 2)
# eachPays = round((totalToPay / float(noOfPeople)),2)

# print("Each to pay: £" + str("{:.2f}".format(eachPays)))

# num_char = len(input("what is your name: \n"))
#
# new_num_char = str(num_char)
# print("your name has " + str(num_char) + " characters")


# a = "123"
# print(80 + float(a))
# print(str(80) + a)

# num = input("Type a 2 digit number: \n")
# firstDigit = int(num[0])
# secondDigit = int(num[1])
# print(firstDigit + secondDigit)

# print(10**5)

#BMI calculator
# height = input("Please enter your height: \n")
# weight = input("Please enter your weight: \n")
# bmi = round((float(weight))/(float(height) ** 2), 2)
# int_bmi = int(bmi)
# print("Your BMI is: " + str(bmi))

# print(type(8 // 3))

# score = 0
# height = 1.74
# isWinning = True
# #f-String
# print(f"your score is {score} and height is {height} and you're winnning {isWinning}")

# age = input("What is your current age? \n")
# total_months = 90 * 12
# total_weeks = 90 * 52
# total_days = 90 * 365
#
# months = float(age) * 12
# weeks = float(age) * 52
# days = float(age) * 365
#
# rounded_month = round(months)
# rounded_week = round(weeks)
# rounded_day = round(days)
#
# remaining_months = total_months - rounded_month
# remaining_weeks = total_weeks - rounded_week
# remaining_days = total_days - rounded_day
# print(f"You have {remaining_days} days, {remaining_weeks} weeks or {remaining_months} months till 90 years")

import math
print(math.ceil(8/3))
score = 0 
print("score type is: ", type(score))
