import tkinter

top = tkinter.Tk()

#This creates a basic button layout
b1 = tkinter.Button(top, text ="Click Here", command = top, height = 3, width = 14,
                    bd = 3, activebackground = 'white', font = ('Times',14))
b2 = tkinter.Button(top, text="Press Me Down", command = top, height = 3, width = 14,
                    bd = 3, activebackground = 'green', font = ('Times',14))
b3 = tkinter.Button(top, text="Push My Buttons", command = top, height = 3, width = 14,
                    bd = 3, activebackground = 'gray', font = ('Times',14))
b4 = tkinter.Button(top, text="Push it", command = top, height = 3, width = 14,
                    bd = 3, activebackground = 'grey', font = ('Times',14))
b1.pack()
b2.pack()
b3.pack()
b4.pack()

#will change the background of button completely
b1.configure(bg="#00D1FF")
b2.configure(bg="#78FF00")
b3.configure(bg="#FF0042")
b4.configure(bg="#FF3200")
