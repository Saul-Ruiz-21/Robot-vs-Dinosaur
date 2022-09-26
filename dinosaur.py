from robot import Robot

class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 120
        
    def attack(self, robot):
        self.robot = robot
        self.fight = self.attack_power - Robot(self.health)


Dinosaur('Abominable Giga', 30)