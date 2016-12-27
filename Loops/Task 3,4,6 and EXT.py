
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
    userAnswer = input("Make your choice [add/remove/search/view/end]: ")

    userAnswer = userAnswer.lower()

    if userAnswer == "add":

        continueAdd = True
        while continueAdd:
            name = input("\nEnter a name ('end' to finish): ")

            if name.upper() == "END":
                continueAdd = False
                print("")
                continue
            elif name == "":
                print("")
                continue


            grade = input("Enter a grade: ")

            names.append(name.title())
            grades.append(grade)

            print("\n-----------")
            print("Name: " + name.title())
            print("Grade: " + grade)
            print("-----------")
            print("The record was created!")
            print("-----------\n")

            save(names, grades)

    elif userAnswer == "remove":
        continueRemove = True
        while continueRemove:
            name = input("\nEnter the name to remove ('end' to finish): ")

            if name.upper() == "END":
                continueRemove = False
                print("")
                continue

            name = name.title()

            try:
                #Task 4
                index = names.index(name)
                grades.pop(index)
                #End Task 4

                names.remove(name)

                print("\n-----------")
                print(name + " was removed!")
                print("-----------")
                continue

            except ValueError:
                print("\n-----------")
                print(name.title() + " doesn't exist!")
                print("-----------")
                continue 

        save(names, grades)          

    #Task 6
    elif userAnswer == "search":
        continueSearch = True
        while continueSearch:

            name = input("\nEnter a name to search for ('end' to finish): ")
            grade = ""

            if name.upper() == "END":
                continueSearch = False
                print("")
                continue

            name = name.title()

            for student in names:
                if student == name:
                    grade = grades[names.index(name)]
                    print("\n-----------")
                    print("Name: " + name)
                    print("Grade: " + str(grade))
                    print("-----------")



    elif userAnswer == "view":

        if len(names) == 0:
            print("\n-----------")
            print("No records!")
            print("-----------\n")
            continue

        print("")

        for student in names:
            grade = grades[names.index(student)]
            print("-----------")
            print("Name: " + student)
            print("Grade: " + str(grade))
            print("-----------")

        print("")

    elif userAnswer == "end":
        continueProg = False
    else:
        print("\n-------------")
        print("Wrong Option!")
        print("-------------\n")


