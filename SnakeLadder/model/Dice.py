import random
class Dice:
    def __init__(self):
        self.__start = 1
        self.__end = 6
    
    def roll_dice(self):
        return random.randint(self.__start, self.__end)