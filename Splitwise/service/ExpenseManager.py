from model import ExpenseType
from dao import UserDao
from .Expense import EqualExpense, ExactExpense, PercentExpense

class ExpenseManager:
    
    def __init__(self, user_service):
        self.__user_service = user_service
            
    # FACTORY PATTERN
    def make_expense(self, payment_from_userid_list, payment_to_userid, amount, expense_type, percent_list=None):
         
        if expense_type == ExpenseType.EXACT:
            expense = ExactExpense(self.__user_service)
            expense.make_expense(payment_from_userid_list, payment_to_userid, amount)
            
        elif expense_type == ExpenseType.EQUAL:
            expense = EqualExpense(self.__user_service)
            expense.make_expense(payment_from_userid_list, payment_to_userid, amount)
            
        elif expense_type == ExpenseType.PERCENT:
            expense = PercentExpense(self.__user_service)
            expense.make_expense(payment_from_userid_list, payment_to_userid, amount, percent_list)
            
            
    