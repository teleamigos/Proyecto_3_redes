import tkinter as tk
from  StartPage import *

""" --------------------------------------------------------

class CU_Mapp : this define a window.

------------------------------------------------------------
"""
class CU_Mapp (tk.Tk):
    """__init__ : to create a window. """
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        container=tk.Frame(self)
        container.pack(side="top",fill="both",expand="True")
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.frames={}
        frame=StartPage(container,self)
        self.frames[StartPage]=frame
        frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(StartPage) # show widgets in the window.

    def show_frame(self,cont):
        """show a frame """
        frame=self.frames[cont]
        frame.tkraise()
