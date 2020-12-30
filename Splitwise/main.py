from service import ExpenseManager, UserService
from model import ExpenseType

def main():
    
    user_service = UserService()
    expense_manager = ExpenseManager(user_service)
    
    user_service.add_user('u1', 'Komal Bansal', 'komalbansal@gmail.com', '8783939390')
    user_service.add_user('u2', 'Nikhil Kumar', 'nikhilkumar@gmail.com', '9182837001')
    user_service.add_user('u3', 'Daniel', 'daniel@gmail.com', '9830189200')
    user_service.add_user('u4', 'Preeti Aggarwal', 'preeti@gmail.com', '9810283779')
    
    expense_manager.make_expense(['u2', 'u3'], 'u1', 1000, ExpenseType.EQUAL)
    user_service.show_user('u1')
    user_service.show_user('u2')
    user_service.show_user('u3')
    
    expense_manager.make_expense(['u2', 'u3'], 'u1', [100, 200], ExpenseType.EXACT)
    user_service.show_user('u1')
    user_service.show_user('u2')
    user_service.show_user('u3')
    
    expense_manager.make_expense(['u1', 'u3'], 'u2', 1000, ExpenseType.PERCENT, [30, 70])
    user_service.show_user('u1')
    user_service.show_user('u2')
    user_service.show_user('u3')
    
main()