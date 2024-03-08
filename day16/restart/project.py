# day16\restart\project.py
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import Menu, MenuItem

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

user_input = input("What would you like? (espresso/latte/cappuccino/) :")

if user_input.lower() == "report":
    money_machine.report()
    coffee_maker.report()

elif user_input.lower() == "latte":
    drink = MenuItem(user_input, 200, 150, 24, 40)
    if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)

elif user_input.lower() == "espresso":
    drink = MenuItem(user_input, 50, 0, 18, 60)
    if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)

elif user_input.lower() == "cappuccino":
    drink = MenuItem(user_input, 250, 50, 24, 50)
    if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)
