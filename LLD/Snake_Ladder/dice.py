import random

class Dice:
    def __init__(self,number):
        self.number = number
        

    def roll(self):
        return random.randint(self.number*1,self.number*6)
