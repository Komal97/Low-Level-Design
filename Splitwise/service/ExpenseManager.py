from model import ExpenseType
from dao import UserDao

class ExpenseManager:
    
    def __init__(self, user_service):
        self.__user_service = user_service
            
    def make_expense(self, payment_from_userid_list, payment_to_userid, amount, expense_type, percent_list=None):
        
        if expense_type == ExpenseType.EXACT:
            self.__make_expense_exact(payment_from_userid_list, payment_to_userid, amount)
            
        elif expense_type == ExpenseType.EQUAL:
            self.__make_expense_equal(payment_from_userid_list, payment_to_userid, amount)
            
        elif expense_type == ExpenseType.PERCENT:
            self.__make_expense_in_percent(payment_from_userid_list, payment_to_userid, amount, percent_list)
            
            
    def __make_expense_exact(self, payment_from_userid_list, payment_to_userid, amount_list):
        
        payment_to_user = self.__user_service.get_user(payment_to_userid)
        
        idx = 0
        for payment_from_userid in payment_from_userid_list:
            payment_from_user = self.__user_service.get_user(payment_from_userid)
            payment_to_user.set_payment_from(payment_from_userid, amount_list[idx])
            payment_from_user.set_payment_to(payment_to_userid, amount_list[idx])
            idx += 1
        
    
    def __make_expense_equal(self, payment_from_userid_list, payment_to_userid, amount):
        
        each_user_amount = round(amount/(len(payment_from_userid_list)), 2)
        
        payment_to_user = self.__user_service.get_user(payment_to_userid)

        for payment_from_userid in payment_from_userid_list:
            payment_from_user = self.__user_service.get_user(payment_from_userid)
            payment_to_user.set_payment_from(payment_from_userid, each_user_amount)
            payment_from_user.set_payment_to(payment_to_userid, each_user_amount)
        
    def __make_expense_in_percent(self, payment_from_userid_list, payment_to_userid, amount, percent_list):
        
        amount_in_percent_list = []
        for percent in percent_list:
            amt = amount * (percent/100)
            amount_in_percent_list.append(amt)
            
        payment_to_user = self.__user_service.get_user(payment_to_userid)
        
        idx = 0
        for payment_from_userid in payment_from_userid_list:
            payment_from_user = self.__user_service.get_user(payment_from_userid)
            payment_to_user.set_payment_from(payment_from_userid, amount_in_percent_list[idx])
            payment_from_user.set_payment_to(payment_to_userid, amount_in_percent_list[idx])
            idx += 1