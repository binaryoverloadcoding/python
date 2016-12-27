#Challenge 1 - William Oldham

import random

jokes = open("jokes.txt","r")

lines = jokes.readlines()
pos = random.randint(0,len(lines))

jokes.close()

jokeline = lines[pos]
jokeline.replace("\n"," ")
jokedata = jokeline.split(",")

if len(jokedata) == 2:
    print("***** " + jokedata[0] + " *****")
    wait = input("Press enter to see the punch line!")
    print("***** " + jokedata[1] + " *****") 
