from CU_Mapp import *
from StartPage import *
from tkinter import*

app=CU_Mapp()
photo=tk.PhotoImage(file="mapacu.gif")
image_shown=tk.Label(app,image=photo).pack(side="top")

app.mainloop()
