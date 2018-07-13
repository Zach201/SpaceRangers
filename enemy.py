
import random

def get():
    if random.randint(10, 100) == 1:
        return Enemy()
    else:
        return None

class Enemy:
    def __init__(self):
        self.health = random.randint(10, 100)
        self.damage = random.randint(10, 100)

    def isAlive(self):
        return self.health > 0
