#Challenge 12 - William Oldham

import easygui as eg

factorNum = eg.integerbox("What number do you want the factors for?")
factors = []

for i in range(1, factorNum+1):
    if factorNum % i == 0:
        factors.append(i)

if len(factors) == 2:
    eg.msgbox("Your number is a prime number!")
else:
    factorStr = ""
    for i in factors:
        factorStr += str(i) + ", "
    eg.msgbox("The factors of the number " + str(factorNum) + " are:\n" + factorStr)