import random
from words import word_list #list of words that will be used in the game
from hangman_art import stages, logo

print(logo)
print("Im thinking of an animal...can you guess what it is?")
lives = 6 # variable set to 6 as thats how many gueses a user gets before they lose

chosen_word = random.choice(word_list) # choses a random word from the word list defined


placeholder = ""
word_length = len(chosen_word) # this line lets me set the range to the length of the random chosen word
for position in range(word_length):
    placeholder += "_" # will add a "_" to placeholder for every character of the word
print(placeholder)

game_over = False
correct_letters = [] # this will store the correct letters guessed ina  list, its outside the while loop because otherwise when the while loop repeats then the list will be wiped to 0.

while not game_over: # this is where the question 'guess a letter' will be looped and asked till game is over
    print(f"{lives}/6")
    guess = input("Guess a letter: ").lower() # asks the user to pick a random letter and converts it to lower case

    if guess in correct_letters:
        print(f"You've already guessed {guess}, try again")
    
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter # correct letter guessed is added to the display
            correct_letters.append(letter) # adds the correct letters guess to the list I made outside the while loop
        elif letter in correct_letters: # condition checks if the correct letter is in the 'correct_letters' list 
            display += letter # then displays all the letters saved in that list, the previous lines would not show all the letters guessed, would just shouw them one by one after each guess


        else:
            display += "_"
    print (display)


    if guess not in chosen_word:
        lives -= 1 # decreasing lives when the incorrect letter is inputted
        print(f"Letter {guess} is not in the chosen word, you lose a life")
        if lives == 0:
            game_over = True # game over when there are no more lives
            print (f"Game Over, the chosen word was {chosen_word}")
    


    if "_" not in display: # if no more underscores then it means the user has guessed all the letters, so they win
       game_over = True
       print("You win!")

    print(stages[lives]) # printing the ASCII art from 'stages' and decreasing lives as the user gets letters wrong

input("Press 'enter' to exit")