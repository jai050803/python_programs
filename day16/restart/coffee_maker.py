class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }
    
    def report(self):
        print(f"water : {self.resources['water']} rupees")
        print(f"milk : {self.resources['milk']} ml")
        print(f"Coffee : {self.resources['coffee']} mg")
        
    def is_resource_sufficient(self, drink):
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        if can_make == False:
            print("Sorry! We can't make that drink. Not enough resources. ")
        return can_make
        