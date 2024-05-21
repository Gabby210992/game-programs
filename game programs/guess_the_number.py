import random
import os
from guess_logo import logo
print(logo)
def guess_number():
    if difficulty_level == "easy":
        no_of_attempts = 10
    else:
        no_of_attempts = 5
    target_number = random.randint(1, 100)
    print(f"You have {no_of_attempts}, attempts left")
    guess = int(input("Guess a number: "))
    while no_of_attempts > 0:
        if guess == target_number:
            print(f"Great! You got it. The number is {target_number}.")
            no_of_attempts = 0 
        elif guess < target_number:
            print("Too low.")
        else:
            print("Too high.")
        if guess != target_number and no_of_attempts != 0:
            no_of_attempts -= 1
            if no_of_attempts == 0:
                print("You have ran out your attempts.")
            else:
                print(f"You have {no_of_attempts} attempts left")
                guess = int(input("Guess another number: "))
        elif guess != target_number:
            print("You have ran out of your attempts.")

print("Hi! Welcome to my Number Guessing game.")
print("I am thinking of a number between 1 and 100.")

while input("Do you want to play this game of guess the number? Type 'yes' to proceed: ").lower() == "yes":
    os.system("cls")
    difficulty_level = input("Choose a difficulty level: Type 'easy' or 'hard': ").lower()
    guess_number()
    