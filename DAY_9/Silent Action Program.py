import art



print(art.logo)

should_continue_bid = True

bid_dictionary = {}

def find_highest_bid(final_dictionary_bid):
    winner = ""
    highest_bid = 0

    max(bid_dictionary)
    for bidder in bid_dictionary:
        if highest_bid < bid_dictionary[bidder]:
            winner = bidder
            highest_bid = bid_dictionary[bidder]

    print(f"The winner is {winner} with a bid of ${highest_bid}")


while should_continue_bid:
    name = input("What is your name: ") 
    bid = int(input("What is you want to bid: $"))

    bid_dictionary[name] = bid

    add_bid_again = input("Are there any other bidders? Type 'yes or 'no'.\n") .lower()

    if add_bid_again == "no":
        should_continue_bid = False
        find_highest_bid(final_dictionary_bid= bid_dictionary)
    else:
        print("\n" * 100)
        