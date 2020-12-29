class LeaderBoard:
    
    def __init__(self):
        self.__users = []
    
    def set_users(self, users):
        self.__users = users
        
    def get_users(self):
        return self.__users