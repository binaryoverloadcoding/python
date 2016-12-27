#Challenge 7 - William Oldham

import time

print("This program will measure your alphabet typing!")
input("Press enter to start...")

alphabet = "abcdefghijklmnopqrstuvwxyz"

while True:
    t1 = time.time()

    answer = str(input("Try and type the alphabet as fast as you can: "))


    t2 = time.time()

    if(alphabet == str.lower(answer)):
        print("You took " + str(round(t2-t1,2)) + " seconds to type it!")
        break
    else:
        print("You entered it incorrectly!")
