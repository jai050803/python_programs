class CoffeeMaker:
    def __init__(self, resources):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }
    
    def report(self):
        print(f"Money : {self.resources['money']} rupees")
        print(f"Water : {self.resources['water']} ml")
        print(f"Milk : {self.resources['milk']} ml")
        