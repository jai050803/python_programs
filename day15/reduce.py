from resources import *

def reduce():
    if espresso["water"] <= resource["water"]:
        if espresso["milk"] <= resource["milk"]:
            if espresso["coffee"] <= resource["coffee"]:
                resource["water"] -= espresso["water"]
                resource["milk"] -= espresso["milk"]
                resource["coffee"] -= espresso["coffee"]
                resource["money"] += espresso["money"]
                print(f"your espresso is ready")
            else:
                print(f"not enough coffee available coffee :{resource['coffee']} and required is {espresso['coffee']}")
        else:
            print(f"not enough milk available milk :{resource['milk']} and required is {espresso['milk']}")
    else:
        print(f"not enough water available water :{resource['water']} and required is {espresso['water']}")