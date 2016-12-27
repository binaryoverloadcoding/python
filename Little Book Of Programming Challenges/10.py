#Challenge 10 - William Oldham

import random

scorePlayer = 0
scoreComputer = 0

rockPaperScissorsDict = { 1 : 'Rock', 2 : 'Paper', 3 : 'Scissors'}





for i in range(300):
    randNum = random.randint(1, 3)
    playerSelection = int(input("Enter 1, 2 or 3 for Rock, Paper or Scissors: "))
    print("\n-------------------------------------------")

    while playerSelection != 1 and playerSelection != 2 and playerSelection != 3:
        print("You did not enter 1, 2 or 3!")
        playerSelection = int(input("Enter 1, 2 or 3 for Rock, Paper or Scissors: "))
        print("\n-------------------------------------------")

    if randNum == 1:
        if playerSelection == 2:
            print("You won that round!")
            scorePlayer = scorePlayer + 1
            print("Score: Player:" + str(scorePlayer) + " Computer:" + str(scoreComputer))
            print("\n-------------------------------------------")
        elif playerSelection == 1:
            print("That round was a draw!")
            print("Score: Player:" + str(scorePlayer) + " Computer:" + str(scoreComputer))
            print("\n-------------------------------------------")
        else:
            print("Computer won that round!")
            scoreComputer = scoreComputer + 1
            print("Score: Player:" + str(scorePlayer) + " Computer:" + str(scoreComputer))
            print("\n-------------------------------------------")
    elif randNum == 2:
        if playerSelection == 2:
            print("That round was a draw!")
            print("Score: Player:" + str(scorePlayer) + " Computer:" + str(scoreComputer))
            print("\n-------------------------------------------")
        elif playerSelection == 1:
            print("Computer won that round!")
            scoreComputer = scoreComputer + 1
            print("Score: Player:" + str(scorePlayer) + " Computer:" + str(scoreComputer))
            print("\n-------------------------------------------")
        else:
            print("You won that round!")
            scorePlayer = scorePlayer + 1
            print("Score: Player:" + str(scorePlayer) + " Computer:" + str(scoreComputer))
            print("\n-------------------------------------------")
    elif randNum == 3:
        if playerSelection == 2:
            print("Computer won that round!")
            scoreComputer = scoreComputer + 1
            print("Score: Player:" + str(scorePlayer) + " Computer:" + str(scoreComputer))
            print("\n-------------------------------------------")
        elif playerSelection == 1:
            print("You won that round!")
            scorePlayer = scorePlayer + 1
            print("Score: Player:" + str(scorePlayer) + " Computer:" + str(scoreComputer))
            print("\n-------------------------------------------")
        else:
            print("That round was a draw!")
            print("Score: Player:" + str(scorePlayer) + " Computer:" + str(scoreComputer))
            print("\n-------------------------------------------")


if scorePlayer > scoreComputer:
    print("\nYou won that game!")
elif scorePlayer < scoreComputer:
    print("\nThe computer won that game!")
else:
    print("\nThat game was a draw!")
