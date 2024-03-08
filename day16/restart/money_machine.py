class MoneyMachine:
    def __init__(self):
        self.profit = 0
    
    def report(self):
        print(f"available money is {self.profit} rupees")