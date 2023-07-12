import random
import time

from functions import scoring, find_card_order, create_deck, play_one_round, end_game

my_cards = [] # user's deck
co_cards = [] # computer's deck

my_score = 0
co_score = 0

# Rule
print("This game compares numbers of cards played in a round.")
print("Higher number wins and gives you one point.")
print("You can not use the card you have used")
print("In the end of game, the person who gets higher score wins!")
print("Let's get started!")
time.sleep(1)


# 1 ask user to choose maisu and reveal the deck
maisu = int(input('How many cards do you want to play?: '))
my_cards = create_deck(maisu, my_cards)
print(f"Your deck: {my_cards}")
co_cards = create_deck(maisu, co_cards)

def game(maisu, my_cards,co_cards,my_score,co_score):
    for i in range(maisu):
        print("\n")
        round = i + 1
        print(f"----- Round {round} -----")
        #  user's choice
        print('Which card do you want to play?')
        print(f"Your deck: {my_cards}")
        my_choice = int(input('Choose the index number: '))
        # computer's choice
        co_choice = random.randint(0, maisu - 1 - i)
        my_cards,co_cards,my_score,co_score = play_one_round(my_cards,co_cards,my_score,co_score, my_choice, co_choice)
        i = i + 1
        # display the cards left
    return my_score, co_score

my_score, co_score = game(maisu, my_cards,co_cards,my_score,co_score)

end_game(my_score, co_score)