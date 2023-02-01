while(True):
    print("Welcome to Landscaper! Press '1' to Mow the Lawn. Press '2' to check your stats. Press 'Q' to quit the game. Happy mowing!")
    money = 0
    restart = True
    print(money)
    user_choice = input("[1] Mow Lawn [2] Check Stats [Q] Quit")
    if (user_choice == "q"):
        break
    elif (user_choice == "1"):
        money += 1
        print("You mowed the lawn! You earned $1.")
        restart
    elif (user_choice == "2"):
        if (money == 0):
            print("You don't have any money....")
            restart
        else :
            print(f"You have earned ${money}!")
            restart
    else:
        print("Please make another selection.")
        restart