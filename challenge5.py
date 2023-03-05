class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def withdrawal(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def getBalance(self):
        return self.balance
    

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
    
    def interestAmount(self):
        return (self.balance * self.interestRate) / 100

demo1 = SavingsAccount("Ashish", 2000, 5)
print("Account balance is",demo1.getBalance())  # Output: 2000
demo1.deposit(500)
print("After deposit account balance is ",demo1.getBalance())  # Output: 2500
demo1.withdrawal(500)
print("After withdrawal account balance is ",demo1.getBalance())  # Output: 2000
print("InterestAmount is ",demo1.interestAmount()) # Output: 100.0

