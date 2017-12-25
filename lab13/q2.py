class BankAccount:
    def __init__(self, accountnum, balance=0):
        self.accountnum=accountnum
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount

    def withdraw(self, amount):
        if amount>self.balance:
            print("Insufficient balance. The current balance remained as $",self.balance)
        else:
            self.balance=self.balance-amount

    def show_balance(self):
        return "Current balance is $" + str(self.balance)

    def __repr__(self):
        return "Account Number: "+self.accountnum+" Balance: $"+str(self.balance)

def main():
    my_account=BankAccount('B0A123',1000)
    print(my_account)
    print(my_account.show_balance())
    my_account.deposit(50)
    print(my_account.show_balance())
    my_account.withdraw(2000)
    print(my_account.show_balance())
    my_account.withdraw(100)
    print(my_account.show_balance())



main()
