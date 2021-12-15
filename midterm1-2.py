#Author:JTI 12/15/21

initial = input("What was the initial velocity?: ")
final = input("What was the final velocity?: ")
time = input("What was the total time?: ")

acceleration = (float(final)) - float(initial) / float(time)

print("The average velocity was " + str(acceleration) + " meters-per-second.")