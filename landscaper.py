## Setting the game state

game = {"cutting implement" : 0, "money": 0} 

## Game items
cutting_implements = [
    {"name": "your teeth", "profit": 1, "cost": 0},
    {"name": "rusty scissors", "profit": 5, "cost": 5},
    {"name": "push powered mower", "profit": 50, "cost": 25},
    {"name": "battery powered mower", "profit": 100, "cost": 250},
    {"name": "team of starving students", "profit": 250, "cost": 500},
]

## Game functions

def cut_grass():
    cutting_implement = cutting_implements[game["cutting implement"]]
    print(f"You cut the lawn with {cutting_implement['name']} and made ${cutting_implement['profit']}!")
    game["money"] += cutting_implement["profit"]

def check_stats():
    cutting_implement = cutting_implements[game["cutting implement"]]
    print(f"You currently have ${game['money']} and are using {cutting_implement['name']} to cut grass")

def shop():
    if (game["cutting implement"] >= len(cutting_implements) -1):
        print("There is nothing left to buy!")
        return 0

    buy = cutting_implements[game["cutting implement"] + 1]
    if (buy == None):
        print('Nothing left to buy!')
        return 0
    if (game["money"] < buy["cost"]):
        print('Not enough buy')
        return 0
    game["cutting implement"] += 1
    game["money"] -= buy["cost"]
    cutting_implement = cutting_implements[game["cutting implement"]]
    print(f"You have successfully bought {cutting_implement['name']}")

def win_check():
    if(game["cutting implement"] == len(cutting_implements) -1 and game["money"] == 1000):
        print("You've Won!")
        return True
    return False

while (True):

    i = input("[1] Cut Some Grass [2] Check Stats [3] Shop [4] Quit Game ")

    i = int(i)

    if (i == 1):
        cut_grass()
    
    if (i == 2):
        check_stats()

    if (i == 3):
        shop()
    
    if (i == 4):
        print("You have quit the game!")
        break

    if (win_check()):
        break