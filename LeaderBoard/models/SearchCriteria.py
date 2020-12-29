class SearchCriteria:
    
    def __init__(self, name=None, score=None, country=None):
        self.__name = name
        self.__score = score
        self.__country = country
        
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_score(self, score):
        self.__score = score
        
    def get_score(self):
        return self.__score
    
    def set_country(self, country):
        self.__country = country
        
    def get_country(self):
        return self.__country