import tkinter as tk

win = tk.Tk()
win.title("BLOCK")
win.geometry("405x605")
win.resizable(False, False)

can = tk.Canvas(bg="gray", width=400, height=600)
can.place(x=0, y=0)

# 玉
ball_x = 50
ball_y = 500
bx = 5
by = -5

def drawBall():
    global ball_x
    global ball_y
    global bx
    global by
    can.create_oval(ball_x, ball_y, ball_x+20, ball_y+20, fill="white")
    if ball_x <= 0 or ball_x >= 380:
      bx *= -1
    if ball_y <= 0 or ball_y >= 580:
      by *= -1
    ball_x += bx
    ball_y -= by


def gameLoop():
    can.delete("all")
    drawBall()
    win.after(30, gameLoop)


gameLoop()

win.mainloop()
