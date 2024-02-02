#This is a python remake of the card game ride the bus.

import random
#time imported to slow down text pop up
import time

#This Builds the deck
vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace'] #card rankings
suits = ['spades', 'clubs', 'hearts', 'diamonds']

#Set up for the 1st phase of thea game
red = ['hearts', 'diamonds']
black = ['spades', 'clubs']

first_card = random.choice(vals),random.choice(suits)
card_two = random.choice(vals),random.choice(suits)
card_three = random.choice(vals),random.choice(suits)
card_four = random.choice(vals),random.choice(suits) # these four choose cards for the game

play_cards = [first_card,card_two,card_three,card_four] #sets up for duplicate checking

cards_in_play = [first_card, card_two, card_three, card_four] #also sets up for duplicate checking

play_cards1 = cards_in_play.remove(card_two)
play_cards2 = cards_in_play.remove(card_three)
play_cards3 = cards_in_play.remove(card_four) #also sets up for duplicate checking

# for testing the game (ctrl + / once they are all highlited to bring them into code)
# print('[The %s of %s]' % (first_card))
# print('[The %s of %s]' % (card_two))
# print('[The %s of %s]' % (card_three))
# print('[The %s of %s]' % (card_four))

#these make it so there are no duplicate cards
if card_two == play_cards1:
    card_two = random.choice(vals),random.choice(suits)
    # print('New 2nd card [The %s of %s]' % (card_two))

if card_three == play_cards2:
    card_three = random.choice(vals),random.choice(suits)
    # print('New 3rd card [The %s of %s]' % (card_three))

if card_four == play_cards3:
    card_four = random.choice(vals),random.choice(suits)
    # print('New 4th card [The %s of %s]' % (card_four))

#for testing the game (ctrl + shift once they are all highlited to bring them into code)
# print('[The %s of %s]' % (first_card))
# print('[The %s of %s]' % (card_two))
# print('[The %s of %s]' % (card_three))
# print('[The %s of %s]' % (card_four))
    
 
#Phase 1: Red or Black
print('Welcome aboard the bus, you are our only passenger!')
time.sleep(1) #timers to allow enough time for player to read
print('If you want to get to your destination, you have to get through this card game')
time.sleep(1.5)
print('[*][*][*][*]')
time.sleep(0.5)

print("We'll start from left to right.")
time.sleep(0.5)
color_input = input("tell me...will this first card be red or black? ")
time.sleep(0.8)
print('*flips top card* \n[The %s of %s]' % (first_card))
if 'hearts' in (first_card) or 'diamonds' in (first_card):
    if (color_input) == str.lower("red"):
            print("Correct, this is a red card")
    else:
        print("WRONG! GET ON THE NEXT BUS!")
        exit()
elif 'spades' in (first_card) or 'clubs' in (first_card):
    if (color_input) == str.lower("black"):
        print("Correct, this is a black card")
    else:
        print("WRONG! GET ON THE NEXT BUS!")
        exit()
time.sleep(0.5)

#Phase 2: Higher or Lower
print("Moving on to the second card, we'll just look at the number not the suit.")
time.sleep(0.5)
second_card_input = input("Now for the next card, will it be higher or lower than your previous card? ")
time.sleep(0.5)
print('*flips top card* \n[The %s of %s]' % (card_two))
if second_card_input == str.lower("higher"):
    if  vals.index(first_card[0]) < vals.index(card_two[0]):
        high_card = (card_two)
        low_card = (first_card)
        print("The card is actually higher, good job")
    else:
        print("Whoops sorry, this is your stop, get on a new bus.")
        exit()
elif second_card_input == str.lower("lower"):
    if  vals.index(first_card[0]) > vals.index(card_two[0]):
        high_card = (first_card)
        low_card = (card_two)
        print("The card is actually lower, good job")
    else:
        print("Whoops sorry, this is your stop, get on a new bus.")
        exit()
else:
    print("invalid input")
time.sleep(0.5)
print("This third card is a little tricky.")
time.sleep(0.5)

#Phase 3: Inbetween or Outside
third_card_input = input("Will it be inbetween or outside the values of your first two cards? ")

print('[The %s of %s]' % (high_card))
print('[The %s of %s]' % (low_card))
print("Third card is \n *flips third card*")
time.sleep(0.5)
print('[The %s of %s]' % (card_three))
time.sleep(0.5)

if third_card_input == str.lower("inbetween"):
    if vals.index(high_card[0]) >= vals.index(card_three[0]) >= vals.index(low_card[0]):
        print('Would you look at that, it is in between!')
    else:
        print('Shucks, you almost had it, guess you have to get on a new bus.')
        exit()
if third_card_input == str.lower("outside"):
    if vals.index(high_card[0]) <= vals.index(card_three[0]):
        print('Would you look at that, it is outside!')
    elif vals.index(low_card[0]) >= vals.index(card_three[0]):
        print('Would you look at that, it is outside!')
    else:
        print('Shucks, you almost had it, guess you have to get on a new bus.')
        exit()
time.sleep(0.5)

#Phase 4: Guess the Suit
print("This last card you'll have to guess the suit.")
fourth_card_input = input("Will it be: Spades, Clubs, Hearts, or Diamonds? ")

print("*flips fourth card*")
time.sleep(0.5)
print('[The %s of %s]' % (card_four))

if fourth_card_input == str.lower("Spades"):
    if 'spades' in card_four[1]:
        print("You did it, you have guessed all four cards! Now brag to your friends and get off my bus!")
    else:
        print("Darn, so close! This was the last card...welp get on a new bus buddy.")
        exit()
elif fourth_card_input == str.lower("Clubs"):
    if 'clubs' in card_four[1]:
        print("You did it, you have guessed all four cards! Now brag to your friends and get off my bus!")
    else:
        print("Darn, so close! This was the last card...welp get on a new bus buddy.")
        exit()
elif fourth_card_input == str.lower("Hearts"):
    if 'hearts' in card_four[1]:
        print("You did it, you have guessed all four cards! Now brag to your friends and get off my bus!")
    else:
        print("Darn, so close! This was the last card...welp get on a new bus buddy.")
        exit()
elif fourth_card_input == str.lower("Diamonds"):
    if 'diamonds' in card_four[1]:
        print("You did it, you have guessed all four cards! Now brag to your friends and get off my bus!")
    else:
        print("Darn, so close! This was the last card...welp get on a new bus buddy.")
        exit()