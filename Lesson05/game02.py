import tkinter as tk
from tkinter import messagebox
win = tk.Tk()
win.title("BLOCK")
win.geometry("405x605")
win.resizable(False, False)

can = tk.Canvas(bg="gray", width=400, height=600)
can.place(x=0, y=0)


def gameOver():
    messagebox.showinfo("Infomation", "GAME OVER")
    exit()


# 玉
ball_x = 50
ball_y = 500
bx = 5
by = -5


def drawBall():
    global ball_x, ball_y, bx, by
    can.create_oval(ball_x, ball_y, ball_x+20, ball_y+20, fill="white")
    if ball_x <= 0 or ball_x >= 380:
        bx *= -1
    if ball_y <= 0 or ball_y >= 580:
        by *= -1
    if ball_y >= 580:
        gameOver()
    if ball_y >= 480 and ball_x >= rack_x-10 and ball_x <= rack_x+10:
        by *= -1
    ball_x += bx
    ball_y -= by


# 板
rack_x = 170
keyPress_R = False
keyPress_L = False


def rightKeyPress(event):
    global keyPress_R
    keyPress_R = True


def rightKeyRelease(event):
    global keyPress_R
    keyPress_R = False


def leftKeyPress(event):
    global keyPress_L
    keyPress_L = True


def leftKeyRelease(event):
    global keyPress_L
    keyPress_L = False


win.bind("<KeyPress-Right>", rightKeyPress)
win.bind("<KeyRelease-Right>", rightKeyRelease)
win.bind("<KeyPress-Left>", leftKeyPress)
win.bind("<KeyRelease-Left>", leftKeyRelease)


def drawRacket():
    global rack_x
    can.create_rectangle(rack_x, 500, rack_x+60, 520, fill="white")
    if keyPress_R == True and rack_x <= 350:
        rack_x += 5
    if keyPress_L == True and rack_x >= -10:
        rack_x -= 5
# 表示


def gameLoop():
    can.delete("all")
    drawBall()
    drawRacket()
    win.after(30, gameLoop)


gameLoop()

win.mainloop()
