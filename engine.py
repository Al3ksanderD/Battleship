import random

# Klasa odpowiedzialna za tworzenie statków
class Ship:
    def __init__(self, size):
        self.row = random.randrange(0,9)
        self.col = random.randrange(0,9)
        self.size = size
        self.orientation = random.choice(["h", "v"])
        self.indexes = self.compute_indexes()
    # funkcja zapisująca każdy index pojedynczego statku
    def compute_indexes(self):
        start_index = self.row * 10 + self.col
        if self.orientation == "h":
            return[start_index + i for i in range(self.size)]
        elif self.orientation == "v":
            return[start_index + i*10 for i in range(self.size)]

# Klasa tworząca graczy
class Player:
    def __init__(self):
        self.ships = []
        self.search = ["U" for i in range(100) # "U" for unknown]
        self.place_ships()


