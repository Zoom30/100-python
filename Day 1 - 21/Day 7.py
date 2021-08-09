import random
from hangman_words import word_list
from hangman_art import steps

# choosing random word from "word_list"
random_word = random.choice(word_list)

# creating "____" spaces for the random_word
blank_spaces = "_" * len(random_word)

# making blank spaces a list so that we can change the letters if the user guesses them right
list_blank_spaces = list(blank_spaces)
print(blank_spaces)
hint = random_word[0] + random_word[1]
print(hint)

total = 6
counter = 0
num_of_occurences = 0
all_guesses_correct = False
while counter < total and all_guesses_correct == False:
    guessed_letter = input("Guess a letter: \n").lower()

    for n in range(len(random_word)):
        if random_word[n] == guessed_letter:
            list_blank_spaces[n] = guessed_letter
            num_of_occurences += 1

    if num_of_occurences == 0:
        counter += 1
    num_of_occurences = 0
    if counter == 0:
        print(steps[counter])
    else:
        print(steps[counter])
    print("".join(list_blank_spaces))
    final_guess_result = "".join(list_blank_spaces)
    if final_guess_result == random_word:
        all_guesses_correct = True
        print("You win")
if not final_guess_result == random_word:
    print("It was", random_word)
    print("You lose")
# ========================================================================
# homies = ["Dani", "Mati", "Yuel"]
# if "Dani" in homies:
#     print("They're good")

# else:
#     print("No defense")
