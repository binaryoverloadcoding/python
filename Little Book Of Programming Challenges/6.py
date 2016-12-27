#Challenge 6 - William Oldham

import time

print("This program will measure you time perception!")
input("Press enter to start...")


t1 = time.time()

input("Press when you think 10 seconds has passed")


t2 = time.time()

print("You took " + str(round(t2-t1,2)) + " seconds to press it!")
