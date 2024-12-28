import random
from art import logo

# Defining constants and variables
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_hand = []
user_hand = []

# Functions
def scoring():
    print(f"Your cards: {user_hand}, current score: {sum(user_hand)}")
    print(f"Computer's first card: {computer_hand[0]}")

def initiate():
    print(logo)

    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_game == "n":
        exit()
    computer_hand.clear()
    user_hand.clear()
    for item in range(2):
        computer_hand.append(random.choice(cards))
        user_hand.append(random.choice(cards))

    scoring()
    blackjack()

def draw():
    draw_another = input("Type 'y' to get another card, type 'n' to pass: ")
    if draw_another == 'y':
        user_hand.append(random.choice(cards))
        if sum(user_hand) > 21:
            for card in user_hand:
                if card == 11:
                    computer_hand[card] = 1
            if sum(user_hand) > 21:
                winner()
                print(f"You lose! The total value of your cards is {sum(user_hand)}")
        else:
            scoring()
            draw()
    elif draw_another == 'n':
        winner()

def close_computer_hand():
    while sum(computer_hand) < 17:
        computer_hand.append(random.choice(cards))
    if sum(computer_hand) > 21:
        for card in computer_hand:
            if card == 11:
                computer_hand[card] = 1

def blackjack():
    if computer_hand[0] + computer_hand[1] == 21:
        scoring()
        print("The computer won with a blackjack!")
        initiate()
    if user_hand[0] + user_hand[1] == 21:
        scoring()
        print("Blackjack! You won!")
        initiate()

def winner():
    close_computer_hand()
    if sum(user_hand) < 22:
        if sum(computer_hand) > 22:
            print(f"Your cards: {user_hand}, current score: {sum(user_hand)}")
            print(f"Computer's hand: {computer_hand}")
            print("You won!")
        elif sum(user_hand) > sum(computer_hand):
            print(f"Your cards: {user_hand}, current score: {sum(user_hand)}")
            print(f"Computer's hand: {computer_hand}")
            print("You won!")
        elif sum(user_hand) == sum(computer_hand):
            print(f"Your cards: {user_hand}, current score: {sum(user_hand)}")
            print(f"Computer's hand: {computer_hand}")
            print("It's a draw!")
        else:
            print(f"Your cards: {user_hand}, current score: {sum(user_hand)}")
            print(f"The computer won with hand {computer_hand}!")

initiate()
draw()
