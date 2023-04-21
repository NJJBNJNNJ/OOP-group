from tkinter import *
import tkinter as tk

class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text="Charles Babage", bg = "Cyan", font = "Calibri, 26")
        self.lbl1.place(x=60, y=50)


window = Tk()
mywin = MyWindow(window)
window.geometry("390x160")
window.title("Father of computer")


window.mainloop()