from art import logo,vs
from game_data import data
import random
import os

# Displat visual arts
print(logo)
score = 0

def format_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return(f"{account_name}, a {account_descr}, from {account_country}")

def check_answer(guess, a_followers,b_followers):
    """Take the user guess and follower count and return they get it right"""
    if a_followers > b_followers:
        return guess == "a"
    else: 
        return guess == "b"

# Make the game repeatable
game_should_continue = True
account_b = random.choice(data) # choose a random account b so that in the future, account a can become account b

while game_should_continue:   
          
    # Generate a random account from the game data.
    account_a = account_b
    account_b = random.choice(data)

    # If account_a equals to account_b, regenerate account_b:
    # if account_a == account_b:
    #     account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")


    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
   
    # Check if user is correct.
    ## Get follower count.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct =check_answer(guess, a_follower_count, b_follower_count)

    # Clear the screen between rounds
    os.system('cls')
    print(logo)

    # Feedback and score keeping
    if is_correct:
        score += 1
        print(f"You are right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry you are wrong. Your score: {score}.")
        print("Try again!")

