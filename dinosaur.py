from robot import Robot

class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 125
        
    def attack(self, robot):
        robot = Robot
        Robot.health -= self.attack_power