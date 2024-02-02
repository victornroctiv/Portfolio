# Today we are going to create a random password generator using for loops and arrays in python
# Make sure to print you password to the screen
# Can you randomize your password generated

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Let's make a password")
lets = int(input("How many letters? "))
syms = int(input(f"How many symbols? "))
nums = int(input(f"How many numbers? "))
# What is line 15 doing? Creating a variable blank list.
password = []
# Below is the guide how to write the for loop you need to write for symbols and numbers
for char in range(0, lets):
    password.append(random.choice(letters))
for char in range (0, syms):
    password.append(random.choice(symbols))
for char in range (0, nums):
    password.append(random.choice(numbers))
shuff = len(password)-1
for i in range(shuff):
    random_index = random.randint(0, shuff)
    temp = password.pop(random_index)
    password.append(temp)
cp = [str(x) for x in password]
np = "".join(cp)
print(f"Here is your randomly generated password: {np}")