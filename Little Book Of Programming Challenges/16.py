#Challenge 16 - William Oldham

import random

continueProg = True

while continueProg == True:
    randomNum = random.randint(1,100)

    print("I have selected a random number between 1 and 100!")
    print("Try and guess it!\n\n")

    guess = int(input("Enter a number between 1 and 100:"))

    if not guess > 0 & guess < 100:
        print("Your number is not between 1 and 100!")
        continue

    answerTrue = False
    tries = 0

    while answerTrue == False:
        if guess > randomNum:
            print("Your guess was too big!")
            tries += 1
        elif guess < randomNum:
            print("Your guess was too small!")
            tries += 1
        else:
            print("Well done! You guessed in " + str(tries) + " tries!")
            answerTrue = True
            break
        guess = int(input("Enter a number between 1 and 100:"))

        if not guess > 0 & guess < 100:
            print("Your number is not between 1 and 100!")
            continue

    continueText = input("Continue? [Y/N]").lower()

    if continueText == "y":
        continueProg = True
    else:
        continueProg = False




