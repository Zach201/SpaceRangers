import location, player, item, boss
import random
from datetime import datetime

seed = input(" Enter a seed: ")

tile = location.Location(seed + "0,0")

user = player.Player(input("Hello Space Ranger! What is your Ranger name ? "))

boss = boss.Boss()

bossLocationX = random.randint(6, 12)
bossLocationY = random.randint(6, 12)

x = 0
y = 0
tiles = {}
searched_tiles = []

# print("{}, {}".format(bossLocationX, bossLocationY))

def bossFight():
    print("You have descovered a boss!")
    while boss.isAlive() and user.isAlive():
        print("You have {} health!".format(user.health))
        command = input("FIGHT CLUB > ")
        if command == "punch":
            if random.randint(1,5) < 5:
                print("You punched the enemy!")
                boss.health -= 3
            else:
                print("You are clumsy and missed the punch! oof.wav")
        elif command == "curb stomp":
            if random.randint(1,5) ==1:
                print("Wow! A critical hit!")
                boss.health -= 10
            else:
                print("What a horrible attempt!")
        elif command == "Swing Battle axe of the gods":
            if random.randint(1,2) ==1:
                print("SLASH! a critical hit!")
                boss.health -=10
            else:
                print("What a Brutal Attempt, maybe you should use a lighter weapon")
        elif command == "Cross Bow":
            if random.randint(1,2) ==1:
                print("BULLSEYE!!")
                boss.health -=10
            else:
                print("You missed!! You should stick to melee weapons")
        elif command == "Amara's Dagger of the Goddess":
            if random.randint(1,1) ==1:
                print("SLASH! a critical hit!")
                if boss.health > 0:
                    user.health -= boss.damage

def move(direction):
    global x,y
    if direction == "n":
        y += 1
    elif direction == "e":
        x += 1
    elif direction == "s":
        y -= 1
    elif direction == "w":
        x -= 1
    key = "{},{}".format(x, y)
    if key in tiles:
        return tiles[key]
    else:
        newtile = location.Location(seed + key)
        tiles[key] = newtile
        return newtile

running = True
while running and user.isAlive():
    print("You are in {}".format(tile.name))
    if x == bossLocationX and y == bossLocationY:
        bossFight()
    if tile.enemy and tile.enemy.isAlive():
        print("There is a boss enemy present! They have {} health".format(tile.enemy.health))
    command = input("> ")
    if command == "inventory":
        if user.inventory:
            print("You have: {}".format(user.getItems()))
        else:
            print("You have a TG611 Space Rifle")
    elif command == "move":
        direction = input("N/E/S/W > ")[0].lower()
        if direction == "n":
            print("Go North")
            tile = move("n")
        elif direction == "e":
            print("Go East")
            tile = move("e")
        elif direction == "s":
            print("Go South")
            tile = move("s")
        elif direction == "w":
            tile = move("w")
            print("Go West")
        else:
            print("Moving Cancelled")
    elif command == "search":
        if command == "items":
            if tile.seed in searched_tiles:
                print("You've already searched here")
            continue
        random.seed(seed + str(x) + str(y))
        if random.randint(0,5) == 1:
            print("You seem to have found something")
            user.addItem(item.getRandomItem())
        else:
            print("You find nothing")
        searched_tiles.append(tile.seed)
    elif command == "fight":
        random.seed(datetime.now())
        while tile.enemy.isAlive() and user.isAlive():
            print("You have {} health!".format(user.health))
            command = input("FIGHT CLUB > ")
            if command == "punch":
                if random.randint(1,5) < 5:
                    print("You punched the enemy!")
                    tile.enemy.health -= 1
                else:
                    print("You are clumsy and missed the punch! oof.wav")
            elif command == "curb stomp":
                if random.randint(1,5) ==1:
                    print("Wow! A critical hit!")
                    tile.enemy.health -= 10
                else:
                    print("What a horrible attempt!")
            elif command == "Battle axe of the gods":
                if random.randint(1,2) ==1:
                    print("SLASH! a critical hit!")
                    tile.enemy.health -=50
                else:
                    print("What a Brutal Attempt, maybe you should use a lighter weapon")
            elif command == "Cross Bow":
                if random.randint(1,1) ==1:
                    print("BULLSEYE!!")
                    tile.enemy.health -=20
                else:
                    print("You missed!! You should stick to melee weapons")
            elif command == "Amara's Dagger of the Goddess":
                if random.randint(1,1) ==1:
                    print("SLASH! a critical hit!")
                    tile.enemy.health -=999
            elif command == "Pistol":
                if random.randint(1,1) ==1:
                    print("POW! You have shot the Enemy!")
                    tile.enemy.health -=15
