import random
#from art import *

#==========================================================================================
# randomNumber = random.random() * 10
# if randomNumber > 5:
#     print(randomNumber - 5)
# else:
#     print(randomNumber)

#========================================================================
# number = random.randrange(10, 50)
# for n in range(10, number):
#     print (n)
# calorie_allocated = random.randrange(2100, 3300)
# print(calorie_allocated)
# if calorie_allocated >= 2500:
#     print("it is above 2.5k")
# else:
#     print("it is below 2.5k")


#========================================================================
# rock = 0
# paper = 1
# scissors = 2
# player_result = int(input("rock, paper, scissors: 0, 1 & 2 \n"))
# computer_result = random.randint(rock, scissors)
# if player_result == 0:
#     print("Player chose: ", tprint("ROCK"))
# elif player_result == 1:
#     print("Player chose: ", tprint("PAPER"))
# elif player_result == 2:
#     print("Player chose: ", tprint("SCISSORS"))
# else:
#     tprint("WRONG ENTRY")

# if computer_result == 0:
#     print("CPU chose: ", tprint("ROCK"))
# elif computer_result == 1:
#     print("CPU chose: ", tprint("PAPER"))
# else:
#     print("CPU chose: ", tprint("SCISSORS"))

# if player_result == 0:
#     if computer_result == 1:
#         print("CPU wins")
#     elif computer_result == 2:
#         print("Player wins")
#     else:
#         print("Draw")
# elif player_result == 1:
#     if computer_result == 0:
#         print("Player wins")
#     elif computer_result == 2:
#         print("CPU wins")
#     else:
#         print("Draw")
# elif player_result == 2:
#     if computer_result == 0:
#         print("CPU wins")
#     elif computer_result == 1:
#         print("Player wins")
#     else:
#         print("Draw")
# else:
#     print("You typed an invalid number, you lose!")

# if player_result == 0 and computer_result == 1:
#     print("CPU wins")
# elif player_result == 0 and computer_result == 2:
#     print("Player wins")
# elif player_result == 1 and computer_result == 0:


#========================================================================
head = 0
tail = 1
result = random.randint(head, tail)
if result == 0:
    print("it is head")
else:
    print("it is tail")

#========================================================================
# fruits = ["Cherry", "Apple", "Pear"]
# print(fruits[-1])
# print(fruits[len(fruits)-1])
# fruits.append("Banana")
# print(fruits)
# fruits.remove("Apple")
# fruits.extend(["Ananas", "Strawberries", "Apple"])

# print(fruits)
# details = {
#     "Address": "25 Marie Lloyd House",
#     "Name": "Daniel Ghebrat",
#     "Age": "22"
# }
#========================================================================
# list_of_names = input("Insert the names: \n")
# payer_list = list_of_names.split(", ")
# designated_payer = payer_list[random.randrange(0, len(payer_list)-1)]
# #OR
# designated_payer2 = random.choice(payer_list)
# print(designated_payer2, " is going to pay")
#========================================================================
# insertNo = input("where \n")
# splitted = list(insertNo)
# print(splitted)
# row1 = [" ", " ", " "]
# row2 = [" ", " ", " "] #3,2
# row3 = [" ", " ", " "]
# map = [row1, row2, row3]

# print(f"{row1}\n{row2}\n{row3}")

# position = input("Where do you want to put your treasure? \n")
# #we change the given int(s) to list
# location = list(position)
# print(location) #prints out list(array) of strings

# #isolating the values
# new_row_location = int(location[1]) - 1
# new_column_location = int(location[0]) - 1

# print(new_column_location, new_row_location)
# map[new_row_location][new_column_location] = "X"
# print(f"{row1}\n{row2}\n{row3}")




