# Story book 

import subprocess
import turtle
import time
import random
import webbrowser

yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
 
# Introduction
name = input("What is your name, adventurer?\n")
print("Greetings, " + name + ". Let us go on a quest!")
print("You find yourself on the edge of a dark forest.")
print("Can you find your way through?\n")
 
# Start of game
response = ""
while response not in yes_no:
    response = input("Would you like to step into the forest?\nyes/no\n")
    if response == ("yes"):
        print("You head into the forest. You hear crows cawwing in the distance.\n")
    elif response == ("no"):
        print("You are not ready for this quest. Goodbye, " + name + ".")
        quit()
    else: 
        print("I didn't understand that.\n")
 
# Next part of game
response = ""
while response not in directions:
    print("As you step into the forest you hear the fluttering of the crows slowly disappearing ahead of you.\n")
    print("To your left, you see specifically placed rocks creating what seems like a path.\n")
    print("To your right, just unbothered forestry like nothing has traveled through there in years.\n")
    response = input("Which way will you go? or will you go backward for fear of the unknown?\nleft|right|forward|backward\n")
    if response == "forward":
        print("While following the crows you notice their diving for something low to the ground.\n")
        print("You come to a clearing and you see the crows are diving for a singular shadowy spot in the center of the clearing until...")
        #play cut scene
        print("Loki appears to you and asks, What is your name traveler? \n To which you reply, " + name + "sir.")
        fans = input("Loki: Would you like to play a game? Yes|No")
        if fans == "yes":
            subprocess.run(["python", "Unit104\RideTheBus.py"])
    elif response == "left":
        print("The rocks continue further and become more aligned and do form a path")
        print("At the end of the path is a hut and just as you notice someone in the window.")
        time.sleep(0.5)
        print("*Fwoosh*\n a bright light hits you from the window")
        time.sleep(1)
        print("You've been hypnotized and trapped by an evil wizard!\n You'll be used as one of his pawns to do his bidding unknowingly.")
        time.sleep(2)
        trap = turtle.Turtle()
        window = turtle.Screen()
        trap.speed(10)
        trap.pencolor('red')

        def drawSpiral(trap, linelen):
            trap.forward(linelen)
            trap.right(90)
            drawSpiral(trap, linelen-10)

        drawSpiral(trap, 80)
        window.exitonclick()
        time.sleep(1)
    elif response == "right":
        spi = random.randint(0, 10)
        if spi <= 3:
            print("You run into a few spiderwebs and a couple spiders land on you.")
            print("You swipe them off quickly as you stumble through the dense forest.")
            print("On the floor you notice a mound of dirt that could be easily missed had someone not been paying attention.")
            dirt = ("Will you get dirty and dig through the mound? yes|no")
            if dirt == "yes":
                print("You forget about the spiders and you get your hands dirty, pulling dirt out of the ground.")
                print("You hand strikes something hard/n You continue digging and slowly make out the shape of a chest!")
                print(+ name + "has found burried tressure!")
                time.sleep(2.5)
                webbrowser.open("https://images.ctfassets.net/pujs1b1v0165/3MP8uJp2eLptyjRze8Ao2n/165b8cb66eea3b5fb7ae9688f34ac05e/forrest_fenn_treasure_location__1_.jpg?w=1200&fit=fill&fm=webp")
                exit()
        elif spi >= 4:
            print("You panic because you just walked through" + spi + "spider webs each with 4 spiders around!")
            print("Not paying attention you trip over some logs and fall to the floor.\nScaring a majority of the spiders off you and you manage to swipe the rest off.")
            print("As you get up to gather yourself, you realize that you have no clue where you came from,\nYou stumbled into the deep forst and everything looks the same.")
            print("Lost in the woods without food or supplies...you end up...dead")
            print("Riparoonie Atricoonie")
            exit()
    elif response == "backward":
        print("You choose to go back, perhaps afraid of the unknown.")
        print("Did you let your fear control you? or did you make a sound decision to go back to your boring life?")
        bans = ("Would you like to try again? yes|no \n")
        if bans == "no":
            webbrowser.open("https://youtu.be/gc7wKr0XkN8?si=eO82V2Z3xxXwabJE&t=58")
        elif bans == "yes":
            continue
        else:
            print("It was a yes or no, I'm not taking anything else, get outta here.")
            exit()