from tkinter import *
from tkinter import messagebox

class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text="Prelim")
        self.lbl1.place(x=100, y=50)
        self.lbl2 = Label(win, text="Midterm")
        self.lbl2.place(x=100, y=100)
        self.lbl3 = Label(win, text="Finals")
        self.lbl3.place(x=100, y=150)
        self.lbl4 = Label(win, text="Grade")
        self.lbl4.place(x=100, y=200)
        self.txt1 = Entry(win, bd=1)
        self.txt1.place(x=200, y=50)
        self.txt2 = Entry(win, bd=1)
        self.txt2.place(x=200, y=100)
        self.txt3 = Entry(win, bd=1)
        self.txt3.place(x=200, y=150)
        self.txt4 = Entry(win, bd=1)
        self.txt4.place(x=200, y=200)
        self.btnclr = Button(win, text="Clear")
        self.btnclr.place(x=350, y=50)
        self.btnclr.bind('<Button-1>', self.clr)
        self.btnadd = Button(win, text="Addition")
        self.btnadd.place(x=350, y=100)
        self.btnadd.bind('<Button-1>', self.add)

    def add(self, add):
        self.txt4.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        num3 = int(self.txt3.get())
        prelim = num1 * 0.3
        midterm = num2 * 0.3
        final = num3 * 0.4
        result = prelim + midterm + final
        self.txt4.insert(END, str(result))

        if result >= 75:
            messagebox.showinfo("Result", "You passed!")
        else:
            messagebox.showinfo("Result", "You failed.")

    def clr(self, clr):
        self.txt1.delete(0, 'end')
        self.txt2.delete(0, 'end')
        self.txt3.delete(0, 'end')
        self.txt4.delete(0, 'end')

window = Tk()
mywin = MyWindow(window)
window.geometry("600x400+10+10")
window.title("Grade Calculator")
window.mainloop()