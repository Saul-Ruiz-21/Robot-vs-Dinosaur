class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 125
        
    def attack(self, robot):
        if self.health >= 0:
            robot.health -= self.attack_power
            print(f'{self.name} pushes back and attacks {robot.name} dealing {self.attack_power} damage')
            print(f'This leaves {robot.name} with {robot.health} health')
            print()
            print()