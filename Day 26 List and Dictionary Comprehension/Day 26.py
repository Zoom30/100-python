import math
import pandas
# ================================================================
# new_list = [new_item for item in list if test]
# new_dictionary = {new_key: new_value for item in list}
# new_dictionary2 = {new_key: new_value for (key, value) in dict.items()}
# new_dictionary3 = {new_key: new_value for (index, row) in dict.iterrows()}
# ================================================================

# number = [1, 2, 3]
# new_list = [n + 1 for n in number]
# print(new_list)

# ===================================================

# name = "Daniel"
# new_list = [letter for letter in name]
# print(new_list)

# ===================================================

# x = range(1, 5)
# new_list = [i * 2 for i in x]
# print(new_list)

# ===================================================

# names = ["Daniel", "Matiwos", "Joel", "Stesy", "Francy", "Saitama", "Madara", "Midoriya"]
# new_list = [item for item in names if item[0] == "M"]
# another_list = [item.upper() for item in names if len(item) <= 5]
# print(another_list)

# ==========================================================================

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆
#
# #Write your 1 line code 👇 below:
#
# squared_numbers = [int(math.pow(item, 2)) for item in numbers]
#
# #Write your code 👆 above:
#
# print(squared_numbers)

# ==========================================================================


# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above
#
# #Write your 1 line code 👇 below:
#
# result = [item for item in numbers if item % 2 == 0]
#
# #Write your code 👆 above:
#
# print(result)

# ==========================================================================

# with open("file1.txt") as file1:
#     contents_of_file1 = file1.readlines()
#     int_list_file1 = [int(item.strip("\n")) for item in contents_of_file1]
#
# with open("file2.txt") as file2:
#     contents_of_file2 = file2.readlines()
#     int_list_file2 = [int(item.strip("\n")) for item in contents_of_file2]
#
# result = [item for item in int_list_file1 if item in int_list_file2]
# print(result)

# ==========================================================================
# import random
#
# new_list = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_scores = {item: random.randint(1, 100) for item in new_list}
# print(students_scores)
#
# passed_students = {key: value for (key, value) in students_scores.items() if value > 50}
# print(passed_students)

#=================================================================================

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
#
# result = {item: len(item) for item in sentence.split()}
#
# print(result)

#=================================================================================

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
#
#
# # Write your code 👇 below:
#
# weather_f = {key: (value * 9/5) + 32 for (key, value) in weather_c.items()}
#
# print(weather_f)


#=================================================================================

student_dict = {
    "student": ["Daniel", "Matiwos", "Joel"],
    "scores": [56, 76, 98]
}
#
# # normal loop
# # for (key, value) in student_dict.items():
# #     print(key)
# #     print(value)
#
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
for (key, value) in student_data_frame.items():
    print(key)
for (index, row) in student_data_frame.iterrows():
    if row["student"] == "Daniel":
        print(row["scores"])
