import random
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0

def game():
    #Choose a random number between 1 and 100
    print("Welcome to the Number Gussing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randrange(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    #Choose difficulty
    def set_difficulty():
        level = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if level == "easy":
            global turns
            return EASY_LEVEL_TURNS
        elif level == "hard":
            return HARD_LEVEL_TURNS
        else:
            print("Please only type 'easy' or 'hard'")

    turns = set_difficulty()
    

    #Check the guess
    def check_answer(guess, answer,turns):
        """checks answer against guess. Returns the number of turns remainintg."""
        if guess > answer:
            print("Too high.")
            return turns - 1
        elif guess < answer:
            print("Too low.")
            return turns - 1
        else: 
            print(f"Correct! The answer was {answer}.")

        #Track the attemmpt

    #Repeat if guess wrong
    guess = 0
    while guess != answer:
        #Guess a number
        guess = int(input("Pick a number: "))
        turns = check_answer(guess, answer, turns)

        print(f"You have {turns} attempts remaining to guess the number.")
        
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return

game()