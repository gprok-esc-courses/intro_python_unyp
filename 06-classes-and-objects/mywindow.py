from tkinter import Tk, Button

def button_action():
    print("Clicked")

window = Tk()
window.geometry("300x300")

button = Button(window, text="Click Me", command=button_action)
button.grid(row=0, column=0)

window.mainloop()