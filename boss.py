

class Boss:
    def __init__(self):
        self.health = 35
        self.damage = 15

    def isAlive(self):
        return self.health > 0
