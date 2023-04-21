from tkinter import *
import tkinter as tk

class MyWindow:
    def __init__(self,win):
        self.btn1 = tk.Button(win, text="color", fg="Red", bg="Blue", command=self.change_blue)
        self.btn1.place(x=50, y=100)
        self.cc = self.btn1.cget("background")
        self.btn2 = Button(window, text="<---Click here to change the color of the button", command=self.color)
        self.btn2.place(x=100, y=100)

    def change_blue(self):
        if self.btn1.cget("background") == self.cc:
           self.btn1.config(bg="Yellow")
        else:
           self.btn1.config(bg=self.cc)

    def color(self):
        if self.btn1.cget("background") == self.cc:
           self.btn1.config(bg="Yellow")
        else:
           self.btn1.config(bg=self.cc)

window = Tk()
mywin = MyWindow(window)
window.geometry("390x160")
window.title("Button")


window.mainloop()