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
mapa_window = Label(window, image=mapa).place(x=150,y=50)
#mapa_window = Label(window, image=mapa).pack()

#In the window.
dest=Label(window,text="Where to?")
dest.place(x=450,y=0)
#Close the window.
window.mainloop()
