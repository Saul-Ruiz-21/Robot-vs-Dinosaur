from robot import Robot
from dinosaur import Dinosaur


class Battlefield:
    def __init__(self):
        self.robot = Robot("Repentance")
        self.dinosaur = Dinosaur("Abominable Giga", 50)
    
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print('Ladies and gentleman, welcome to the 5th annual Robot vs Dinosaur battle to the death!!')
        print()
        print()


    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            if self.robot.health >= 0:
                self.robot.attack(self.dinosaur)
                print(f'{self.robot.name} attacks {self.dinosaur.name} with his weapon {self.robot.active_weapon.weapon_name} dealing {self.robot.active_weapon.attack_power} damage.')
                print(f'This leaves {self.dinosaur.name} with {self.dinosaur.health} health')
                print()
                print()
            if self.dinosaur.health >= 0:
                self.dinosaur.attack(self.robot)
                print(f'{self.dinosaur.name} pushes back and attacks {self.robot.name} dealing {self.dinosaur.attack_power} damage')
                print(f'This leaves {self.robot.name} with {self.robot.health} health')
                print()
                print()


    def display_winner(self):
        if self.robot.health <= 0:
            print(f'The winner is {self.dinosaur.name}')
        elif self.dinosaur.health <= 0:
            print(f'The winner of this battle is {self.robot.name}')


#        while Robot.health != 0 or Dinosaur.health != 0:
#            if Robot.health != 0:
#                Robot.attack
#                print(f'{Robot.name("Repentance")} attacks {Dinosaur.name("Abominable Giga")} with his weapon {weapon.weapon_name} dealing {weapon.attack_power} damage.')
#                print(f'this leaves {Dinosaur.name("Abominable Giga")} with {Dinosaur.health} health.')
