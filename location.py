import random, enemy

descriptions = ["Planet", "Galaxie of", "Sector BZF1",  "Galaxie ESV"]
location_types = ["Earth", "Mars", "Neptune", "Mercury", "Saturn", "Jupiter", "Uranus", "Venus"]

class Location:
    def __init__(self, seed):
        self.seed = seed
        random.seed(seed)
        self.name = "{} {}".format(
                random.choice(descriptions),
                random.choice(location_types)
            )
        self.enemy = enemy.get()
