#Author:JTI 12/15/21

import random

def clone_name_generator(number):
    total = []
    number = random.randint(0,9999)
    if number < 10:
        numbers = "000" + str(number)
    elif number < 100:
        numbers = "00" + str(number)
    elif number < 1000:
        numbers = "0" + str(number)
    while number == "y":
        total = total + "CT-" + str(number)
        return(number)

number = input("Name a clone? ")
if number.lower() == "y":
    print("Clones name is CT-" + str(total)
elif number.lower() == "n":
    print() 