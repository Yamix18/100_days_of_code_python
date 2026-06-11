import random
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

# Rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
# Paper
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# Scissors
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


nested_choice = [rock, paper, scissors]
if choice >= 0 and choice <=2:
    print(nested_choice[choice])

computer_choice = random.randint(0, 2)
final_choice = nested_choice[computer_choice]
if choice >= 0 and choice <=2:
    print(f"Computer chose: \n {final_choice}")
else: 
    print("")


if choice >= 3 or choice < 0:
    print("Yout type the invalid number!")
elif computer_choice == choice:
    print("It's a tie. Please try again!")
elif choice == 2 and computer_choice == 0:  
    print("You lose")
elif choice == 0 and computer_choice == 2:
    print("You win.")
elif computer_choice > choice:
    print("You lose.")
elif choice > computer_choice:
    print("You win.")
