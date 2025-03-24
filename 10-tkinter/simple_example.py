
from tkinter import Tk, Entry, Label, Button


def onclick():
    name = field.get()
    label.config(text="Hello " + name)


window = Tk()
window.title("Greeting")
window.geometry("250x150")

field = Entry(window)
field.grid(row=0, column=0)

button = Button(window, text="Click Me", command=onclick)
button.grid(row=1, column=0)

label = Label(window, text="Hello stranger")
label.grid(row=2, column=0)

window.mainloop()