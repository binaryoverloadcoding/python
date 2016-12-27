
import easygui as eg
import string

fileName = "students.csv"

def save(names, grades):
    studentsWrite = open(fileName, "w")

    fileContents = ""
    for user in names:
        items =  user + "," + grades[names.index(user)]
        fileContents = fileContents + items + "\n"

    studentsWrite.write(fileContents)
    studentsWrite.close()

names = []
grades = []

continueProg = True

studentsAppend = open(fileName, "a")
studentsAppend.close()

studentsRead = open(fileName, "r")


for row in studentsRead:
    if row == "\n" or row == "":
        continue
    items = row.split(",")
    name = items[0]
    grade = items[1]
    names.append(name)
    grades.append(grade)

studentsRead.close()


while continueProg:

    options = ["Add", "Remove", "Search", "View", "Exit"]

    userAnswer = eg.buttonbox("Choose an option!", "Choose option", options)

    userAnswer = userAnswer.lower()

    if userAnswer == "add":

        continueAdd = True
        while continueAdd:
            name = eg.enterbox("Enter a name ('end' to finish): ")

            try:
                #Task 4
                index = names.index(name)
                
                message = ""

                message += "-----------------------------------\n"
                message += "That name already exists!\n"
                message += "-----------------------------------"

                eg.msgbox(message)

                continue

            except ValueError:


            if name == None:
                continueAdd = False
                continue

            if name.upper() == "END":
                continueAdd = False
                print("")
                continue
            elif name == "":
                print("")
                continue


            grade = eg.enterbox("Enter a grade: ")

            names.append(name.title())
            grades.append(grade)

            message = ""

            message += "----------------------\n"
            message += "Name: " + name.title() + "\n"
            message += "Grade: " + grade + "\n"
            message += "----------------------\n"
            message += "The record was created!\n"
            message += "----------------------"

            eg.msgbox(message)

            save(names, grades)

    elif userAnswer == "remove":
        continueRemove = True
        while continueRemove:
            name = eg.enterbox("Enter the name to remove ('end' to finish): ")

            if name == None:
                continueRemove = False
                continue

            if name.upper() == "END":
                continueRemove = False
                continue

            name = name.title()

            try:
                #Task 4
                index = names.index(name)
                grades.pop(index)
                #End Task 4

                names.remove(name)

                message = ""

                message += "----------------------\n"
                message += name + " was removed!\n"
                message += "----------------------"

                eg.msgbox(message)

                continue

            except ValueError:
                message = ""

                message += "----------------------\n"
                message += name.title() + " doesn't exist!\n"
                message += "----------------------"

                eg.msgbox(message)

                continue

        save(names, grades)

    #Task 6
    elif userAnswer == "search":
        continueSearch = True
        while continueSearch:

            name = eg.enterbox("Enter a name to search for ('end' to finish): ")
            grade = ""

            if name == None:
                continueSearch = False
                continue

            if name.upper() == "END":
                continueSearch = False
                continue

            name = name.title()

            for student in names:
                if student == name:
                    grade = grades[names.index(name)]

                    grade = grade.replace("\n", "")

                    message = ""

                    message += "-----------\n"
                    message += "Name: " + name + "\n"
                    message += "Grade: " + str(grade) + "\n"
                    message += "-----------"

                    eg.msgbox(message)




    elif userAnswer == "view":

        if len(names) == 0:
            message = ""

            message += "-----------------\n"
            message += "No records!\n"
            message += "-----------------"

            eg.msgbox(message)

            continue

        message = ""

        for student in names:
            grade = grades[names.index(student)]

            grade = grade.replace("\n", "")

            message += "----------------------\n"
            message += "Name: " + student + "\n"
            message += "Grade: " + str(grade) + "\n"
            message += "----------------------\n"

        eg.msgbox(message)

    elif userAnswer == "exit":
        continueProg = False
    else:
        message = ""

        message += "----------------------\n"
        message += "Wrong Option!\n"
        message += "----------------------"

        eg.msgbox(message)


