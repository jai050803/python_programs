# day16\restart\project.py
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

user_input = input("What would you like? (espresso/latte/cappuccino/) :")

if user_input.lower() == "report":
    money_machine.report()
    coffee_maker.report()
