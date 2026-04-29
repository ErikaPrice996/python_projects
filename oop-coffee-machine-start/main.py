from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
cm = CoffeeMaker()
mm = MoneyMachine()
power = True

while power:
    order = input(f"What would you like to order?: ({menu.get_items()}) ").lower()
    if order == "off":
        power = False
        continue
    elif order == "report":
        cm.report()
        mm.report()
        continue
    else:
        drink = menu.find_drink(order)
        if drink is not None:
            if cm.is_resource_sufficient(drink):
                if mm.make_payment(drink.cost):
                    cm.make_coffee(drink)

