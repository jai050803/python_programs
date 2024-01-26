from replit import clear

bidding_value = {}
def highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
print("\n....Welcome to the secret auction program.....\n")

bids = {}
repeat = True
while repeat:
    name = input("Enter your name :")
    bid_price = int(input("Enter your bid :"))

    bids[name] = bid_price
    ask = input("Is there any other who want to bid (yes/no) ?").lower()
    if ask == "no":
        repeat = False
    else:
        clear()
highest_bid(bids)
        
    