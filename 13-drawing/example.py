from tkinter import Tk, Canvas 

class Token:
    def __init__(self):
        self.x = 30
        self.y = 30

def key_pressed(e):
    key = e.keysym
    print(key)
    if key == "Up":
        token.y -= 10
    elif key == "Down":
        token.y += 10
    elif key == "Left":
        token.x -= 10
    elif key == "Right":
        token.x += 10
    canvas.delete("all")
    canvas.create_rectangle(token.x, token.y, token.x+10, token.y+10, fill='red')


token = Token()
window = Tk()
window.geometry("300x300")

canvas = Canvas(window, bg='white', width=280, height=280)
canvas.grid(row=0, column=0)

canvas.create_rectangle(token.x, token.y, token.x+10, token.y+10, fill='red')

window.bind('<KeyRelease>', key_pressed)

window.mainloop()
