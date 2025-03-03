
from account import Account
from tkinter import Tk, Button, Label, Entry

bank_accounts = {
    1: Account(1, "George"),
    2: Account(2, "Mary"),
    3: Account(3, "Peter"),
    4: Account(4, "Tom"),
    5: Account(5, "Pam")
}

def start_account():
    global account
    id = int(id_field.get())
    if id in bank_accounts:
        account = bank_accounts[id]
        msg = "Welcome " + account.name
        msg_label.configure(text=msg)
    else: 
        msg_label.configure(text="Invalid account")
        account = None

def withdraw():
    global account
    amount = int(amount_field.get())
    if account is not None:
        result = account.withdraw(amount)
        msg_label.configure(text=result)
    else:
        msg_label.configure(text="No account selected")

def deposit():
    global account
    amount = int(amount_field.get())
    if account is not None:
        result = account.deposit(amount)
        msg_label.configure(text=result)
    else:
        msg_label.configure(text="No account selected")

account = None

window = Tk()
window.title("ATM")
window.geometry("500x300")

id_label = Label(window, text="ID:")
id_label.grid(row=0, column=0)

id_field = Entry(window)
id_field.grid(row=0, column=1)

start_btn = Button(window, text="Start", command=start_account)
start_btn.grid(row=0, column=2)

amount_label = Label(window, text="Amount:")
amount_label.grid(row=1, column=0)

amount_field = Entry(window)
amount_field.grid(row=1, column=1)
withdraw_btn = Button(window, text="Withdraw", command=withdraw)
withdraw_btn.grid(row=1, column=2)
deposit_btn = Button(window, text="Deposit", command=deposit)
deposit_btn.grid(row=1, column=3)

msg_label = Label(window, text="-")
msg_label.grid(row=2, column=1)

window.mainloop()