import os
import rano_dom # could not use random module -> change the name of random file to another name
# Step 1
# this way
import hangman_words
# or this way
# from hangman_words import word_lists | => does not need to you hangman_words.word_lists, word_lists instead of.

import hangman_stages


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# Display the logo of game
print(hangman_stages.logo)

# Random a word in list
chosen_word = rano_dom.choice(hangman_words.word_list)

# length of chosen word
word_length = len(chosen_word)

# State of game
end_of_game = False

# lives of person
lives = 6

# Saving word of guessing
display = []

# Replacing the chosen word to blanks
for _ in range(word_length):
    display += "_"  

# Display the blank word
# join all of elems of display into a string
print(f"{' '.join(display)}")

# Loop for game
while not end_of_game:
    # ask the user for guessing
    guess = input("Guess a letter: ").lower()

    clearConsole()

    # Replacing the word when guessing right
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    # Reducing lives when guessing wrong
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose - the word is {chosen_word}")

    

    # Checking whether user win or not
    if "_" not in display:
        end_of_game = True
        print("You win")
    
    # Display state of lives
    print(hangman_stages.stages[lives])
    print(f"{' '.join(display)}")
