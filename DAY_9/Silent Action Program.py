import art



print(art.logo)

should_continue_bid = True

bid_dictionary = {}

while should_continue_bid:
    name = input("What is your name: ") 
    bid = int(input("What is you want to bid: $"))

    bid_dictionary[name] = bid

    add_bid_again = input("Are there any other bidders? Type 'yes or 'no'.\n") .lower()

    if add_bid_again == "no":
        should_continue_bid = False
        winner = ""
        highest_bid = 0

        for bid in bid_dictionary:
            if highest_bid < bid_dictionary[bid]:
                winner = bid
                highest_bid = bid_dictionary[bid]

        print(f"The winner is {winner} with a bid of ${highest_bid}")
    else:
        print("\n" * 100)
        