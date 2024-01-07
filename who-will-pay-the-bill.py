import random

names_string = input("Enter the names: \n")

names = names_string.split(", ")

len = len(names)

choice = random.randint(0, len-1)

print(f"{names[choice]} is going to pay the bill today!")