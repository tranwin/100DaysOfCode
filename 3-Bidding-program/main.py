from art import logo
print(logo)

from replit import clear

bids = {}
new_bidder = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not new_bidder:
    name = input("Enter name of bidder: ")
    bid_price = int(input("Enter the bidding amount: $"))
    bids[name] = bid_price 
    result = input("Type 'yes' if there is more bidder. Otherwise type 'no'.\n")
    if result == "no":
        new_bidder = True
        find_highest_bidder(bids)
    elif result == "yes":
        clear()

