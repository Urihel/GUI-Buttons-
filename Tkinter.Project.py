import tkinter
top = tkinter.Tk()
#This creates a basic button layout

b1 = tkinter.Button(top, text ="Click Here", command = top, height = 5, width = 20)
b2 = tkinter.Button(top, text="Press Me Down", command = top, height = 5, width = 20)
b3 = tkinter.Button(top, text="Push My Buttons", command = top, height = 5, width = 20)
b4 = tkinter.Button(top, text="Push it", command = top, height = 5, width = 20)
b1.pack()
b2.pack()
b3.pack()
b4.pack()








