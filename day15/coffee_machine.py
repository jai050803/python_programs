from resources import *

def check(ask):
    if ask == "espresso":
        if espresso["water"] <= resource["water"]:
            if espresso["milk"] <= resource["milk"]:
                if espresso["coffee"] <= resource["coffee"]:
                    print(f"insert {espresso["money"]} rupees to get espresso")
                else:
                    print(f"not enough coffee available coffee :{resource['coffee']} and required is {espresso['coffee']}")
            else:
                print(f"not enough milk available milk :{resource['milk']} and required is {espresso['milk']}")
        else:
            print(f"not enough water available water :{resource['water']} and required is {espresso['water']}")

    elif ask == "latte":
        if latte["water"] <= resource["water"]:
            if latte["milk"] <= resource["milk"]:
                if latte["coffee"] <= resource["coffee"]:
                    print(f"insert {latte["money"]} rupees to get the latte")
                else:
                    print(f"not enough coffee available coffee :{resource['coffee']} and required is {latte['coffee']}")
            else:
                print(f"not enough milk available milk :{resource['milk']} and required is {latte['milk']}")
        else:
            print(f"not enough water available water :{resource['water']} and required is {latte['water']}")

    elif ask == "cappuccino":
        if cappuccino["water"] <= resource["water"]:
            if cappuccino["milk"] <= resource["milk"]:
                if cappuccino["coffee"] <= resource["coffee"]:
                    print(f"insert {cappuccino["money"]} rupees to get cappuccino")     
                else:
                    print(f"not enough coffee available coffee :{resource['coffee']} and required is {cappuccino['coffee']}")
            else:
                print(f"not enough milk available milk :{resource['milk']} and required is {cappuccino['milk']}")
        else:
            print(f"not enough water available water :{resource['water']} and required is {cappuccino['water']}")
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