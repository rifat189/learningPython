print("Welcome to the tip calculator!")
a = float(input("What was the total bill?\n$"))
b = int(input("How much tip would you like to give?\n$"))
tip = a * (b / 100)
total = a + tip
c = int(input("How many people to split the bill?\n"))
per = (a+b)/c
print(f"Each person should pay: ${round(per, 2)}")

# for formatting to 2 decimal points always (ex: 32.5 to 32.50)
per = "{:.2f}".format(round(per, 2))
print(f"Each person should pay (formatted): ${per}")

