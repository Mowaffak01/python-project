
from tkinter import *

window = Tk()
window.title('Homework Tkinter')
window.geometry('400x400')

greeting = Label(text="Hello person", fg='red', bg='blue')
button = Button(text="press me", bg='black', fg='white')
entry = Entry(fg="black", bg="blue", width=50)

greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()

label = Label(master=frame, text='A random frame')
label.pack()

textbox = Text(fg='green', bg='yellow')
textbox.pack()


window.mainloop()
