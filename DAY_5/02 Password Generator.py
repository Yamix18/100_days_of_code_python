import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "\\", "|", ";", "<", ">", "/", "?", "~"]
# list_of_password = [letters, numbers, symbols]

print("Welcome to the Francis Password Generator!")
no_of_letters = int(input("How many letters would you like to add to your password? \n"))
no_of_numbers = int(input("How many numbers would you  like? \n"))
no_of_symbols = int(input("How many symbols would you like? \n"))

# Easy Level
# password = ""
# for char in range(0, no_of_letters):
#     password += random.choice(letters)

# for char in range(0, no_of_numbers):
#     password += random.choice(numbers)

# for char in range(0, no_of_symbols):
#     password += random.choice(symbols)
# print(f"Your password is: {password}")

#Hard Level
password_list = []
for char in range(0, no_of_letters):
    password_list.append(random.choice(letters))

for char in range(0, no_of_numbers):
    password_list.append(random.choice(numbers))

for char in range(0, no_of_symbols):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)

#Get to make a string the shuffle list.

final_password = ""
for char in password_list:
    final_password += char

print(f"Your password is {final_password}")