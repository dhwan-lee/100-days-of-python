import secret_auction_art

print(secret_auction_art.logo)
should_continue = True
bids = {}


def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        if bidding_dictionary[bidder] > highest_bid:
            highest_bid = bidding_dictionary[bidder]
            winner = bidder
    
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

while should_continue:

    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))

    bids[name] = bid

    user_response = input("Are there any bidders? Type 'yes' or 'no'.\n").lower()

    if user_response == 'no':
        find_highest_bidder(bids)
        should_continue = False
    else:
        print("\n" * 20)
