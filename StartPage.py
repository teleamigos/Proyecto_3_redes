import tkinter as tk


LARGE_FONT=("Verdana",12)
""" --------------------------------------------------------

class StartPage : Principal page.

------------------------------------------------------------
"""
""" --------------------------------------------------------

NOTA : Modificar la linea 23 para meter el nuevo mapa.
        Modificar la linea 28 para cambiar el tamaño y se ajuste al nuevo mapa
        Modificar la función Create_locations para agregar mas locaciones.

------------------------------------------------------------
"""
class StartPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label=tk.Label(self,text="where are you going?",font=LARGE_FONT)#Show the Label.
        label.pack(side="top")
        self.mapa=tk.PhotoImage(file="mapacu.gif")# Load the image
        send_button=tk.Button(self,text="Let's Go!")# Show a button to send info.
        send_button.pack(side="top")
        """ Create a canvas """
        self.canvas=tk.Canvas(width=500,height=500,bg="black")# Define the size shown of the image
        self.canvas.pack()
        self.canvas.create_image(0,0,image=self.mapa,anchor=tk.NW)#show the image
        self.Create_locations()#It's called  to set locations in the map.

    def Create_locations(self):
        """this method is setting points of location in the map """
        """NOTA : Modifica este codigo para agregar los puntos de localización. """
        c_deportivo=self.canvas.create_oval(145,361,157,374,fill='blue')
        veterinaria=self.canvas.create_oval(480,346,493,357,fill='blue')
