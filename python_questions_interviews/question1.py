# Write a program that defines a class representing a simple bank account. The class should have methods for depositing money, withdrawing money, and checking the account balance. Instantiate an object of this class and demonstrate its functionality.

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited successfully. New balance: ${self.balance}.")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn successfully. Remaining balance: ${self.balance}.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    
    def check_balance(self):
        print(f"Current balance: ${self.balance}.")

# Instantiate an object of the BankAccount class
account = BankAccount("John Doe", 1000)

# Demonstrate depositing money
account.deposit(500)

# Demonstrate withdrawing money
account.withdraw(200)

# Demonstrate checking the account balance
account.check_balance()

# Attempt to withdraw more than the current balance
account.withdraw(2000)

# Attempt to deposit a negative amount
account.deposit(-300)
