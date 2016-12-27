#Challenge 1 - William Oldham

import random, sys

jokes = None

try:
	jokes = open("jokes.txt","r")
except Exception:
	jokes = open("jokes.txt","w")
	jokes.close()
	print("Put jokes in jokes.txt")
	print("Use the format: [joke],[punchline]")
	sys.exit(0)

lines = jokes.readlines()
pos = random.randint(0,len(lines) - 1)

jokes.close()

jokeline = lines[pos]
jokeline.replace("\n"," ")
jokedata = jokeline.split(",")

if len(jokedata) == 2:
    print("***** " + jokedata[0] + " *****")
    input("Press enter to see the punch line!")
    print("***** " + jokedata[1] + " *****") 
