import random
from stages import game_stages
 
word_list = ["gabriel", "esther", "glory"]
chosen_word = random.choice(word_list)

lives = 6
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: \n").lower()

    display = []
    for i in range(len(chosen_word)):
        display += "_"
    print(display)

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            
    print(display)


    if not guess in chosen_word:
        lives -= 1


        print(game_stages[len(game_stages)-lives])
        if lives == 0:
            end_of_game = True
            print("You loss!")

    if not "_" in display:
        end_of_game = True

        print("You won!")
 

