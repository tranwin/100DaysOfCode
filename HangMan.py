# Step 1: Create the list
word_list = ["lord", "bring", "king", "new"]

# Step 2: Randomly choose words from the list
import random

chosen_word = random.choice(word_list)

# Step 3: Ask the user to guess the words
guess = input("Guess a letter:").lower()

# Step 4: Check if the guess word is one of the letter in the chosen_word
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Left")