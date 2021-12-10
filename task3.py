import tkinter as tk
from tkinter import *
from tkinter import ttk
window = tk.Tk()
window.title  ("                           Example")
window.geometry ("270x160")
dogphoto = PhotoImage(file = "dog.png")
label1 = tk.Label(window, text = "Pochacco!")
label2 = tk.Label(window, image=dogphoto)
label3 = tk.Label(window, text ="A cuddly little puppy! This is from the same\ncreators who broughtyou keropi and kero kero" )
label4 = tk.Label(window, text = "" )
label1.grid(row = 2, column = 2, sticky=W)
label2.grid(row = 2, column =1,sticky=E)
label3.grid(row = 3, column = 1,columnspan=2)
label4.grid(row = 1, column = 1)




window.mainloop()