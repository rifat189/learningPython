import random

names = input().split()
total = len(names)
choice = random.randint(0, total-1)
print(f"{names[choice]} is going to pay for the meal")
