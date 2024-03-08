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
        if self.resources["water"] >= drink["water"] and self.resources["milk"] >= drink["milk"] and self.resources["coffee"] >= drink:
            return True
        