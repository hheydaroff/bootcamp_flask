class Account():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f"Created a new account for {self.name} with the balance of {self.balance} amount."

    def deposit(self, amount):
        new_balance = self.balance + amount
        self.balance = new_balance
        print(f"Deposited {amount} to your account. your balance now is {self.balance}")

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"The amount you are trying to withdraw is exceeding your balance ({self.balance}). Please withdraw less amount.")
        else:
            new_balance = self.balance - amount
            self.balance = new_balance
            print(f"Withdrew {amount} to your account. your balance now is {self.balance}")


myaccount = Account("Hido", 100)
myaccount.deposit(100)
myaccount.withdraw(300)