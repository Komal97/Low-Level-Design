from models import User, SearchCriteria
from service import LeaderBoardService, UserService

def main():
    
    leaderboard_service = LeaderBoardService()
    user_service = UserService()
    
    user = user_service.insert_user('Komal Bansal', 'komalbansal@gmail.com', 'India')
    leaderboard_service.add_user_to_leaderboard(user)
    print(f'{user.get_email()} added')
    
    user = user_service.insert_user('Nikhil Kumar', 'nikhilkumar@gmail.com', 'India')
    leaderboard_service.add_user_to_leaderboard(user)
    print(f'{user.get_email()} added')
    
    user = user_service.insert_user('Daniel', 'daniel@gmail.com', 'USA')
    leaderboard_service.add_user_to_leaderboard(user)
    print(f'{user.get_email()} added')
    
    user_service.insert_score('komalbansal@gmail.com', 5)
    user_service.insert_score('nikhilkumar@gmail.com', 2)
    user_service.insert_score('daniel@gmail.com', 4)
    
    top_rank_users = leaderboard_service.get_top_rank_users(2)
    print(f'Top 2 Rank users: ', end = ' ')
    for user in top_rank_users:
        print(user.get_email(), end = ', ')
    print()
    
    users_with_score = leaderboard_service.get_users_with_score(5)
    print(f'Users with score 5: ', end = ' ')
    for user in users_with_score:
        print(user.get_email(), end = ', ')
    print()
    
    search_criteria = SearchCriteria()
    search_criteria.set_country('India')
    search_criteria.set_score(5)
    searched_user = user_service.search_user(search_criteria)
    print(f'Searched user: ', end = ' ')
    for user in searched_user:
        print(user.get_email(), end = ', ')
    print()
    
main()