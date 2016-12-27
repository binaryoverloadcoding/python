#Challenge 14 - William Oldham

import random
import easygui as eg

lives = 2
roundNum = 1

def gameOver():
    eg.msgbox("You have lost!\nYou were on round " + str(roundNum))

while roundNum <= 10:
    startNum = random.randint(1, 13)
    eg.msgbox("Starting number is " + str(startNum))
    choices = ["Higher", "Lower"]
    choice = eg.choicebox("Is the next number Higher or Lower?", "", choices)
    nextNum = random.randint(1, 13)

    if (choice == "Higher" and nextNum > startNum) or (choice == "Lower" and nextNum < startNum):
        eg.msgbox("You have guessed correctly!\nYou have " + str(lives) + " lives left!\nThere are " + str(10 - roundNum) + " rounds left!\nThe Next Number was: " + str(nextNum))
    else:
        lives -= 1
        if lives <= 0:
            gameOver()
            break

        eg.msgbox("You have guessed incorrectly!\nYou have " + str(lives) + " lives left!\nThere are " + str(10 - roundNum) + " rounds left!\nThe Next Number was: " + str(nextNum))
    roundNum += 1

