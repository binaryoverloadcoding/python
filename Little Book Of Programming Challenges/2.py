#Challenge 2 - William Oldham

name = ""

while name == "":
	name = str(input("What is your name? "))
	if name == "":
		print("Enter a proper name!")


print("Hello " + name)
