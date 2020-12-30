class User:
    
    def __init__(self, user_id, name, email, phone):
        self.__user_id = user_id
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__payment_from = {}
        self.__payment_to = {}
    
    def set_userid(self, user_id):
        self.__user_id = user_id
    
    def get_userid(self):
        return self.__user_id
    
    def set_name(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name
    
    def set_email(self, email):
        self.__email = email
        
    def get_email(self):
        return self.__email
    
    def set_phone(self, phone):
        self.__phone = phone
        
    def get_phone(self):
        return self.__phone
    
    def set_payment_from(self, user, amount):
        if user not in self.__payment_from:
            self.__payment_from[user] = amount
        else:
            self.__payment_from[user] += amount
        
    def get_payment_from(self):
        return self.__payment_from
    
    def set_payment_to(self, user, amount):
        if user not in self.__payment_to:
            self.__payment_to[user] = amount
        else:
            self.__payment_to[user] += amount
        
    def get_payment_to(self):
        return self.__payment_to
    