from datetime import datetime

class User:
    
    def __init__(self, id, name, email, country):
        self.__id = id
        self.__name = name
        self.__email = email
        self.__country = country
        self.__score = 0
        self.__last_updated_score = datetime.now()
    
    def set_id(self, id):
        self.__id = id
        
    def get_id(self):
        return self.__id
    
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name

    def set_email(self, email):
        self.__email = email
        
    def get_email(self):
        return self.__email
    
    def set_country(self, country):
        self.__country = country
    
    def get_country(self):
        return self.__country
    
    def set_score(self, score):
        self.__score = score
        self.__last_updated_score = datetime.now()
    
    def get_score(self):
        return self.__score