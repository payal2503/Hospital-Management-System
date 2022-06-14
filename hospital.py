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
        self.root.geometry("1540x800+0+0")  # width and axis


        lbltitle=Label(self.root, bd=20, relief=RIDGE, text="Hospital Management System", fg="red", bg="white", font=('times new roman',50,"bold"))
        lbltitle.pack(side=TOP,fill=X)


root=Tk()
ob=Hospital(root)
root.mainloop()
