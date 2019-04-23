from tkinter import *
import tkinter as tk


LARGE_FONT=("Verdana",12)

class StartPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label=tk.Label(self,text="where to...",font=LARGE_FONT)
        label.pack(pady=10,padx=10)
