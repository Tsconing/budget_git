from tkinter import *
from tkinter import ttk

# going to be the parent for all variables, the window


root = Tk()


button = ttk.Button(root, text="This is my button")

button.pack()

root.mainloop()
