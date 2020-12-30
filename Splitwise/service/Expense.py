from abc import ABC, abstractmethod

class Expense(ABC):
    
    @abstractmethod
    def make_expense(self, payment_from_userid_list, payment_to_userid, amount, percent_list):
        pass

class ExactExpense(Expense):
    
    def __init__(self, service):
        self.__service = service
        
    def make_expense(self, payment_from_userid_list, payment_to_userid, amount_list):
        
        payment_to_user = self.__service.get_user(payment_to_userid)
        
        idx = 0
        for payment_from_userid in payment_from_userid_list:
            payment_from_user = self.__service.get_user(payment_from_userid)
            payment_to_user.set_payment_from(payment_from_userid, amount_list[idx])
            payment_from_user.set_payment_to(payment_to_userid, amount_list[idx])
            idx += 1
    
class PercentExpense(Expense):
    
    def __init__(self, service):
        self.__service = service
        
    def make_expense(self, payment_from_userid_list, payment_to_userid, amount, percent_list):
        
        amount_in_percent_list = []
        for percent in percent_list:
            amt = amount * (percent/100)
            amount_in_percent_list.append(amt)
            
        payment_to_user = self.__service.get_user(payment_to_userid)
        
        idx = 0
        for payment_from_userid in payment_from_userid_list:
            payment_from_user = self.__service.get_user(payment_from_userid)
            payment_to_user.set_payment_from(payment_from_userid, amount_in_percent_list[idx])
            payment_from_user.set_payment_to(payment_to_userid, amount_in_percent_list[idx])
            idx += 1
    
class EqualExpense(Expense):
    
    def __init__(self, service):
        self.__service = service
        
    def make_expense(self, payment_from_userid_list, payment_to_userid, amount):
        
        each_user_amount = round(amount/(len(payment_from_userid_list)), 2)
        
        payment_to_user = self.__service.get_user(payment_to_userid)

        for payment_from_userid in payment_from_userid_list:
            payment_from_user = self.__service.get_user(payment_from_userid)
            payment_to_user.set_payment_from(payment_from_userid, each_user_amount)
            payment_from_user.set_payment_to(payment_to_userid, each_user_amount)