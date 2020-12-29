from dao import UserDao
from models import User
from exceptions import UserNotExist
import uuid

class UserService:
    
    def __init__(self):
        self.user_dao = UserDao()
        
    def insert_user(self, name, email, country):
        
        existing_user = self.user_dao.get_user(email)
        if existing_user:
            existing_user.set_name(name) 
            existing_user.set_country(country)
            return self.user_dao.update_user(existing_user)
        else:
            user = User(uuid.uuid4(), name, email, country)
            return self.user_dao.add_user(user)
    
    def insert_score(self, email, score):
        
        existing_user = self.user_dao.get_user(email)
        if not existing_user:
            raise UserNotExist
        else:
            existing_user.set_score(score)
            return self.user_dao.update_user(existing_user)
      
    def search_user(self, search_criteria):
        return self.user_dao.search_user(search_criteria)