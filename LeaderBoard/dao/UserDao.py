class UserDao:
    
    def __init__(self):
        self.__user_map = {}

    def add_user(self, user):
        self.__user_map[user.get_email()] = user
        return user
        
    def update_user(self, user): 
        self.__user_map[user.get_email()] = user
        return user
    
    def get_user(self, email):
        if email in self.__user_map:
            return self.__user_map[email]
        else:
            return None
        
    def search_user(self, search_criteria):
        
        users = []
        
        for key in self.__user_map:
            
            user = self.__user_map[key]
            count_of_eligibility = 0
            
            if not search_criteria.get_country():
                count_of_eligibility += 1
            if search_criteria.get_country() and search_criteria.get_country() == user.get_country():
                count_of_eligibility += 1
            if not search_criteria.get_score():
                count_of_eligibility += 1
            if search_criteria.get_score() and search_criteria.get_score() == user.get_score():
                count_of_eligibility += 1
            if not search_criteria.get_name():
                count_of_eligibility += 1
            if search_criteria.get_name() and search_criteria.get_name() == user.get_name():
                count_of_eligibility += 1
            
            if count_of_eligibility == 3:
                users.append(user)
            
        return users