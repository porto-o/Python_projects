from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()


def barista():

    is_on = True
    while is_on:
        order = input(f"What would you like ({menu.get_items()})")
        if order == "off":
            is_on = False
        elif order == "report":
            coffee_machine.report()
        else:
            drink = menu.find_drink(order)
            if coffee_machine.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_machine.make_coffee(drink)


if __name__ == '__main__':
    barista()
