from resources import MENU, resources
from art import logo

profit = 0

def rsc_chk(user_drink):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for resource in user_drink:
        if user_drink[resource] > user_drink[resource]:
            print("Sorry there is not enough water.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?:")) * 0.10
    total += int(input("how many nickels?:")) * 0.05
    total += int(input("how many pennies?:")) * 0.01
    return total

def is_transact_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(choice, item_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in item_ingredients:
        resources[item] -= item_ingredients[item]
    print(f"Here is your {choice} ☕️. Enjoy!")

print(logo)
is_on = True
while is_on:
    user_order = input("What would you like? (espresso/latte/cappuccino): ") .lower()
    if user_order == "off":
        is_on = False
    elif user_order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_order]
        if rsc_chk(drink["ingredients"]):
            payment = process_coins()
            if is_transact_successful(payment, drink["cost"]):
                make_coffee(user_order, drink["ingredients"])







