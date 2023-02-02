money = 0

tools = [{"name": "teeth", "cost": 0 , "profit": 1},{"name": "scissors", "cost": 5, "profit": 5}, {"name": "push mower", "cost": 25, "profit": 10}, {"name": "battery mower", "cost": 250, "profit": 100},{"name": "mower team", "cost": 500, "profit": 250}]

equipped = 0

rate = 1

print("Welcome to Landscaper! Press '1' to Mow the Lawn. Press '2' to check your stats. Press 'Q' to quit the game. Happy mowing!")

while(True):
    
    print(money)
    if (money >= tools[equipped].cost):
        user_choice = input(f'Would you like to purchase {tools[equipped].name} for ${tools[equipped].cost}')
        if (user_choice == "y"):
            rate = 5
            money -= 5
            continue
        else:
            continue
    user_choice = input("[1] Mow Lawn [2] Check Stats [Q] Quit")
    if (user_choice == "q"):
        break
    elif (user_choice == "1"):
        money += rate
        print("You mowed the lawn! You earned $1.")
        continue
    elif (user_choice == "2"):
        if (money == 0):
            print("You don't have any money....")
            continue
        else :
            print(f"You have earned ${money}!")
            continue
    else:
        print("Please make another selection.")
        continue