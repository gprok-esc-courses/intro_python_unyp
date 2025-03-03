from tkinter import Tk, Button

def button_action():
    print("Clicked")

def second_button_clicked():
    print("Second Clicked")

window = Tk()
window.geometry("300x300")

button = Button(window, text="Click Me", command=button_action)
button.grid(row=0, column=0)

button2 = Button(window, text="Click Me Instead", command=second_button_clicked)
button2.grid(row=1, column=0)

window.mainloop()