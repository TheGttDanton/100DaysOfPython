import random
names_string = input("Enter everybody's name, separated by comma. \n")
names = names_string.split(", ")

#max_index = len(names) - 1
#random_index = random.randint(0, max_index)

#print(f"{names[random_index]} is going to pay the bill")

#alternate way:

name_bill = random.choice(names)
print(f"{name_bill} is going to pay the bill")
