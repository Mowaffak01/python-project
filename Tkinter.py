import Tkinter as tk

window=tk.Tk()

for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RASIED,
            borderwidth=1
                       
        )
frame.grid(row=i,collum=j,padx=5,padx=5)
label = tk.label(master=frame,text=f"Row{i}\ncollum{j}")
label.pack

window.mainloop()
           
