import os


end = False
bidder = []
while not end:
    name = input("Enter name: ")
    bid = int(input("Enter your bid: "))
    newDict = {"name": name, "bid": bid}
    bidder.append(newDict)
    cont = input("Do you want to continue?(y/n): ").lower()
    if cont=='n':
        end = True
    if os.name == 'nt':  # for Windows
        os.system('cls')
    else:  # for macOS or Linux
        os.system('clear')

    # clear()
max_bid = 0
max_name = None
# max_bid = None
for i in bidder:
    if i['bid'] > max_bid:
        max_name = i['name']
        max_bid = i['bid']
print(f"{max_name}, {max_bid}")

print(bidder)
