import random
from types import NoneType

# user input
choice = int(input("Choose Rock(1), Paper(2) or Scissor(3): "))
if choice < 1 or choice > 3:
    print("Your choice is invalid")
else:
    # Declaring user's choice
    if choice == 1:
        choseOption='Rock'
    elif choice == 2:
        choseOption = 'Paper'
    else:
        choseOption = 'Scissor'
    print(f"You have chosen {choseOption}")

    # Computer Choice
    compChoice = random.randint(1,3)

    # Declaring computer choice
    if compChoice == 1:
        choseOption='Rock'
    elif compChoice == 2:
        choseOption = 'Paper'
    else:
        choseOption = 'Scissor'
    print(f"Computer has chosen {choseOption}")

    # Choosing the winner
    winner=NoneType
    if choice == 1:
        if compChoice==1:
            winner = 0
        elif compChoice==2:
            winner = 2
        elif compChoice==3:
            winner = 1
    elif choice == 2:
        if compChoice==1:
            winner = 1
        elif compChoice==2:
            winner = 0
        elif compChoice==3:
            winner = 2
    elif choice == 3:
        if compChoice==1:
            winner = 2
        elif compChoice==2:
            winner = 1
        elif compChoice==3:
            winner = 0

    # Declaring the winner
    if winner == 0:
        print("It a draw")
    elif winner == 1:
        print("You win the game")
    elif winner == 2:
        print("Computer Wins the game")
