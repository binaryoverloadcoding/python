#Challenge 17 - William Oldham

def percentageMark(number, maxNumber):
    percentage = (number / maxNumber) * 100

    if percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    elif percentage >= 30:
        return "F"
    elif percentage >= 20:
        return "G"
    else:
        return "U"

maxModuleMark = int(input("Maximum module mark: "))

module1 = int(input("Module 1 mark: "))
module2 = int(input("Module 2 mark: "))

print("Module 1 grade: " + percentageMark(module1, maxModuleMark))
print("Module 2 grade: " + percentageMark(module2, maxModuleMark))

print("\nAS Grade: " + percentageMark(module1 + module2, maxModuleMark * 2))



