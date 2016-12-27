#Challenge 9 - William Oldham
import random
import time

suitDict = {1 : 'hearts',2 : 'diamonds',3 : 'clubs',4 : 'spades'}

while True:
    
    suit = random.randint(1 , 4)
    card = random.randint(1 , 13)
    cardname = ""
    
    suitname = str.capitalize(suitDict[suit])

    if card == 11:
        cardname = "Jack"
    elif card == 12:
        cardname = "Queen"
    elif card == 13:
        cardname = "King"
    elif card == 1:
        cardname = "Ace"
    else:
        cardname = str(card)

    print("You random card is: " + cardname + " " + suitname)
    contin = input("Continue? [Y/N]")
    if contin == "N" or contin == "n":
        break
