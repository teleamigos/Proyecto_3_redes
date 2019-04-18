from tkinter import *
from tkinter import Label

#window init
window=Tk()
#window settings
window.title("CU waze")
window.resizable(True,False)
window.geometry("1020x1020")
window.configure(background = 'black')
#Getting image
mapa=PhotoImage(file="mapacu.gif")
widget = Label(window, image=mapa).pack()
#Closing
window.mainloop()
