from Enemy import *
import random

class Ogre(Enemy):
    def __init__(self,type_of_enemy = "Ogre",health_points = 10,attack_damage = 1):
        super().__init__(type_of_enemy = type_of_enemy,
                         health_points=health_points,
                         attack_damage=attack_damage)


    def talk(self):
        print("Ogre is slamming hands all round")

    def special_attack(self):
        did_special_attack_work = random.random() < 0.20
        if did_special_attack_work:
            self.health_points +=4
            print("Zombie gets angry &  increases by 4 HP")
        print(f"Ogre Current scour is {self.health_points}")