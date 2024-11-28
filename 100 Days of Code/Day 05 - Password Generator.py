import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

nr_password = nr_letters + nr_symbols + nr_numbers
password = []

for i in range(0, nr_letters):
    password.append(letters[random.randint(0, 26)])

for i in range(0, nr_numbers):
    password.append(numbers[random.randint(0, 9)])

for i in range(0, nr_symbols):
    password.append(symbols[random.randint(0, 8)])

random.shuffle(password)

password_string = ''
for i in password:
    password_string += i

print(f"Your password is: {password_string}")