from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer):
    """Checks and Returns the result of the guessed number and the actual answer"""
    if guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    else:
        print(f"You got it. The answer is {answer}")

def set_difficulty():
    """Prompts the user for a level and returns the difficulty level."""
    level = input("Choose difficulty level: ")
    if level == "easy":
       return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
     
print("Welcome to Guess the Number Game.")
print("I am thinking of a number between 1 and 100.")
answer = randint(1, 100)

turns = set_difficulty()

print(f"You have {turns} attempts remaining to guess the number.")
guess = int(input("Guess a number: "))

check_answer(guess, answer)