#Challenge 8 - William Oldham

import datetime

now = datetime.datetime.today()
seconds = datetime.datetime.now().second

day1 = int(input("Enter your birth day: "))
month1 = int(input("Enter your birth month: "))
year1 = int(input("Enter your birth year: "))

datediff = now.date() - datetime.date(year1,month1,day1)

print("You are approximatly " + str(round(datediff.days / 365 , 1)) + " years old!")
if datediff.days/365 >= 18:
    print("You cn vote!")
else:
    print("You cannot vote!")
