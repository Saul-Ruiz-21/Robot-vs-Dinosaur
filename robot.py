from weapon import weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 150
        self.active_weapon = weapon('Disfunctional Void', 25)
    
    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        