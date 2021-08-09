import csv
import pandas
import math
import statistics

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
#
#
# print(temperature)

# ================================================================


# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)
#
# data_series = data["temp"].to_list()
# print(data_series)
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.day)
# print(data[data["day"] == "Monday"])
# print(data[data["temp"] == data["temp"].max()])
# ==============================================================================

# monday = data[data["day"] == "Monday"]
# monday_temp = float(monday["temp"])
# print(monday_temp * (9/5) + 32)


# ================================================================================

# dataframe from scratch

# data_dictionary = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# df = pandas.DataFrame.from_dict(data_dictionary)
# df.to_csv("new_data.csv")

# =================================================================================

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
# black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
# print(cinnamon_squirrel_count, gray_squirrel_count, black_squirrel_count)
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
# }
#
# df = pandas.DataFrame(data_dict)
# df_converted_to_csv = df.to_csv()
# print(df_converted_to_csv)

# =================================================================================

