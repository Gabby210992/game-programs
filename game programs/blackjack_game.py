import random
import os
from black_jack_logo import logo

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Calculates the scores from the list of cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == 0:
        return "Blackjack! You win."
    elif computer_score == 0:
        return "Opponent got blackjack! You lose."
    elif user_score > 21:
        return "Oops! Burst, You lose."
    elif computer_score > 21:
        return "You win."
    elif user_score == computer_score:
        return "Push!"
    elif user_score > computer_score:
        return "======= You win ========"
    else:
        return "-------You lose -------"
    
def play_game():
    user_card = []
    computer_card = []
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    
    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"Your cards: {user_card}, your current score is: {user_score}")
        print(f"Computer's first card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score >= 21:
            is_game_over = True
            
        else: 
            deal_a_card = input("type 'y' to deal a card, 'n' to stay: ").lower()
            if deal_a_card == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"Your final hand is: {user_card}, and your final score is {user_score}")
    print(f"The computer's final score is: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play blackjack game? Type 'y' or 'n': ").lower() == "y":
    os.system('cls')
    print(logo)
    play_game()