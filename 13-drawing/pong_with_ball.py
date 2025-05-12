from tkinter import Tk, Canvas 

class Token:
    def __init__(self):
        self.x = 120
        self.y = 270
        self.step = 10

class Ball:
    def __init__(self):
        self.x = 30
        self.y = 30
        self.size = 10
        self.step = 2

def key_pressed(e):
    key = e.keysym
    print(key)
    if key == "Left":
        token.step = -10
        if token.x >= 10:
            token.x -= 10
        else:
            token.step = 0
    elif key == "Right":
        token.step = 10
        if token.x <= 240:
            token.x += 10
        else:
            token.step = 0

    # canvas.delete("all")
    # canvas.create_rectangle(token.x, token.y, token.x+40, token.y+10, fill='red')
    canvas.move(token_id, token.step, 0)

def ball_loop():
    ball.x += ball.step
    # ball.y += 3
    canvas.move(ball_id, ball.step, 0)
    if ball.x >= 280:
        ball.step = -2
    if ball.x <= 0:
        ball.step = 2
    window.after(10, ball_loop)


token = Token()
window = Tk()
window.geometry("300x300")

canvas = Canvas(window, bg='white', width=280, height=280)
canvas.grid(row=0, column=0)

token_id = canvas.create_rectangle(token.x, token.y, token.x+40, token.y+10, fill='red')

ball = Ball()
ball_id = canvas.create_oval(ball.x, ball.y, ball.x+ball.size, ball.y+ball.size)

window.bind('<KeyRelease>', key_pressed)

ball_loop()

window.mainloop()
