class MoneyMachine:
    def __init__(self):
        self.profit = 0
        self.money_received = 0
    
    def report(self):
        print(f"available money is {self.profit} rupees")
    
    def process_coins(self):
        print("please insert coins")
        for _ in ["5s", "10s", "20s"]:
            money = int(input(f"how many money in terms of {_} :"))
            self.money_received += money
        return self.money_received
    
    def make_payment(self, cost):
        self.process_coins()
        if self.money_received >= cost:
            change = self.money_received - cost
            print(f"here is rupees {change} in change")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("sorry that's not enough money. money refunded")
            self.money_received = 0
            return False