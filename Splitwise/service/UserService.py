from model import User
from dao import UserDao

class UserService:
    
    def __init__(self):
        self.__user_dao = UserDao()
        
    def add_user(self, user_id, name, email, phone):
        
        existing_user = self.__user_dao.get_user(user_id)
        if existing_user:
            existing_user.set_name(name)
            existing_user.set_email(email)
            existing_user.set_phone(phone)
            self.__user_dao.update_user(existing_user)
        else:
            new_user = User(user_id, name, email, phone)
            self.__user_dao.add_user(new_user)
    
    def get_user(self, user_id):
        return self.__user_dao.get_user(user_id)
    
    def show_user(self, user_id):
        
        user = self.__user_dao.get_user(user_id)
        collect_from = user.get_payment_from()
        for u in collect_from:
            print(f'{u} owes {user_id}: {collect_from[u]}')
            
        paid_to = user.get_payment_to()
        for u in paid_to:
            print(f'{user_id} owes {u}: {paid_to[u]}')
        
        print('--------------------------------------')