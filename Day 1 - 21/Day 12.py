# Guessing game
import random

easy_lives = 10
hard_lives = 5
random_number = random.randint(1, 100)
print("I am thinking a number between 1 and 100")
difficulty_choice = input("Choose a difficulty to get started: '(e)asy' or '(h)ard'\n")


def reduce_lives(number_of_lives):
    return number_of_lives - 1


def reset_lives():
    global easy_lives, hard_lives, random_number
    easy_lives = 10
    hard_lives = 5
    random_number = random.randint(1, 100)

is_playing = True
while is_playing:
    if difficulty_choice == "e":
        print(f"You have {easy_lives} attempts left to guess the number")
        guess = int(input("Make a guess: "))
        if guess != random_number:
            if guess > random_number:
                print("Your guess is too high: ")
                easy_lives = reduce_lives(easy_lives)
            elif guess < random_number:
                print("Your guess is too small: ")
                easy_lives = reduce_lives(easy_lives)
        else:
            print(f"You have correctly guessed the number, which is {random_number}")
            reset_lives()
            another_game = input("Do you want to keep playing: (y/n)\n")
            if another_game == "y":
                is_playing = True
                difficulty_choice = input("easy or hard")
            else:
                is_playing = False


        if easy_lives == 0:
            print(f"GAME OVER! The number was {random_number}")
            reset_lives()
            another_game = input("Do you want to keep playing: (y/n)\n")
            if another_game == "y":
                is_playing = True
                difficulty_choice = input("easy or hard")
            else:
                is_playing = False
    else:
        print(f"You have {hard_lives} attempts left to guess the number")
        guess = int(input("Make a guess: "))
        if guess != random_number:
            if guess > random_number:
                print("Your guess is too high: ")
                hard_lives = reduce_lives(hard_lives)
            elif guess < random_number:
                print("Your guess is too small: ")
                hard_lives = reduce_lives(hard_lives)
        else:
            print(f"You have correctly guessed the number, which is {random_number}")
            reset_lives()
            another_game = input("Do you want to keep playing: (y/n)\n")
            if another_game == "y":
                is_playing = True
                difficulty_choice = input("easy or hard")
            else:
                is_playing = False


        if hard_lives == 0:
            print(f"GAME OVER! The number was {random_number}")
            reset_lives()
            another_game = input("Do you want to keep playing: (y/n)\n")
            if another_game == "y":
                is_playing = True
                difficulty_choice = input("easy or hard")
            else:
                is_playing = False

# ================================================================================================

# Angela's Method

# from random import randint

# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5


# # Function to check user's guess against actual answer.
# def check_answer(guess, answer, turns):
#     """checks answer against guess. Returns the number of turns remaining."""
#     if guess > answer:
#         print("Too high.")
#         return turns - 1
#     elif guess < answer:
#         print("Too low.")
#         return turns - 1
#     else:
#         print(f"You got it! The answer was {answer}.")


# # Make function to set difficulty.
# def set_difficulty():
#     level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#     if level == "easy":
#         return EASY_LEVEL_TURNS
#     else:
#         return HARD_LEVEL_TURNS


# def game():
#     # Choosing a random number between 1 and 100.
#     print("Welcome to the Number Guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")
#     answer = randint(1, 100)
#     print(f"Pssst, the correct answer is {answer}")

#     turns = set_difficulty()
#     # Repeat the guessing functionality if they get it wrong.
#     guess = 0
#     while guess != answer:
#         print(f"You have {turns} attempts remaining to guess the number.")

#         # Let the user guess a number.
#         guess = int(input("Make a guess: "))

#         # Track the number of turns and reduce by 1 if they get it wrong.
#         turns = check_answer(guess, answer, turns)
#         if turns == 0:
#             print("You've run out of guesses, you lose.")
#             return
#         elif guess != answer:
#             print("Guess again.")


# game()
