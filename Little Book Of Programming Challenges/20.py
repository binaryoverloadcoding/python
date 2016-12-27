#Challenge 20 - William Oldham

lastNum1 = 1
lastNum2 = 1

finishNumber = int(input("Enter finish: "))
currNum = 2

while currNum != finishNumber:
    ln1Temp = lastNum1
    ln2Temp = lastNum2
    lastNum1 = ln2Temp
    lastNum2 = ln1Temp + ln2Temp
    currNum = currNum + 1

print(str(lastNum2))

