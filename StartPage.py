import tkinter as tk


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
        send_button=tk.Button(self,text="Let's Go!")# Show a button to send info.
        send_button.pack(side="top")
        """ Create a canvas """
        self.canvas=tk.Canvas(width=790,height=580,bg="black")# Define the size shown of the image
        self.canvas.pack()
        self.canvas.create_image(0,0,image=self.mapa,anchor=tk.NW)#show the image
        self.Create_locations()#It's called  to set locations in the map.

    def Create_locations(self):
        """this method  put points of location in the map """
        pumitas=self.canvas.create_oval(120,410,130,420,fill='blue')
        anexo_ingenieria=self.canvas.create_oval(480,346,490,356,fill='blue')
        F_economia=self.canvas.create_oval(446,26,456,36,fill='blue')
        D_general_deporte=self.canvas.create_oval(55,84,65,94,fill='blue')
        E_universitario=self.canvas.create_oval(167,131,177,141,fill='blue')

        rectoria=self.canvas.create_oval(292,119,302,129,fill='blue')
        FyLetras=self.canvas.create_oval(335,50,345,60,fill='blue')
        Islas=self.canvas.create_oval(385,86,395,96,fill='blue')
        F_medicina=self.canvas.create_oval(547,83,557,93,fill='blue')
        F_odontologia=self.canvas.create_oval(508,36,518,46,fill='blue')

        F_ingenieria=self.canvas.create_oval(405,136,415,146,fill='blue')
        F_derecho=self.canvas.create_oval(446,48,456,58,fill='blue')
        muca=self.canvas.create_oval(310,152,320,162,fill='blue')
        F_arquitectura=self.canvas.create_oval(346,154,356,164,fill='blue')
        A_olimpica=self.canvas.create_oval(393,188,403,198,fill='blue')

        Direccion_cch=self.canvas.create_oval(283,210,293,220,fill='blue')
        Escultura_flama=self.canvas.create_oval(293,241,303,251,fill='blue')
        Museo_anatomia=self.canvas.create_oval(625,162,635,172,fill='blue')
        F_MedicinaVyZ=self.canvas.create_oval(641,604,651,614,fill='blue')
        Cafe76=self.canvas.create_oval(665,155,675,165,fill='blue')

        Museo_morfologia=self.canvas.create_oval(635,235,645,245,fill='blue')
        Posgrado_ingenieria=self.canvas.create_oval(503,275,513,285,fill='blue')
        Instituto_quimica=self.canvas.create_oval(588,288,598,298,fill='blue')
        Instituto_geofisica=self.canvas.create_oval(679,295,689,305,fill='blue')
        Instituto_fisica=self.canvas.create_oval(641,370,651,380,fill='blue')

        F_ciencias=self.canvas.create_oval(551,385,561,395,fill='blue')
        Trabajo_social=self.canvas.create_oval(335,404,345,414,fill='blue')
        M_universidad=self.canvas.create_oval(747,384,757,394,fill='blue')
        MB_universidad=self.canvas.create_oval(287,406,297,416,fill='blue')
        Instituto_ecologia=self.canvas.create_oval(154,474,164,484,fill='blue')



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
