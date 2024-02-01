from resources import *

def check(ask):
    if ask == "espresso":
        if espresso["water"] <= resource["water"] and espresso["milk"] <= resource["milk"] and espresso["coffee"] <= resource["coffee"]:
            print(f"insert {espresso["money"]} rupees to get espresso")
        else:
            return False
    elif ask == "latte":
        if latte["water"] <= resource["water"] and latte["milk"] <= resource["milk"] and latte["coffee"] <= resource["coffee"]:
            print(f"insert {latte["money"]} rupees to get the latte")
        else:
            return False
    elif ask == "cappuccino":
        if cappuccino["water"] <= resource["water"] and cappuccino["milk"] <= resource["milk"] and cappuccino["coffee"] <= resource["coffee"]:
            print(f"insert {cappuccino["money"]} rupees to get cappuccino")     
        else:
            print(f"not enough resources")
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