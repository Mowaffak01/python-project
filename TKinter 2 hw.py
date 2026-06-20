from tkinter import *

from tkinter import messagebox

root = Tk()

root.geometry('300x300')

def msg():
    messagebox.showwarning('Waring! , stop virus Threat detcted! ')
    
button = Button(root ,text='scaning for virus ',command=msg)

button.place(x=50,y=90)

root.mainloop()