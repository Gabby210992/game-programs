import random
from guess_logo import logo

print(logo)
print("Welcome to my Guessing Game.")
print("I am thinking of a number between 1 and 100.")
fixed_number = random.randint(1, 100)
print(fixed_number)
no_of_attempts = 5
while no_of_attempts > 0:
    guess = int(input("Guess a number: "))
    if guess == fixed_number:
        print(f"You got it. The number is {guess}.")
        no_of_attempts = 0
    elif guess > fixed_number:
        print("Too high.")
    elif guess < fixed_number:
        print("Too low.")

# def logic(a, b): 
#     if guess > fixed_num:
#         return "Too high."
#     elif guess < fixed_num:
#         return "Too low."
#     else: 
#         return f"You got it. The number is {guess}."
# attempts = 5
# fixed_num = random.randint(1, 100)
# guess = int(input("Guess a number:")) 
# result = logic(guess, fixed_num)
# print(result)
# def lopping(attempts):
#     while attempts > 0:
#         logic(attempts)
