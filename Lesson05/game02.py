import tkinter as tk

win = tk.Tk()
win.title("BLOCK")
win.geometry("405x605")
win.resizable(False, False)

can = tk.Canvas(bg="gray", width=400, height=600)
can.place(x=0, y=0)

#玉
can.create_oval(50, 500, 70, 520, fill= "white")

win.mainloop()
