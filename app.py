import random

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","#","$","%","(",")","*","+"]

print("Welcome to the Pypassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy version
# password = ''
# for letter in range(0, nr_letters):
#     password += random.choice(letters)

# for symbol in range(0, nr_symbols):
#     password += random.choice(symbols)

# for number in range(0, nr_numbers):
#     password += random.choice(numbers)

# print(f"Easy password: {password}")

#Hard random password
hard_password = ''
combined_list = []

for letter in range(0, nr_letters):
    combined_list.append(random.choice(letters))

for symbol in range(0, nr_symbols):
    combined_list += random.choice(symbols)

for number in range(0, nr_numbers):
    combined_list.append(random.choice(numbers))


random.shuffle(combined_list)
print(combined_list)

for char in combined_list:
    hard_password += char
print(f'Hard password: {hard_password}')


    


    
