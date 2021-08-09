# blackjack rules
# 1. 2 cards are dealt at the start
# the value of 'ace' can be either 11 or 1 depending on the situations
# for example, if you have cards adding up to 10 or less, then the 'ace' can count as 11
# if you have cards adding up to 11 and more, then the 'ace' counts as 1
# the dealer must not have cards adding up to 16 or less. Needs to be more always
# if the player's cards exceed 21, then it's automatic loss, 'bust'
# if the player cards add up to 21 and the dealer is less than 21 or greater than 21, the it's a win for the player
# if the player has less than 21 and the dealer has more than the player and less than 21, dealer wins
# if both, the dealer and the player, have them same number at the end, it's a draw
#
import random

# decision_2 = True
# decision = input("Do you want to play blackjack, 'y' or 'n': ")
# start_of_game = True
# while decision_2:
#     def deal_card():
#         random_chosen_card = random.choice(card_deck)
#         return random_chosen_card
#
#
#     while start_of_game:
#         card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#
#         dealer_cards = []
#         dealer_sum = 0
#
#         player_cards = []
#         player_sum = 0
#
#         random_chosen_card = 0
#         index_of_random_card = 0
#
#         for x in range(2):
#             # dealer's cards
#             random_chosen_card = random.choice(card_deck)
#             index_of_random_card = card_deck.index(random_chosen_card)
#             if dealer_sum < 11:
#                 dealer_cards.append(random_chosen_card)
#                 dealer_sum += random_chosen_card
#             else:
#                 if index_of_random_card == 0:
#                     random_chosen_card = 1
#                     dealer_cards.append(random_chosen_card)
#                     dealer_sum += 1
#
#             # player's cards
#             random_chosen_card = random.choice(card_deck)
#             index_of_random_card = card_deck.index(random_chosen_card)
#             if player_sum < 11:
#                 player_cards.append(random_chosen_card)
#                 player_sum += random_chosen_card
#             else:
#                 if index_of_random_card == 0:
#                     random_chosen_card = 1
#                     player_cards.append(random_chosen_card)
#                     player_sum += 1
#
#         start_of_game = False
#         print(f"Dealer has {dealer_cards[0]}\nPlayer has {player_cards}")
#
#     if dealer_sum < 17 and not dealer_sum > 21:
#         new_card = deal_card()
#         if new_card == 11:
#             dealer_cards.append(1)
#             dealer_sum += 1
#         else:
#             dealer_cards.append(new_card)
#             dealer_sum += new_card
#
#     if player_sum < 21:
#         draw_or_not = input("Would you like to draw card: (y/n) ")
#         if draw_or_not == "y":
#             new_card = deal_card()
#             if new_card == 11 and player_sum > 10:
#                 player_cards.append(1)
#                 dealer_sum += 1
#             else:
#                 player_cards.append(new_card)
#                 player_sum += new_card
#         elif player_sum > dealer_sum:
#             print("PLAYER WINS")
#             decision_2 = False
#         elif player_sum < dealer_sum:
#             print("DEALER WINS")
#             decision_2 = False
#         elif player_sum == dealer_sum:
#             print("DRAW")
#             decision_2 = False
#     elif player_sum == 21:
#         if player_sum == dealer_sum:
#             print("DRAW")
#             decision_2 = False
#         else:
#             print("PLAYER WINS")
#             decision_2 = False
#
#     elif dealer_sum > 21 and player_sum < 22:
#         print("PLAYER WINS")
#         decision_2 = False
#     elif player_sum > 21:
#         print("DEALER WINS")
#         decision_2 = False
#
# print(f"Dealer has {dealer_cards} with a total of {dealer_sum}\nPlayer has {player_cards} with a total of {player_sum}")

# ------------------------------------------------------------

# Angela's Method
from art import logo_blackjack


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "DRAW"
    elif computer_score == 0:
        return "LOSE, OPPONENT HAS BLACKJACK"
    elif user_score == 0:
        return "WIN, WITH A BLACKJACK"
    elif user_score > 21:
        return "YOU WENT OVER, YOU LOSE"
    elif computer_score > 21:
        return "OPPONENT WENT OVER. YOU WIN"
    elif user_score > computer_score:
        return "YOU WIN"
    else:
        return "YOU LOSE"


def play_game():
    print(logo_blackjack)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        def calculate_score(cards):
            if sum(cards) == 21 and len(cards) == 21:
                return 0

            if 11 in cards and sum(cards) > 21:
                cards.remove(11)
                cards.append(1)
            return (sum(cards))

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(
            f"Player cards: {user_cards} and score is {user_score}\nComputer cards: {computer_cards} and score is {computer_score}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card or 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

    print(compare(user_score, computer_score))


while input("Do you want another game of blackjack: (y/n)") == "y":
    play_game()
