class Board:
    
    def __init__(self, size):
        self.__start = 1
        self.__end = self.__start + size - 1
        self.__size = size
          
    def set_start(self, start):
        self.__start = start
        
    def get_start(self):
        return self.__start
    
    def set_end(self, end):
        self.__end = end
        
    def get_end(self):
        return self.__end
    
    def set_size(self, size):
        self.__size = size
        
    def get_size(self):
        return self.__size