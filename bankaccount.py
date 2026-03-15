#bank account and display details
class BankAccount:
    def __init__(self):
        self.account_holder = input("Enter your name: ")
        self.balance = int(input("Enter your balance: "))
    def withdraw(self):
        self.amount = int(input("enter amount you want to withdraw:"))
        if self.amount > self.balance:
            print("insufficient balance")
        elif self.amount < 100:
            print("account balance is low")
        else:
            self.balance = self.balance - self.amount
            print("your balance is:",self.balance)
    def deposit(self):
        self.deposit = int(input("enter amount you want to deposit:"))
        self.balance = self.balance +self.deposit
        print("your balance is:",self.balance)
    def display_balance(self):
        print("your balance is:",self.balance)
obj1 = BankAccount()
obj1.withdraw()
obj1.deposit()
obj1.display_balance()
