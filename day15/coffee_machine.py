from resources import *
from check_function import *
On = True

while On == True:
    ask = input("What would you like to have (espresso/latte/cappuccino) :")
    if ask == "report":
        print(f"Water : {resource['water']} ml")
        print(f"Milk : {resource['milk']} ml")
        print(f"Coffee : {resource['coffee']} g")
        print(f"Money : ${resource['money']}")
    check(ask)
    if ask == "off":
        On = False