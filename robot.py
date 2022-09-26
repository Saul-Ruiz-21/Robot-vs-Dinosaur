from weapon import weapon
from dinosaur import Dinosaur

class Robot:
    def __init__(self, name):
        self.name = ''
        self.health = 150
        self.active_weapon = weapon('Disfunctional Void', 25)
        print(name)
    
    def attack(self, dinosaur):
        self.dinosaur = Dinosaur
        Dinosaur.health -= self.active_weapon