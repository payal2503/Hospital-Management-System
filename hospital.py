from tkinter import *
from tkinter import ttk
import random
import datetime
import time
from tkinter import messagebox
# import mysql.connector


class Hospital:
    def __init__ (self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1240x800+0+0")  # width and axis


        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white", font=('times new roman',50,"bold"))
        lbltitle.pack(side=TOP, fill=X)

        #=========================Data Frame============================

        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1375, height=360)

        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=20,
                                                            font = ('arial', 12 , "bold"), text="Patient Information")
        DataframeLeft.place(x=0, y=5, width=840, height=310 )

        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=20,
                                                            font = ('arial', 12 , "bold"), text="Prescription")
        DataframeRight.place(x=845, y=5, width=480, height=310 )

        #=========================Buttons Frame============================

        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=490, width=1375, height=70)

        #=========================Details Frame============================

        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=560, width=1375, height=145)

        #=============================DataframeLeft============================

        lblNameTablet = Label(DataframeLeft, text="Names Of Tablet", font = ('arial', 12 , "bold"),padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0)

        comNametablet = ttk.Combobox(DataframeLeft, font = ('arial', 12 , "bold"),
                                                                                  width=33)
        comNametablet["values"] = ('Painkiller', 'corona Dose' ,'Vacacine', 'Ativan', 'Donafide', 'Adderall')
        comNametablet.grid(row=0, column=1)


root=Tk()
ob=Hospital(root)
root.mainloop()
