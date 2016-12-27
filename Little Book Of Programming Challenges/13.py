#Challenge 13 - William Oldham

import random
import easygui as eg

startNum = random.randint(20,30)
currNum = startNum
lastPerson = ""

removeNums = [1, 2, 3]

eg.msgbox("Starting Number: " + str(startNum))

while currNum > 0:
    choice = int(eg.choicebox("Choose a number to subtract from " + str(currNum), "", removeNums))
    lastPerson = "player"
    currNum -= choice
    eg.msgbox("Player subtracts " + str(choice) + " to get " + str(currNum))
    compChoice = random.randint(1,3)
    lastPerson = "computer"
    currNum -= compChoice
    eg.msgbox("Computer subtracts " + str(compChoice) + " to get " + str(currNum))

if lastPerson == "player":
    eg.msgbox("Computer Wins!")
else:
    eg.msgbox("Player Wins!")