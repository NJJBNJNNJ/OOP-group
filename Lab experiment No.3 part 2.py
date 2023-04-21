from tkinter import *
import tkinter as tk

class MyWindow:
    def __init__(self, win):
        self.txt1 = Entry(win, bd=1, width= 25)
        self.txt1.insert(INSERT, "This is where i type my text")
        self.txt1.place(x=100, y=30, height= 50)


window = Tk()
mywin = MyWindow(window)
window.geometry("360x120")
window.title("Text Field")


window.mainloop()