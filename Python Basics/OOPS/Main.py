from Enemy import *
from Zombie import *
from Ogre import *
from Hero import *


# print(f"{enemy.type_of_enemy} has {enemy.health_points} health points"
#       f" & can do the attack {enemy.attack_damage}")

# zombie = Enemy() ## default
# zombie.type_of_enemy = 'Zombie'
# zombie.talk()
# zombie.walk_forward()
# zombie.attach()

# no_arg_zombie = Enemy() #No argument constructor
# zombie = Enemy("Enemy") #parameter constructor
# big_zombie = Enemy("Orge" , 20,100) #with all parameter constructor
# big_zombie.type_of_enemy = 'Zooo'
# zombie.get_details()
# big_zombie.get_details()

# enemy = Enemy('Zombie')
# enemy.get_details()
# # print(enemy.__type_of_enemy) #throws error as undefined becz we are trying to access outside the class
# enemy.get_type_of_enemy()
# enemy.set_type_of_enemy("Ogre")
# enemy.get_details()

# enemy = Enemy('Zombie')
# enemy.get_type_of_enemy()


# zombie = Zombie(20,1)
# zombie.get_type_of_enemy()
# zombie.talk()
# zombie.spread_disease()
#
# ogre = Ogre(20,3)
# ogre.get_type_of_enemy()
# ogre.talk()

# def battle(e1:Enemy , e2:Enemy):
#     e1.talk()
#     e2.talk()
# 
#     while e1.health_points > 0 and e2.health_points > 0:
#         e1.special_attack()
#         e2.special_attack()
#         e2.attack()
#         e1.health_points -= e2.attack_damage
#         e1.attack()
#         e2.health_points -= e1.attack_damage
# 
#     if e1.health_points > e2.health_points:
#         print("Enemy 1 wins")
#     else:
#         print("Enemy 2 wins")
# 
# zombie = Zombie(health_points = 10,attack_damage = 1)
# ogre = Ogre(health_points = 20,attack_damage = 3)
# 
# battle(zombie, ogre)



def hero_battle(hero: Hero,enemy:Enemy):
    while hero.health_points > 0 and enemy.health_points > 0:
        print("----------------")
        enemy.special_attack()
        print(f" Hero: {hero.health_points} HP left")
        print(f"{enemy.get_type_of_enemy()} : {enemy.health_points} HP left")
        enemy.attack()
        hero.health_points -= enemy.attack_damage
        hero.attack()
        enemy.health_points -= hero.attack_damage

    print("----------------")
    if hero.health_points >0:
        print("Hero Wins!....")
    else:
        print("Enemy Wins!....")

zombie = Zombie(health_points = 10,attack_damage = 1)
hero = Hero(health_points = 10,attack_damage = 1)
weapon = Weapon("sword",5)
hero.weapon = weapon
hero.equip_weapon()
hero_battle(hero,zombie)