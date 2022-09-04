# Step 1: Create the list
word_list = ["lord", "bring", "king", "new"]

# Step 2: Randomly choose words from the list
import random

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print ("solution is:", chosen_word)

# Print out the number of letter in chosen_word
display =[] 
for _ in chosen_word:
    display += "_"
print(display)

# Step 3: Ask the user to guess the words
end_of_game = False

# The whole loop allows the user to guess multiple times

while not end_of_game:
    guess = input("Guess a letter:").lower()

# Step 4: Check if the guess word is one of the letter in the chosen_word
    for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")


   