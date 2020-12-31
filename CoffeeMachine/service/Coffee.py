from abc import ABC, abstractmethod
from model import CoffeeType, CoffeeStrength, CoffeeCupSize

class Coffee(ABC):
    
    def __init__(self, ingredients_obj):
        self._ingredients = ingredients_obj
        
    @abstractmethod
    def prepare_coffee(self, coffee_cup_size, coffee_strength):
        pass
    
class EspressoCoffee(Coffee):
    
    def __init__(self, ingredients_obj):
        super().__init__(ingredients_obj)
        
    def prepare_coffee(self, coffee_cup_size, coffee_strength):
        
        if coffee_cup_size == CoffeeCupSize.SMALL:
            if coffee_strength == CoffeeStrength.LIGHT:
                pass
            elif coffee_strength == CoffeeStrength.MEDIUM:
                pass
            elif coffee_strength == CoffeeStrength.STRONG:
                pass
        elif coffee_cup_size == CoffeeCupSize.MEDIUM:
            if coffee_strength == CoffeeStrength.LIGHT:
                pass
            elif coffee_strength == CoffeeStrength.MEDIUM:
                pass
            elif coffee_strength == CoffeeStrength.STRONG:
                pass
        elif coffee_cup_size == CoffeeCupSize.LARGE:
            if coffee_strength == CoffeeStrength.LIGHT:
                pass
            elif coffee_strength == CoffeeStrength.MEDIUM:
                pass
            elif coffee_strength == CoffeeStrength.STRONG:
                pass
    
class LatteCoffee(Coffee):
    
    def __init__(self, ingredients_obj):
        super().__init__(ingredients_obj)
        
    def prepare_coffee(self, coffee_cup_size, coffee_strength):
        if coffee_cup_size == CoffeeCupSize.SMALL:
            if coffee_strength == CoffeeStrength.LIGHT:
                pass
            elif coffee_strength == CoffeeStrength.MEDIUM:
                pass
            elif coffee_strength == CoffeeStrength.STRONG:
                pass
        elif coffee_cup_size == CoffeeCupSize.MEDIUM:
            if coffee_strength == CoffeeStrength.LIGHT:
                pass
            elif coffee_strength == CoffeeStrength.MEDIUM:
                pass
            elif coffee_strength == CoffeeStrength.STRONG:
                pass
        elif coffee_cup_size == CoffeeCupSize.LARGE:
            if coffee_strength == CoffeeStrength.LIGHT:
                pass
            elif coffee_strength == CoffeeStrength.MEDIUM:
                pass
            elif coffee_strength == CoffeeStrength.STRONG:
                pass
    
class CappuccinoCoffee(Coffee):
    
    def __init__(self, ingredients_obj):
        super().__init__(ingredients_obj)
        
    def prepare_coffee(self, coffee_cup_size, coffee_strength):
        if coffee_cup_size == CoffeeCupSize.SMALL:
            if coffee_strength == CoffeeStrength.LIGHT:
                pass
            elif coffee_strength == CoffeeStrength.MEDIUM:
                pass
            elif coffee_strength == CoffeeStrength.STRONG:
                pass
        elif coffee_cup_size == CoffeeCupSize.MEDIUM:
            if coffee_strength == CoffeeStrength.LIGHT:
                pass
            elif coffee_strength == CoffeeStrength.MEDIUM:
                pass
            elif coffee_strength == CoffeeStrength.STRONG:
                pass
        elif coffee_cup_size == CoffeeCupSize.LARGE:
            if coffee_strength == CoffeeStrength.LIGHT:
                pass
            elif coffee_strength == CoffeeStrength.MEDIUM:
                pass
            elif coffee_strength == CoffeeStrength.STRONG:
                pass
    
class CoffeeFactory:
    
    def get_coffee_type(self, coffee_type, ingredients_obj):
        
        if coffee_type == CoffeeType.ESPRESSO:
            return EspressoCoffee(ingredients_obj)
        
        elif coffee_type == CoffeeType.LATTE:
            return LatteCoffee(ingredients_obj)
        
        elif coffee_type == CoffeeType.CAPPUCCINO:
            return CappuccinoCoffee(ingredients_obj)