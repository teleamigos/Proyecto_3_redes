import tkinter as tk
#from ttk import *
from tkinter import ttk
#from Dijkstra import *
LARGE_FONT=("Verdana",12)
""" --------------------------------------------------------

class StartPage : Principal page.

------------------------------------------------------------
"""
class StartPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label=tk.Label(self,text="where are you going?",font=LARGE_FONT)#Show the Label.
        label.pack(side="top")
        self.mapa=tk.PhotoImage(file="CU.gif")# Load the image

        send_button=tk.Button(self,text = "Find Location", command = self.clickButton)
        send_button.pack()#)

        """ Create a canvas """
        self.canvas=tk.Canvas(width=790,height=580,bg="black")# Define the size shown of the image
        self.canvas.pack()
        self.canvas.create_image(0,0,image=self.mapa,anchor=tk.NW)#show the image
        self.Create_locations()#It's called  to set locations in the map.

        #""" Graph initialize  """
        #self.gra=Graph()

    def clickButton(self):
        first_button=tk.Button(self,text = "Your location",command = self.clickYourLocation)
        first_button.pack(side = "left")

        first_button=tk.Button(self,text = "Dropped location",command = self.clickDroLocation)
        first_button.pack(side = "left")

        first_button=tk.Button(self,text = "Start",command = self.clickStart)
        first_button.pack(side = "left")

    def clickYourLocation(self):
        """
        Instrucciones para boton que selecciona ubicacion actual
        """
    def clickDroLocation(self):
        """
        Instrucciones para boton que selecciona destino
        """

    def clickStart(self):
        """
        Instrucciones para boton que inicia proceso de ruta
        """

    def Create_locations(self):
        """this method  put points of location in the map """
        pumitas=self.canvas.create_oval(120,410,135,425,fill='red')
        anexo_ingenieria=self.canvas.create_oval(480,346,495,361,fill='red')
        F_economia=self.canvas.create_oval(446,26,461,41,fill='red')
        D_general_deporte=self.canvas.create_oval(55,84,70,99,fill='red')
        E_universitario=self.canvas.create_oval(167,131,182,146,fill='red')

        rectoria=self.canvas.create_oval(292,119,307,134,fill='red')
        FyLetras=self.canvas.create_oval(335,50,350,65,fill='red')
        Islas=self.canvas.create_oval(385,86,400,101,fill='red')
        F_medicina=self.canvas.create_oval(547,83,562,98,fill='red')
        F_odontologia=self.canvas.create_oval(508,36,523,51,fill='red')

        F_ingenieria=self.canvas.create_oval(405,136,420,151,fill='red')
        F_derecho=self.canvas.create_oval(446,48,461,63,fill='red')
        muca=self.canvas.create_oval(310,152,325,167,fill='red')
        F_arquitectura=self.canvas.create_oval(346,154,361,169,fill='red')
        A_olimpica=self.canvas.create_oval(393,188,408,203,fill='red')

        Direccion_cch=self.canvas.create_oval(283,210,298,225,fill='red')
        Escultura_flama=self.canvas.create_oval(293,241,308,256,fill='red')
        Museo_anatomia=self.canvas.create_oval(625,162,640,177,fill='red')
        F_MedicinaVyZ=self.canvas.create_oval(641,604,656,619,fill='red')
        Cafe76=self.canvas.create_oval(665,155,680,170,fill='red')

        Museo_morfologia=self.canvas.create_oval(635,235,650,250,fill='red')
        Posgrado_ingenieria=self.canvas.create_oval(503,275,518,290,fill='red')
        Instituto_quimica=self.canvas.create_oval(588,288,603,303,fill='red')
        Instituto_geofisica=self.canvas.create_oval(679,295,694,310,fill='red')
        Instituto_fisica=self.canvas.create_oval(641,370,656,385,fill='red')

        F_ciencias=self.canvas.create_oval(551,385,566,400,fill='red')
        Trabajo_social=self.canvas.create_oval(335,404,350,419,fill='red')
        M_universidad=self.canvas.create_oval(747,384,762,399,fill='red')
        MB_universidad=self.canvas.create_oval(287,406,302,421,fill='red')
        Instituto_ecologia=self.canvas.create_oval(154,474,169,489,fill='red')



        p1=self.canvas.create_oval(76,92,86,102,fill='blue')
        p2=self.canvas.create_oval(106,63,116,73,fill='blue')
        p3=self.canvas.create_oval(200,53,210,63,fill='blue')
        p4=self.canvas.create_oval(132,447,142,457,fill='blue')
        p5=self.canvas.create_oval(245,113,255,123,fill='blue')

        p6=self.canvas.create_oval(351,178,361,188,fill='blue')
        p7=self.canvas.create_oval(410,167,420,177,fill='blue')
        p8=self.canvas.create_oval(316,180,326,190,fill='blue')
        p9=self.canvas.create_oval(523,170,533,180,fill='blue')
        p10=self.canvas.create_oval(257,192,267,202,fill='blue')

        p11=self.canvas.create_oval(560,170,570,180,fill='blue')
        p12=self.canvas.create_oval(575,213,585,223,fill='blue')
        p13=self.canvas.create_oval(246,46,256,56,fill='blue')
        p14=self.canvas.create_oval(340,30,350,40,fill='blue')
        p15=self.canvas.create_oval(513,24,523,34,fill='blue')

        p16=self.canvas.create_oval(604,64,614,74,fill='blue')
        p17=self.canvas.create_oval(596,137,606,147,fill='blue')
        p18=self.canvas.create_oval(450,389,460,399,fill='blue')
        p19=self.canvas.create_oval(578,255,588,265,fill='blue')
        p2o=self.canvas.create_oval(321,419,331,429,fill='blue')

        p16=self.canvas.create_oval(165,404,175,414,fill='blue')
        p17=self.canvas.create_oval(213,377,223,387,fill='blue')
        p18=self.canvas.create_oval(279,360,289,370,fill='blue')
        p19=self.canvas.create_oval(388,423,398,433,fill='blue')
        p20=self.canvas.create_oval(705,229,715,239,fill='blue')

        p21=self.canvas.create_oval(718,325,728,335,fill='blue')
        p22=self.canvas.create_oval(714,365,724,375,fill='blue')
        p23=self.canvas.create_oval(680,393,690,403,fill='blue')
        p24=self.canvas.create_oval(623,457,633,467,fill='blue')
        p25=self.canvas.create_oval(530,290,540,300,fill='blue')

        p26=self.canvas.create_oval(716,299,726,309,fill='blue')
        p27=self.canvas.create_oval(545,434,555,444,fill='blue')
