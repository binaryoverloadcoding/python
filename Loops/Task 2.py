names = []
grades = []

print("Enter 10 names")

for i in range(0, 10):
	name = input("Enter the next name:")
	grade = input("Enter grade: ")
	names.append(name)
	grades.append(grade)


print(names)
print(grades)