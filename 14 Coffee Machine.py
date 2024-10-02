all_list = [
    {
        "type":"report",
        "water":500,
        "milk":200,
        "coffee":300,
        "money":200,

    },
    {
        "type":"capuccino",
        "water":20,
        "milk":10,
        "coffee":15,
        "money":2.5,
    },
    {
        "type": "expresso",
        "water": 30,
        "milk": 20,
        "coffee": 5,
        "money": 3.75,
    },
]
def check_resource(st):
    not_enough = False
    list_id=0
    for i in range(len(all_list)):
        if all_list[i]['type']==st:
            list_id = i
            if all_list[0]["water"]<all_list[i]["water"]:
                print("Not enough water")
                not_enough = True

            if all_list[0]["coffee"]<all_list[i]["coffee"]:
                print("Not enough coffee")
                not_enough = True

            if all_list[0]["milk"]<all_list[i]["milk"]:
                print("Not enough milk")
                not_enough = True
    if not_enough:
        return 0
    else:
        return list_id

coin = 0
change = 0
def check_coin(ch):
    check_cont=True
    while check_cont:
        print("Insert Coins: ")
        pennies = int(input("How many pennies? : "))
        nickles = int(input("How many nickles? : "))
        dimes = int(input("How many dimes? : "))
        quarters = int(input("How many quarters? : "))
        total_money = (pennies * 0.01) + (nickles * 0.05) + (dimes * 0.1) + (quarters * 0.25)
        global coin
        coin += total_money
        if total_money >= all_list[ch]['money']:
            global change
            change += total_money - all_list[ch]['money']
            change = round(change, 2)
            if change > all_list[0]["money"]:
                change=0
                coin=0
                print("Machine Doesn't have that much change. Try different coins...")
            else:
                return total_money
        else:
            print("Not enough money")
            check_cont=False
            return 0


print("Welcome To Funicula Funiculi")
print("We serve Capuccino ($2.5), Expresso ($3.75)")
print("You can also see our resources by choosing 'report'")
cont = True
while cont:
    choice = input("ENTER YOUR CHOICE: ").lower()
    if choice != "report":
        if check_resource(choice):
            list_index = check_resource(choice)
            if check_coin(list_index):
                all_list[0]["money"] += coin
                coin = 0
                all_list[0]["water"] -= all_list[list_index]["water"]
                all_list[0]["milk"] -= all_list[list_index]["milk"]
                all_list[0]["coffee"] -= all_list[list_index]["coffee"]
                print("Your coffee ☕ is done!!!\nDrink\nBefore the Coffee Gets Cold...")
                all_list[0]["money"] -= change
                print(f"Here's your change: {change}")
                change=0
                if input("Do you want to continue?(y/n): ")!='y':
                    cont = False
        else:
            print("Invalid Choice")
    else:
        print(f"Water: {all_list[0]["water"]}\nMilk:{all_list[0]["milk"]}\nCoffee:{all_list[0]["coffee"]}\nMoney:{all_list[0]["money"]}")

print(f"Remaining Resources:\nWater: {all_list[0]["water"]}ml\nMilk:{all_list[0]["milk"]}ml\nCoffee:{all_list[0]["coffee"]}g\nMoney: ${round(all_list[0]["money"],2)}\n")
