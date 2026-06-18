from art import logo
import random

SET_EASY_LEVEL = 10
SET_HARD_LEVEL = 5

def check_answer(user_guess, actual_num, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_num:
        print("Too high.")
        return turns - 1
    elif actual_num > user_guess:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_num}.")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if level == "easy":
        return SET_EASY_LEVEL
    else:
        return SET_HARD_LEVEL
    
def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_guess = random.randint(1, 100)   # choosing a random number between 1 to 100
    print(f"the number to guess is: {number_guess}")

    turns = set_difficulty()
    guess = 0

    while guess != number_guess:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess  a number
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, number_guess, turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
        elif guess != number_guess:
            print("Guess again.")
game()