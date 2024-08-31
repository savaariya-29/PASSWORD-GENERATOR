import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the world of Mark Anthony,mame")
nr_letters = int(input(f"How many letters do you want in your password?\n"))
nr_symbols = int(input(f"How many symbols would you want password\n"))
nr_numbers = int(input(f"How many numbers would you want in your password?\n"))

password_list=[]
for char in range(0,nr_letters):
    password_list.append(random.choice(letters))

for i in range(0,nr_symbols):
    password_list.append(random.choice(symbols))

for i in range(0,nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password=""
for i in password_list:
    password+=i
print(f"Here is your password is :{password}")