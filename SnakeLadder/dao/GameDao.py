from collections import deque
class GameDao:
    
    def __init__(self):
        self.__players = deque([])
        self.__ladders = {}
        self.__snakes = {}
    
    def add_player(self, player):
        self.__players.append(player)
    
    def get_player(self):
        player = self.__players.popleft()
        return player
    
    def set_snakes(self):
        self.__snakes[15] = 6
        self.__snakes[25] = 20
        self.__snakes[60] = 45
        self.__snakes[88] = 60
    
    def get_snakes(self, position):
        return self.__snakes.get(position, None)
    
    def set_ladders(self):
        self.__ladders[10] = 20
        self.__ladders[32] = 50
        self.__ladders[40] = 58
        self.__ladders[65] = 80
        self.__ladders[85] = 98
    
    def get_ladders(self, position):
        return self.__ladders.get(position, None)
    
    
    