line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot (like A2, B3, C1): ")
position = input() # like A2, B3, C1 etc.
if position[0]=='A':
  index = 0
elif position[0]=='B':
  index = 1
else:
  index = 2

map[int(position[1])-1][index]= "X"

print(f"{line1}\n{line2}\n{line3}")
