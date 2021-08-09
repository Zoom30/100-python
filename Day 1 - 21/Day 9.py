# random_dic = {
#     "Name": "Daniel",
#     "Age": 22,
#     "Address": "25 Marie Lloyd House",
#     "Human": True
# }
#
# #printing 'value' from a dictionary
# print(random_dic["Human"])
#
# #Adding an entry to a dictionary
# random_dic["Loop"] = True
# print(random_dic)

# #creating an empty dictionary
# random_dic2 = {}

# #Wiping a dictionary
# # random_dic = {}
# # print(random_dic)

# #changing a 'value' in dictionary
# random_dic["Name"] = "Dani"
# print(random_dic)

# for thing in random_dic:
#     print (random_dic[thing], "Yo")
# ========================================================================
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermion": 99,
#     "Draco": 74,
#     "Neville": 62
# }

# student_grades = {}
# for i in student_scores:

#     if student_scores[i] < 71 and student_scores[i] > 0:
#         student_grades[i] = "Fail"
#     elif student_scores[i] < 81:
#         student_grades[i] = "Acceptable"
#     elif student_scores[i] < 91:
#         student_grades[i] = "Exceeds expectation"
#     elif student_scores[i] >= 91 and student_scores[i] < 101:
#         student_grades[i] = "Outstanding"
#     else:
#         print("not valid score")

# print(student_grades)
# ========================================================================
# Nesting
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin"
# }

# #Nesting a List in a Dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"]
# }

# #Nesting a Dictionary in a Dictionary
# cities_visited = {
#     "France": {
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#         },
#     "Germany": {
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 12
#     }
# }

# #Nesting a Dictionary in a List
# cities_visited = [
#     {
#         "Country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     {
#         "Country": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 12
#     }
# ]
# print(cities_visited[0]["cities_visited"][2])
# ========================================================================
# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #to be added to the travel_log. 👇
# def add_new_country(country, times_visited, cities_visited):
#     #OR

#     # new_country = {}
#     # new_country["country"] = country
#     # new_country["visits"] = times_visited
#     # new_country["cities"] = cities_visited
#     # travel_log.append(new_country)


#     travel_log.append({
#         "country": country,
#         "visits": times_visited,
#         "cities": cities_visited
#         })


# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

# ========================================================================
# secret auction site
from art import logo_auction

print(logo_auction)
bidders_available = True
bids = []
while bidders_available:

    bidder_name = input("What is your name?: ")
    bidder_amount = float(input("What's your bid?: "))
    another_bidder = input("Yes or no (y / n)?: ").lower()


    def bidding_instant(name, amount):
        new_bid = {
            "name": name,
            "amount": amount
        }
        bids.append(new_bid)
        print("\033[H\033[J")


    bidding_instant(bidder_name, bidder_amount)
    if another_bidder == "n":
        bidders_available = False

max = 0
bidder = ""
for bid in bids:
    if bid["amount"] > max:
        max = bid["amount"]
        bidder = bid["name"]

print(f"max is {max} and the bidder is {bidder}")
