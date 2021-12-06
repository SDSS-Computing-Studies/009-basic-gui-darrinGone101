import tkinter as tk
from tkinter import *
from tkinter import ttk
window = tk.Tk()
window.title  ("t-town veterianry clinic database")
searchbyname = tk.Button(window, "search by name")
label0 = tk.label(window, text =  "Client Database")
dogphoto = PhotoImage(file ="dog.png")
label1 = tk.Label(window,text="Name")
label2 = tk.Label(window,text="type")
label3 = tk.Label(window,text="Breed")
label4 = tk.Label(window,text="Owner")
label5 = tk.Label(window,text="Birthdate")
entry1 = tk.Entry(window,text="")
entry2 = tk.Entry(window,text="")
entry3 = tk.Entry(window,text="")
entry4 = tk.Entry(window,text="")
entry5 = tk.Entry(window,text="")


label1.grid(row=1, column=3)
window.mainloop()