import random

print("Welcome to the Password Generator.")

letters = int(input("Enter the no. of letters: "))
num = int(input("Enter the numbers: "))
sym = int(input("Enter the no. of symbols: "))

character = ['!', '@', '#', '$', '%', '&', '*']
number = ['1','2','3','4','5','6','7','8','8','9','0']
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

temp= []

alpha_uppercase = [char.upper() for char in alpha]

for i in range(letters):
    temp.append(random.choice(alpha_uppercase))

for i in range(num):
    temp.append(random.choice(number))

for i in range(sym):
    temp.append(random.choice(character))

random.shuffle(temp)

password = ""

password = ''.join(temp)

print("Your Generated Password: ", password)
