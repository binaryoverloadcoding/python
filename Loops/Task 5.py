repeat = "yes"

while repeat == "yes":
   repeatTemp = input("Do you want to repeat? ")
   if (repeatTemp != "no") & (repeatTemp != "yes"):
       repeat = "no"
   repeat = repeatTemp
