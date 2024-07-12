class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
        else:
            print(f"Deposited: ${amount}")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount < self.account_balance:
                self.account_balance -= amount
                return True
            print (f"Withdrew:{amount}")
        else:
              print(f"Insufficient funds")
              return False
    
            
        
    def display_balance(self):
        self.account_balance
        """Print in a friendly mannner""" 
        print(f"Current Balance: ${self.account_balance:.2f}")