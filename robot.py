from weapon import weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 150
        self.active_weapon = weapon('Disfunctional Void', 25)
    
    def attack(self, dinosaur):
          if self.health >= 0:
                dinosaur.health -= self.active_weapon.attack_power
                print(f'{self.name} attacks {dinosaur.name} with his weapon {self.active_weapon.weapon_name} dealing {self.active_weapon.attack_power} damage.')
                print(f'This leaves {dinosaur.name} with {dinosaur.health} health')
                print()
                print()
        
        