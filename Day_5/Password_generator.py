import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = ""

# easy version

# for i in range(0, nr_letters):
#     # rand_index = random.randint(0, len(letters) - 1)
#     # password += letters[rand_index]
#     password += random.choice(letters)

# for i in range(0, nr_symbols):
#     # rand_index = random.randint(0, len(symbols) - 1)
#     # password += symbols[rand_index]
#     password += random.choice(symbols)

# for i in range(0, nr_numbers):
#     # rand_index = random.randint(0, len(numbers) - 1)
#     # password += numbers[rand_index]
#     password += random.choice(numbers)

# print(password)

# hard version
# total_len = nr_letters + nr_symbols + nr_numbers
# i = 0

# while (i < total_len):
#     rand_choice_char = random.randint(0, 2)
#     if rand_choice_char == 0 and nr_letters != 0:
#         password += random.choice(letters)
#         nr_letters -= 1
#     elif rand_choice_char == 1 and nr_symbols != 0:
#         password += random.choice(symbols)
#         nr_symbols -= 1
#     elif rand_choice_char == 2 and nr_numbers != 0:
#         password += random.choice(numbers)
#         nr_numbers -= 1
#     else:
#         i -= 1
    
#     i += 1

# print(password)

password_list = []

for i in range(0, nr_letters):
    password_list.append(random.choice(letters))

for i in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for i in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

for char in password_list:
    password += char

print(f"Your password is: {password}")