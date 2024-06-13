from tkinter import *
from tkinter import ttk

# going to be the parent for all variables, the window


root = Tk()
root.title("Budget Manager GUI")

label1 = ttk.Label(root, text="Label 1")
label1.grid(row=0, column=0, padx=5, pady=5)

entry1 = ttk.Entry(root, width=30)
entry1.grid(row=0, column=1, padx=5, pady=5)

label2 = ttk.Label(root, text="Label 2")
label2.grid(row=1, column=0, padx=5, pady=5)

entry2 = ttk.Entry(root, width=30)
entry2.grid(row=1, column=1, padx=5, pady=5)

label3 = ttk.Label(root, text="Label 3")
label3.grid(row=2, column=0, padx=5, pady=5)

entry3 = ttk.Entry(root, width=30)
entry3.grid(row=2, column=1, padx=5, pady=5)

button = ttk.Button(root, text="This is my button")
button.grid(row=3, column=0, padx=5, pady=5, sticky='SE')

button.config(text='PUSH me pls')


root.mainloop()
