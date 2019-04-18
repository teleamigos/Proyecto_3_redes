from tkinter import *

#window init
window=Tk()
#window settings
window.title("CU waze")
window.resizable(True,False)
window.geometry("1020x1020")
window.configure(background = 'black')
#Get the image
mapa=PhotoImage(file="mapacu.gif")
widget = Label(window, image=mapa).place(x=150,y=50)
#Close the window.
window.mainloop()
