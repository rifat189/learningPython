import random

from data import people_list as people
random.shuffle(people)
def score_counter():
    global score
    score +=1

score = 0
cont = True
for i in range(len(people)-1):
    if cont:
        current = people[i]
        next_person = people[i+1]
        choice = input(f"Does {next_person["name"]} has more searches than {current["name"]}? (y/n): ").lower()
        higher = next_person["searches"]>current["searches"]
        if (higher and choice=='y') or (not higher and choice=='n'):
            print("Correct!!!")
            score_counter()
        else:
            print("Wrong!!!")
            cont=False
print(f"Your score: {score}")
