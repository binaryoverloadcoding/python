#Challenge 4 - William Oldham

speed = int(input("Enter Average Speed (MPH): "))
time = int(input("Enter Time (H) :"))
distance = speed * time

print("Distance Travelled (M): " + str(distance))

distance = int(input("How far do you want to travel (M) ? "))
time = int(input("WHat time do you want to take (H) ? "))

speed = distance / time
print("You will have to travel at: " + str(speed) + "MPH")
