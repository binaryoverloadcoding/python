#Challenge 18 - William Oldham

import time

def drawstars(spaceNum, starNum):
    spaces = " " * spaceNum
    stars = "*" * starNum

    return spaces + stars

print(drawstars(2, 3))
print(drawstars(2, 3))
print(drawstars(3, 1))
print(drawstars(2, 3))
print(drawstars(0, 7))
print(drawstars(2, 3))
print(drawstars(2, 1) + drawstars(1, 1))
print(drawstars(1, 2) + drawstars(1, 2))

print("\n\n")

baseSize = int(input("Enter the base of the pyramid: "))

if baseSize % 2 == 0:
    currSize = 2
    spaceSize = int((baseSize - 2) / 2)
    print(drawstars(spaceSize, currSize))
    while currSize != baseSize:



        spaceSize = spaceSize - 1
        currSize = currSize + 2

        print(drawstars(spaceSize, currSize))
else:
    currSize = 1
    spaceSize = int((baseSize - 1) / 2)
    print(drawstars(spaceSize, currSize))
    while currSize != baseSize:



        spaceSize = spaceSize - 1
        currSize = currSize + 2

        print(drawstars(spaceSize, currSize))


input()
