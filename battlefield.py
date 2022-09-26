from robot import Robot
from dinosaur import Dinosaur
from weapon import weapon

class Battlefield:
    def __init__(self):
        self.robot = Robot("Repentance")
        self.dinosaur = Dinosaur("Abominable Giga", 30)
    
    def run_game(self):
        pass

    def display_welcome(self):
        print('Ladies and gentleman, welcome to the 5th annual Robot vs Dinosaur battle to the death!!')
    
    def battle_phase(self):
        while 





#        while Robot.health != 0 or Dinosaur.health != 0:
#            if Robot.health != 0:
#                Robot.attack
#                print(f'{Robot.name("Repentance")} attacks {Dinosaur.name("Abominable Giga")} with his weapon {weapon.weapon_name} dealing {weapon.attack_power} damage.')
#                print(f'this leaves {Dinosaur.name("Abominable Giga")} with {Dinosaur.health} health.')
