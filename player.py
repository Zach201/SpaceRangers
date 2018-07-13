import item as items2

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 20

    def isAlive(self):
        return self.health > 0

    def addItem(self, item):
        self.inventory.append(item)

    def removeItem(self, name):
        for i in range(len(self.inventory)):
            item = self.inventory[i]
            if item.name == name:
                self.inventory.pop(i)
                return

    def use(self, name):
        if self.hasItem(name):
            for item in self.inventory:
                if item.name == name:
                    self.health += item.healing

    def hasItem(self, name):
        for item in self.inventory:
            if item.name == name:
                return True
        return False

    def getItems(self):
        return self.inventory
