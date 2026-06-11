import random
from hangman_words import word_list
from hangman_art import stages
import hangman_art


print(hangman_art.logo)
chosen_word = random.choice(word_list)
print(chosen_word)


game_over = False
correct_guess = []
lives = 6

while not game_over:
    guess = input("Guess a letter: "). lower()
    if guess in correct_guess:
        print(f"You've already guessed {guess}")

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter 
            correct_guess.append(guess)
        elif letter in correct_guess:
            display += letter
        else:
            display += "_"
    print(f"word to guess: {display}")
    print(stages[6 - lives])
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    
# if "_" is not in the display the game is over and the user has won
    if "_" not in display:
        game_over = True
        print("You win!")

# if the guess is not in the chosen_word
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f'****************************YOU LOSE! The word was "{chosen_word}" ****************************')

     

# print the hangman pic based on lives left
        # print(stages[6 - lives])


# TODO-1 Randomly choose a word from the word_list and assign it to a variable called chosen_word. 
# Then print it.

# TODO-2 Ask the user to guess a letter and assign their answer to a variable called guess. 
# Make guess lowercase.

# TODO-3 Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#  If it is, print "Right", otherwise print "Wrong".

# TODO-4 Create a "placeholder" with the same number of blanks as the letters in the chosen_word.
# TODO-5 Create a "display" that puts the guess letter in the right position and _ in the rest 
# of the string.
