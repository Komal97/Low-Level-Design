class Player:
    
    def __init__(self, name):
        self.__name = name
        self.__is_won = False
        self.__position = 0
        
    def set_name(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name
    
    def set_is_won(self, is_won):
        self.__is_won = is_won
        
    def get_is_won(self):
        return self.__is_won
    
    def set_position(self, position):
        self.__position = position
        
    def get_position(self):
        return self.__position