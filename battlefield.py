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
            self.robot.attack(self.dinosaur)
            self.dinosaur.attack(self.robot)
               
    def display_winner(self):
        if self.robot.health <= 0:
            print(f'The winner is {self.dinosaur.name}')
        elif self.dinosaur.health <= 0:
            print(f'The winner of this battle is {self.robot.name}')
