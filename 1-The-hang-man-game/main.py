import random
from hangman_art import stages, logo
from hangman_word import word_list
from replit import clear

print(logo)
end_of_game = False
lives = len(stages) -1
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#print ("solution is:", chosen_word)

display =[] 
for _ in chosen_word:
    display += "_"

while not end_of_game:
    guess = input("Guess a letter:").lower()

    clear() # clear output between guesses
    if guess in display:
        print(f"You have already guessed {guess}")

# S Check if the guess word is one of the letter in the chosen_word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    print(f"{' '.join(display)}")
    
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
      
    
    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win")

    print(stages[lives])

    


   