from tkinter import Tk, Button, Label

def btn_clicked(row, col):
    print("Button clicked", row, col)


window = Tk()
window.title("Tic Tac Toe")

for r in range(3):
    for c in range(3):
        btn = Button(window, text='-', command=lambda row=r, col=c : btn_clicked(row, col))
        btn.grid(row=r, column=c)

window.mainloop()