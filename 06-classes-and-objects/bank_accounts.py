
from account import Account

bank_accounts = {
    1: Account(1, "George"),
    2: Account(2, "Mary"),
    3: Account(3, "Peter"),
    4: Account(4, "Tom"),
    5: Account(5, "Pam")
}

while True:
    id = int(input('ID: '))
    if id in bank_accounts:
        account = bank_accounts[id]
        print("Welcome " + account.name)
        option = -1
        while option != 0:
            print("1. Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("0. EXIT")
            option = int(input("Choose: "))
            match option:
                case 1: 
                    print("Balance", account.balance)
                case 2: 
                    amount = int(input("Amount to deposit: "))
                    result = account.deposit(amount)
                    print(result)
                case 3:
                    amount = int(input("Amount to withdraw: "))
                    result = account.withdraw(amount)
                    print(result)
                case 0:
                    print("Bye!")
                case _:
                    print("Wrong option")
    else: 
        print("Account ID not found, create one")
        name = input("Your name: ")
        bank_accounts[id] = Account(id, name)