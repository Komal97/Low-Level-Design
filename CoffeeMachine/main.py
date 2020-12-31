from model import CoffeeType, CoffeeCupSize, CoffeeStrength
from service import CoffeeMachineService

def main():
    
    coffee_machine = CoffeeMachineService()
    
    coffee_machine.prepare_coffee(CoffeeType.LATTE, CoffeeCupSize.SMALL, CoffeeStrength.LIGHT)
    coffee_machine.pour_coffee()
    
    
main()