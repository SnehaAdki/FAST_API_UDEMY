from Enemy import *
import random

class Zombie(Enemy):
    def __init__(self,type_of_enemy = "Zombie",health_points = 10,attack_damage = 1):
        super().__init__(type_of_enemy = type_of_enemy,
                         health_points=health_points,
                         attack_damage=attack_damage)


    def talk(self):
        print("*Grumbling.....*")

    def spread_disease(self):
        print("Spread Infection")

    def special_attack(self):
        did_special_attack_work = random.random() < 0.5
        if did_special_attack_work:
            self.health_points +=2
            print("Zombie regenerated 2 HP")
        print(f"Zombie Current scour is {self.health_points}")