import random 

print("You have three options to choose: Rock, Scissors or Paper!")

option = ["Rock", "Scissors", "Paper"]
your_choice = input("Please pick an option: Rock, Scissors or Paper \n").upper()
computer_choice = random.choice(option).upper()
print(f"you choose {your_choice}, and the computer choice is {computer_choice}")

if your_choice == computer_choice:
    print("There's a tie!")

elif your_choice == "ROCK" and computer_choice == "SCISSORS":
    print("Congratulations! You win.")

elif your_choice == "SCISSORS" and computer_choice == "PAPER":
    print("You are a genius! You win.")

elif your_choice == "PAPER" and computer_choice == "ROCK":
    print("You are a winner!")

else:
    print("OOPs! You loose, try again.")