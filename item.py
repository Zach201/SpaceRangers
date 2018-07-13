import random

class Item:
    def __init__(self, name,  healing, description):
        self.name = name
        self.healing = healing
        self.description = description

items = [
    Item("Milk from the mily way",  10, "You consume this and it heals you"),
    Item("Magma", -3, "it took away your health, why would you ever eat that?"),
    Item("Space Soda", 5, "You Feel refreshed"),
    Item("Venom ", -50, "it took away your health, are you dumb?"),
    Item("Health Pack", +15, "You heal all of your wounds"),
    Item("Plants that grown on Mars", +420, "PUFF PUFF BABY!!!!"),
    Item("BITCOIN", +0, "Type BITCOIN and see what happens"),
    Item("Laser Rocket Launcher", +999, "The Goddess Amara gives you strength"),
    Item("Space Sword", +5, "TEE Grizzley blesses your Pistol with Pistol Play"),
    Item("Black Hole", +2.5, "The Hunting Knife of a past Hunter")
]


def getRandomItem():
    return random.choice(items)

def getDescription(item2):
    for i in items:
        if i.name == item2:
            return i.getDescription
