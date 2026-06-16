from art import logo
import random

def deal_card():
    new_card = random.choice(cards)
    return new_card


play_game = True
ask_to_play =input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") .lower()

if ask_to_play == "y":
    play_game = True
else:
    play_game = False

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

players_cards = []
players_cards.append(deal_card())
players_cards.append(deal_card())

computer_card = []
computer_card.append(deal_card())
computer_card.append(deal_card())

while play_game:

    if sum(players_cards) <= 21:
        print(logo) 

        print(f"Your card: {players_cards}, current score: {sum(players_cards)}")
        print(f"Computer's first card: {computer_card[0]}")
        hit_or_not = input("Type 'y' to get another card, type 'n' to pass: ") .lower()

        if hit_or_not == "y":
            deal_card()
            players_cards.append(deal_card())

