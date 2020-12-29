from dao import LeaderBoardDao

class LeaderBoardService:
    
    def __init__(self):
        self.__leaderboard_dao = LeaderBoardDao()
        
    def add_user_to_leaderboard(self, user):
        return self.__leaderboard_dao.add_user_to_leaderboard(user)    
    
    def get_top_rank_users(self, k):
        return self.__leaderboard_dao.get_top_rank_users(k)
    
    def get_users_with_score(self, score):
        return self.__leaderboard_dao.get_users_with_score(score)
    
    def get_top_country_users(self, k, country):
        return self.__leaderboard_dao.get_top_country_users(k, country)