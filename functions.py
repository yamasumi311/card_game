import random
import time

from constant import numbers, suits


def scoring(result, my_score, co_score):
    if result == 'higher':
        my_score += 1
    elif result == 'lower':
        co_score += 1
    return my_score, co_score

def make_cards():
    number = random.choice(numbers)
    suit = random.choice(suits)
    card = number + '-' + suit
    return card

def create_deck(maisu, whoes):
    for i in range(maisu):
        whoes.append(make_cards())
    return whoes


def find_card_order(card1, card2):
    if card1 == card2:
        return 'same' #picked the same card
    cpos1 = card1[0: card1.find('-')] # Array slicing [start:end:step]
    cpos2 = card2[0: card2.find('-')]
    order1 = numbers.index(cpos1)
    order2 = numbers.index(cpos2)
    if order1 > order2:
        print("You won this turn!")
        return 'higher'
    elif order1 < order2:
        print("You lost this turn.")
        return 'lower'
    else: #same cardno but not same suit
        print("It's a tie!")
        return 'same'


def play_one_round(my_cards, co_cards, my_score, co_score, my_choice, co_choice):
    my_card, my_new_hand = pull_card_from_hand(my_cards, my_choice)
    print(f"You play [{my_card}].")
    print("\n")
    # computer's turn
    print("Computer's turn!")
    time.sleep(1)
    co_card, co_new_hand = pull_card_from_hand(co_cards, co_choice)
    print(f"Computer plays [{co_card}].")
    print("\n")
    time.sleep(1)
    my_score, co_score = compute_score_from_cards(my_card, co_card, my_score, co_score)
    print(f"Your score is: {my_score}")
    print(f"Computer's score is: {co_score}")
    return my_new_hand, co_new_hand, my_score, co_score



def pull_card_from_hand(cards, index):
    card = cards[index]
    del cards[index]
    return card, cards

def compute_score_from_cards(card1, card2, score1, score2):
    result = find_card_order(card1, card2)
    return scoring(result, score1, score2)


def end_game(my_score, co_score):
    print("----- Final score ----- ")
    print(f"Your score: {my_score}")
    print(f"Computer's score: {co_score}")
    if my_score > co_score:
        print("You won:) Conglatulation!")
    elif my_score < co_score:
        print("You lost :(")
    else:
        print("Tie!")




