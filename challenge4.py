class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance
        

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        Account.__init__(self, title, balance)
        self.interestRate = interestRate

account=Account("Ashish", 5000)
print("Title is ",account.title,'and balance is',account.balance)

savings_account = SavingsAccount("Ashish", 5000, 5)
print("Title is ",savings_account.title,"and balance is",savings_account.balance,"and interestRate is",savings_account.interestRate)

