from tkinter import *
window = Tk()

window.geometry("340x120")
window.title("Label")

lbl = Label(window,text= "Laboratory Activity 5")
lbl.place(x = 110, y = 40)

lbl = Label(window,text= "Submitted to: Mam Sayo")
lbl.place(x = 100, y = 60)

window.mainloop()