class UserDao:
    
    def __init__(self):
        self.__user_map = {}
    
    def add_user(self, user):
        self.__user_map[user.get_userid()] = user
    
    def update_user(self, user):
        self.__user_map[user.get_userid()] = user
        
    def get_user(self, user_id):
        return self.__user_map.get(user_id, None)
    
    def get_all_users(self):
        return self.__user_map
        