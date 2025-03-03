class Account:
    # Constructor
    def __init__(self, id, name):
       self.id = id
       self.name = name
       self.balance = 0 

    def deposit(self, amount):
        if amount > 0 and amount <= 600:
            self.balance += amount
            return "Deposit completed"
        else:
            return "Invalid amount"
        
    def withdraw(self, amount):
        if amount > 0 and amount <= 600:
            if amount <= self.balance:
                self.balance -= amount
                return "Withdraw completed"
            else:
                return "Insufficient balance"
        else:
            return "Invalid amount"

    def __str__(self):
        return str(self.id) + " " + self.name + " balance: " + str(self.balance)