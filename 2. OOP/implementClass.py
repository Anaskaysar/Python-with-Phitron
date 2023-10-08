class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 1000000
    
    def get_balance(self):
        return self.balance
    
    def deposit(self,amount):
        if amount > 0:
            self.balance +=amount;
    
    def withdraw(self,amount):
        if amount <self.min_withdraw:
            print( f'You are trying to withdwar less than {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print( f'You can not exceed the {self.max_withdraw} withdrawal limit')
        else:
            self.balance -= amount;
            print( f'Here is your money {amount}')
            print( f'Remaining Amount {self.get_balance()}')

DBBL = Bank(15000)
DBBL.withdraw(25)
DBBL.withdraw(50000000)
DBBL.withdraw(200000)