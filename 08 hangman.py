import random
HANGMAN = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = ["animal", "books", "writer"]
chosen_word = random.choice(words)
print(chosen_word)

blankList = ['_']*len(chosen_word)
lives = 7
count = 0
position =[]
win = False
while lives != 0:

    ch = input("Your choice: ").lower()
    wrong=True

    for i in range(len(chosen_word)):
        if ch in chosen_word[i]:
            blankList[i] = ch
            count+=1
            wrong=False

    if wrong:
        lives -= 1
        print(f"Oops!! Wrong guess.. Lives remaining: {lives}")

    print(HANGMAN[len(HANGMAN)-lives])



    st = ''.join(blankList)
    print(st)

    for i in blankList:
        if i != '_':
            win = True
            break
if win:
    print("You survived")
else:
    print("You died")
