import random

def lives_counter():
    global  lives
    lives -= 1
    return lives

print("Number Choosing Game between 1 and 100")
lives = int
valid_input = False
while not valid_input:
    level = input("Easy/Hard: ").lower()
    if level == "easy":
        lives = 10
        valid_input = True

    elif level == 'hard':
        lives = 5
        valid_input = True

    else:
        print("invalid input")

print(f"You have {lives} lives to guess the correct number")
target = random.randint(1,100)
win = False
while lives!=0 and not win:
    guess = int(input("Enter your guess: "))
    if guess>target:
        print("Too high")
        lives_counter()
    elif guess<target:
        print("Too low")
        lives_counter()
    else:
        print("Yes!! You've guessed correctly")
        win=True
    # lives-=1
    if not win:
     print(f"Lives remaining: {lives}")
    if lives == 0:
        print(f"correct number: {target}")
