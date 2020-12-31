from .Coffee import CoffeeFactory
from model import Ingredients

class CoffeeMachineService:
    
    def __init__(self):
        self.__coffee_factory = CoffeeFactory()
        self.__ingredients = Ingredients()
        
    def prepare_coffee(self, coffee_type, coffee_cup_size, coffee_strength):
        
        coffee_type_obj = self.__coffee_factory.get_coffee_type(coffee_type, self.__ingredients)
        
        coffee_type_obj.prepare_coffee(coffee_cup_size, coffee_strength)
        print(f'Your {coffee_type} is prepared')
        
    def pour_coffee(self):
        print('Your coffee is poured')
            