
# higher_lower games

import random
from game_data import data

# data is an List of Dictionaries

print("Welcome to Higher - Lower Game")


def game():
    random_account_a = random.choice(data)
    print(f"pssssst A has {random_account_a['follower_count']}")
    random_account_a_followers = random_account_a['follower_count']

    random_account_b = random.choice(data)
    print(f"pssssst B has {random_account_b['follower_count']}")
    random_account_b_followers = random_account_b['follower_count']
    is_playing = True
    score = 0
    while is_playing:
        a_name = random_account_a["name"]
        a_description = random_account_a["description"]
        a_country = random_account_a["country"]
        print(f"A: {a_name}, {a_description}, from {a_country}")

        print(f"B: {random_account_b['name']}, {random_account_b['description']}, from {random_account_b['country']}")
        answer = input("Select the one you think has more followers on instagram:\n").lower()
        if random_account_a_followers > random_account_b_followers:
            if answer == "a":
                score += 1
                print(f"You are correct. Score: {score}")
                random_account_a = random_account_b
                random_account_a_followers = random_account_a['follower_count']

                random_account_b = random.choice(data)
                random_account_b_followers = random_account_b['follower_count']
            else:
                print(f"You are wrong. Score: {score}")
                is_playing = False
        else:
            if answer == "b":
                score += 1
                print(f"You are correct. Score: {score}")
                random_account_a = random_account_b
                random_account_a_followers = random_account_a['follower_count']

                random_account_b = random.choice(data)
                random_account_b_followers = random_account_b['follower_count']

            else:
                print(f"You are wrong. Score: {score}")
                is_playing = False


game()
