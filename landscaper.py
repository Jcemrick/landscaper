## Setting the game state

game = {"Cutting Implement" : 0, "Money": 0} 

## Game items
cutting_implements = [
    {"name": "Teeth", "profit": 1, "cost": 0},
    {"name": "Rusty Scissors", "profit": 5, "cost": 5},
    {"name": "Push Powered Mower", "profit": 50, "cost": 25},
    {"name": "Battery Powered Mower", "profit": 100, "cost": 250},
    {"name": "Team of Starving Students", "profit": 250, "cost": 500},
]

## Game functions

def cut_grass():
    cutting_implement = cutting_implements[game["Cutting Implement"]]
    print(f"You cut the lawn with {cutting_implement['name']} and made {cutting_implement['profit']}!")
    game["Money"] += cutting_implement["profit"]

def check_stats():
    cutting_implement = cutting_implements[game["Cutting Implement"]]
    print(f"You currently have ${game['money']} and are using {cutting_implement['name']} to cut grass")

def shop():
    buy = cutting_implements[game["Cutting Implement"] + 1]
    if (buy == None):
        print('Nothing left to buy!')
        return 0
    if (game["Money"] < buy["cost"]):
        print('Not enough buy')
        return 0
    game["Money"] -= buy["cost"]
    game["Cutting Implement"] += 1

def win_check():
    if(game["Cutting Implement"] == 4 and game["Money"] == 1000):
        print("You've Won!")
        return True
    return False

