class Enemy:
    #default/ Empty Constructor
    # def __init__(self):
    #     pass

    # type_of_enemy : str
    # health_points : int = 10
    # attack_damage  : int = 1

    # No Argument Constructor
    # def __init__(self):
    #     print("New emery created with no starting values")


    # def get_details(self):
    #     print(f"{self.__type_of_enemy} has {self.health_points} health points"
    #   f" & can do the attack {self.attack_damage}")

    # def set_type_of_enemy(self,type_of_enemy ):
    #     self.__type_of_enemy = type_of_enemy

    # parameter Constructor
    def __init__(self,type_of_enemy,health_points = 10,attack_damage = 1):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def talk(self):
        print(f"I am a {self.__type_of_enemy}. Be prepared for a fight")

    def walk_forward(self):
        print(f"{self.__type_of_enemy} moves closer to you")

    def get_type_of_enemy(self):
        print(self.__type_of_enemy)

    def attack(self):
        print(f"{self.__type_of_enemy} attacks for {self.attack_damage} damage")

    def special_attack(self):
        print("Enemy has no special attack")