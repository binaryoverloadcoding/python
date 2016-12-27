#Challenge 5 - William Oldham

import datetime

now = datetime.datetime.today()
seconds = datetime.datetime.now().second

day1 = int(input("Enter your birth day: "))
month1 = int(input("Enter your birth month: "))
year1 = int(input("Enter your birth year: "))

datediff = now.date() - datetime.date(year1,month1,day1)
print("You have lived for: " + str(datediff.days) + " days!")
print("You have lived for: " + str(datediff.days * 86400 + seconds) + " seconds!")
