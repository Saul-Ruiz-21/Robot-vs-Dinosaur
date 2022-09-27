from robot import Robot
from dinosaur import Dinosaur


class Battlefield:
    def __init__(self):
        self.robot = Robot("Repentance")
        self.dinosaur = Dinosaur("Abominable Giga", 30)
    
    def run_game(self):
        self.display_welcome()
        self.battle_phase()

    def display_welcome(self):
        print('Ladies and gentleman, welcome to the 5th annual Robot vs Dinosaur battle to the death!!')
    
    def battle_phase(self):
        while self.robot.health != 0 or self.dinosaur.health != 0:
            if self.robot.health != 0:
                self.robot.attack(self.dinosaur.health)
                print(f'{self.robot.name} attacks {self.dinosaur.name} with his weapon {self.robot.active_weapon.weapon_name} dealing {self.robot.active_weapon.attack_power} damage.')
                print(f'This leaves {self.dinosaur.name} with {self.dinosaur.health} health')


def run_games():
    run = Battlefield()
    run.run_game()

run_games()

#        while Robot.health != 0 or Dinosaur.health != 0:
#            if Robot.health != 0:
#                Robot.attack
#                print(f'{Robot.name("Repentance")} attacks {Dinosaur.name("Abominable Giga")} with his weapon {weapon.weapon_name} dealing {weapon.attack_power} damage.')
#                print(f'this leaves {Dinosaur.name("Abominable Giga")} with {Dinosaur.health} health.')
