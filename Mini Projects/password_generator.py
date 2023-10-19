import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
letters_number = int(input("How many letters would you like in your password?\n"))
symbols_number = int(input("How many symbols would you like?\n"))
numbers_number = int(input("How many numbers would you like?\n"))

password_list = []
for i in range(letters_number):
    password_list.append(random.choice(letters))

for j in range(symbols_number):
    password_list.append(random.choice(symbols))

for k in range(numbers_number):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for symbol in password_list:
    password += symbol

print(f'Your password is {password}')
