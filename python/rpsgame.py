# Remade Rock, Paper, Scissors in python

import random
import time #I like to import this because I dont like how fast the words pop up

hand = ['rock','paper','scissors']#Computers choices

w = (0)
l = (0)
d = (0)#These are variables to track your record

user_hand = ()#Variable to set up the while loop
print("A massive hand floats down and challenges you to a game, you know this game all too well.")
while user_hand not in hand:
    bighand = random.choice(hand)
    time.sleep(1)
    user_hand = input("Whats your move? rock|paper|scissors\n")
    time.sleep(0.5)
    print(f"The massive hand does {bighand}")
    time.sleep(0.5)
    if bighand == "rock":
        if user_hand == "rock":
            print("Draw.")
            d = d + 1
        elif user_hand == "paper":
            print("You Win!")
            w = w + 1
        elif user_hand == "scissors":
            print("You Lose.")
            l = l + 1
        else:
            print("Input Invalid")
    if bighand == "paper":
        if user_hand == "paper":
            print("Draw.")
            d = d + 1
        elif user_hand == "scissors":
            print("Winner!")
            w = w + 1
        elif user_hand == "rock":
            print("Oof.")
            l = l + 1
        else:
            print("Input Invalid")
    if bighand == "scissors":
        if user_hand == "scissors":
            print("Draw.")
            d = d + 1
        elif user_hand == "rock":
            print("Dub")
            w = w + 1
        elif user_hand == "paper":
            print("L")
            l = l + 1
        else:
            print("Input Invalid")
    time.sleep(0.5)
    print(f"Record: Wins[{w}] Loss[{l}] Draws[{d}]")
    user_hand = input("Would you like to play again? y/n\n")
    if user_hand == "n":
        break
if w < l:
    print("The massive hand pulls your pants down because losing to him in Rock, Paper, Scissors wasn't humiliating enough")
elif l < w:
    print("The massive hand robs a bank and gives you $50,000 because a legend like you should not be leaving empty handed.")
else:
    print("The massive hand points at you as if to say, 'This isn't over yet.'")