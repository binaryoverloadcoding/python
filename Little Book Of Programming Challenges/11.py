#Challenge 11 - William Oldham

import easygui as eg

answers = ["XOR", "OR", "AND", "NAND", "NOR"]

contin = 1

while contin == 1:
    gate = eg.choicebox("Pick a Logic gate", "Logic Gates", answers)

    if gate == None:
        continue

    input1 = eg.integerbox("Enter Input 1", "Logic Gates")
    input2 = eg.integerbox("Enter Input 2", "Logic Gates")

    result = 0

    if gate == "XOR":
        if input1 == 1 and input2 == 0:
            result = 1
        elif input1 == 0 and input2 == 1:
            result = 1
        else:
            result = 0
    elif gate == "OR":
        if input1 == 1 and input2 == 0:
            result = 1
        elif input1 == 0 and input2 == 1:
            result = 1
        elif input1 == 1 and input2 ==1:
            result = 1
        else:
            result = 0
    elif gate == "AND":
        if input1 == 1 and input2 ==1:
            result = 1
        else:
            result = 0
    elif gate == "NAND":
        if input1 == 1 and input2 ==1:
            result = 0
        else:
            result = 1
    elif gate == "NOR":
        if input1 == 0 and input2 == 0:
            result = 1
        else:
            result = 0

    eg.msgbox("The result of gate: " + gate + " is: " + str(result))

    contin = eg.ynbox()