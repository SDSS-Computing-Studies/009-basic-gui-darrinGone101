import tkinter as tk
from tkinter import *
from tkinter import ttk
window = tk.Tk()
window.title  ("                       t-town veterianry clinic database")
window.geometry ("630x230")

searchbyname = tk.Button(window, text="search by name")
label0 = tk.Label(window, text =  "Client Database")
dogphoto = PhotoImage(file = "dog.png")
Name = tk.Label(window,text="Name")
Type = tk.Label(window,text="type")
Breed = tk.Label(window,text="Breed")
Owner = tk.Label(window,text="Owner")
Birthdate = tk.Label(window,text="Birthdate")
entry1 = tk.Entry(window,text="")
entry2 = tk.Entry(window,text="")
entry3 = tk.Entry(window,text="")
entry4 = tk.Entry(window,text="")
entry5 = tk.Entry(window,text="")
entry6 = tk.Entry(window,text="")
entryname = tk.Entry(window,text="")
button1 = Button(window,text="< Previous")
button2 = Button(window,text="Next >")
button3 = Button(window,text="Save Entry")
dog = tk.Label(window, image=dogphoto)
dog.grid(row = 1, column = 1, rowspan = 3)
Name.grid(row = 7, column = 1)
entry1.grid(row = 8, column = 1)
button1.grid(row = 9, column = 1, sticky = W)
entry2.grid(row = 8, column = 2)
entry3.grid(row = 8, column = 3)
entry4.grid(row = 8, column = 4)
entry5.grid(row = 8, column = 5, sticky = E)
Type.grid(row = 7, column = 2)
Breed.grid(row = 7, column = 3)
Owner.grid(row = 7, column = 4)
Birthdate.grid(row =7, column = 5)
label0.grid(row = 3, column =2, columnspan = 2)
searchbyname.grid(row = 1, column = 4, sticky = NE)
entry6.grid(row = 1, column = 5, sticky = NE)
button3.grid(row =9, column = 3)
button2.grid(row = 9, column =5, sticky = E,)



window.mainloop()