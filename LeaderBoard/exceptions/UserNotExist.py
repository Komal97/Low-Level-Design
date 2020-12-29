class UserNotExist(Exception):
    
    def __init__(self):
        print('User does not exist')