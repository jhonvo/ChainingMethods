class User:
    
    def __init__(self,name):
        self.name = name
        self.balance = 0.0
    
    def deposit(self, amount):
        self.balance += amount
        return self

    
    def withdraw (self,amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print(f"Balance is not sufficient to withdraw {amount}")
        return self

    
    def transfer(self, destination, amount):
        if amount < self.balance:
            self.balance -= amount
            destination.balance += amount
        else:
            print(f"Balance is not sufficient to transfer {amount}")
        self.display_user_balance()
        destination.display_user_balance()
        return self

    def display_user_balance(self):
        print(f'User: {self.name}, Balance:{self.balance}')
        return self