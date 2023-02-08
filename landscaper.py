game = {"tool": 0, "money": 0}

tools = [
    {"name": "teeth", "cost": 0 , "profit": 1},{"name": "scissors", "cost": 5, "profit": 5}, {"name": "push mower", "cost": 25, "profit": 10}, {"name": "battery mower", "cost": 250, "profit": 100},{"name": "a mower team", "cost": 500, "profit": 250}
    ]


def mow_lawn():
    tool = tools[game["tool"]]
    print(f"You mow a lawn with your {tool['name']} and make ${tool['profit']}")
    game['money'] += tool['profit']
def check_stats():
    tool = tools[game["tool"]]
    print(f"You currently have ${game['money']} and are using {tool['name']} to mow lawns.")
def upgrade():
    if (game["tool"] >= len(tools) - 1):
        print("You have the best tool available!")
        return 0
    next_tool = tools[game["tool"]+1]
    if (next_tool == None):
        print("There are no more tools")
        return 0
    if (game["money"] < next_tool["cost"]):
        print("You dont have enough money to upgrade yet...")
        return 0
    print("You have updraded your tool!")
    game["money"] -= next_tool["cost"]
    game["tool"] += 1
def win_check():
    if (game["tool"] == 4 and game["money"] >= 10000):
        print("You win the game!")
        return True
    return False

while(True):
    i = input("[1] Mow Lawn [2] Check Stats [3] Upgrade [4] Quit")
    i = int(i)
    if (i == 1):
        mow_lawn()
    if (i==2):
        check_stats()
    if (i==3):
        upgrade()
    if (i==4):
        print("You quit the game")
        break
    if (win_check()):
        break