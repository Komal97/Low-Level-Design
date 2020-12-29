class LeaderBoardDao:
    
    def __init__(self):
        self.__users = []
    
    def add_user_to_leaderboard(self, user):
        self.__users.append(user)
        return user
        
    def get_top_rank_users(self, k):
        
        filtered_user = sorted(self.__users, key = lambda user: user.get_score(), reverse=True)
        
        top_k_users, counter = [], 0
        
        for user in filtered_user:
            top_k_users.append(user)
            counter += 1
            if counter == k:
                break
            
        return top_k_users
    
    def get_users_with_score(self, score):
        
        users_with_score = []
        for user in self.__users:
            if user.get_score() == score:
                users_with_score.append(user)
        return users_with_score
    
    def get_top_country_users(self, k, country):
        
        user_with_country = [user for user in self.__users if user.get_country() == country]
        
        filtered_user = sorted(user_with_country, key = lambda user: user.get_score(), reverse = True)
        
        top_k_users, counter = [], 0
        
        for user in filtered_user:
            top_k_users.append(user)
            counter += 1
            if counter == k:
                break
            
        return top_k_users
        
        
        
        