from cProfile import label
from cgitb import text
from ctypes import sizeof
from tkinter import *
from tkinter import ttk
import random
import datetime
import time
from tkinter import messagebox
from tkinter import font
from turtle import width
# import mysql.connector


class Hospital:
    def __init__ (self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1240x800+0+0")  # width and axis


        self.Nameoftablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()      
        self.sideEffect = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowToUseMedication = StringVar()
        self.PatientId = StringVar()
        self.nhsNumber = StringVar()
        self.PatientName = StringVar()      
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()      






        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white", font=('times new roman',50,"bold"))
        lbltitle.pack(side=TOP, fill=X)

        #========================= Data Frame ============================

        Dataframe = Frame(self.root, bd=18, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1375, height=360)

        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=18,
                                                            font = ('arial', 12 , "bold"), text="Patient Information")
        DataframeLeft.place(x=0, y=5, width=930, height=310 )

        DataframeRight = LabelFrame(Dataframe, bd=9, relief=RIDGE, padx=20,
                                                            font = ('arial', 12 , "bold"), text="Prescription")
        DataframeRight.place(x=935, y=5, width=400, height=310 )

        #========================= Buttons Frame ============================

        Buttonframe = Frame(self.root, bd=18, relief=RIDGE)
        Buttonframe.place(x=0, y=490, width=1375, height=70)

        #========================= Details Frame ============================

        Detailsframe = Frame(self.root, bd=17, relief=RIDGE)
        Detailsframe.place(x=0, y=560, width=1380, height=139)

        #============================= Dataframe Left ============================

        lblNameTablet = Label(DataframeLeft, text="Tablet Names", font = ('arial', 12 , "bold"),padx=2, pady=5)
        lblNameTablet.grid(row=0, column=0, sticky=W)

        comNametablet = ttk.Combobox(DataframeLeft, textvariable=self.Nameoftablets, state='readonly', font = ('arial', 12 , "bold"),
                                                                                  width=31)
        comNametablet["values"] = ('Painkiller', 'corona Dose' ,'Vacacine', 'Ativan', 'Donafide', 'Adderall')
        comNametablet.current(0)
        comNametablet.grid(row=0, column=1,  )

        lblref = Label(DataframeLeft, text="Reference no:", font = ('arial', 12 , "bold"),padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(DataframeLeft,textvariable=self.ref, font = ('arial', 13 , "bold"), width=33)
        txtref.grid(row=1, column=1)

        lblDose = Label(DataframeLeft, text="Dose: ", font = ('arial', 12 , "bold"),padx=2, pady=5)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataframeLeft, textvariable=self.DailyDose, font = ('arial', 13 , "bold"), width=33)
        txtDose.grid(row=2, column=1)

        lblNoOfTablets = Label(DataframeLeft, text="No of Tablets: ", font = ('arial', 12 , "bold"),padx=2, pady=4)
        lblNoOfTablets.grid(row=3, column=0, sticky=W)
        txtNoOfTablets = Entry(DataframeLeft, textvariable=self.NumberofTablets, font = ('arial', 13 , "bold"), width=33)
        txtNoOfTablets.grid(row=3, column=1)

        lblLot = Label(DataframeLeft, font = ('arial', 12, 'bold'), text='Lot: ', padx=2,pady=5)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(DataframeLeft, textvariable=self.Lot, font = ('arial', 13, 'bold'), width=33)
        txtLot.grid(row=4, column=1)

        lblissueDate = Label(DataframeLeft, font = ('arial', 12, 'bold'), text='Issue Date', padx=2,pady=4)
        lblissueDate.grid(row=5, column=0, sticky=W)
        txtissueDate = Entry(DataframeLeft, textvariable=self.Issuedate, font = ('arial', 13, 'bold'), width=33)
        txtissueDate.grid(row=5, column=1)

        lblExpDate = Label(DataframeLeft, font = ('arial', 12, 'bold'), text='Exp Date', padx=2,pady=4)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(DataframeLeft, textvariable=self.ExpDate, font = ('arial', 13, 'bold'), width=33)
        txtExpDate.grid(row=6, column=1)

        lbldailyDose = Label(DataframeLeft, font = ('arial', 12, 'bold'), text='Daily Dose: ', padx=2,pady=4)
        lbldailyDose.grid(row=7, column=0, sticky=W)
        txtdailyDose = Entry(DataframeLeft, textvariable=self.DailyDose, font = ('arial', 13, 'bold'), width=33)
        txtdailyDose.grid(row=7, column=1)

        lblsideEffect = Label(DataframeLeft, font = ('arial', 12, 'bold'), text='Side Effect: ', padx=2,pady=4)
        lblsideEffect.grid(row=8, column=0, sticky=W)
        txtsideEffect = Entry(DataframeLeft, textvariable=self.sideEffect, font = ('arial', 13, 'bold'), width=33)
        txtsideEffect.grid(row=8, column=1)

        lblfurtherInfo = Label(DataframeLeft, font = ('arial', 12, 'bold'), text='    Further Info:', padx=2,pady=4)
        lblfurtherInfo.grid(row=0, column=2, sticky=W)
        txtfurtherInfo = Entry(DataframeLeft, textvariable=self.FurtherInformation, font = ('arial', 13, 'bold'), width=33)
        txtfurtherInfo.grid(row=0, column=3)

        lblBloodPressure = Label(DataframeLeft, font = ('arial', 12, 'bold'), text='    Blood Pressure:', padx=2,pady=4)
        lblBloodPressure.grid(row=1, column=2, sticky=W)
        txtBloodPressure = Entry(DataframeLeft, textvariable=self.DrivingUsingMachine, font = ('arial', 13, 'bold'), width=33)
        txtBloodPressure.grid(row=1, column=3)

        lblstorageAdvice = Label(DataframeLeft, font = ('arial', 12, 'bold'), text='    Storage Advice:', padx=2,pady=4)
        lblstorageAdvice.grid(row=2, column=2, sticky=W)
        txtstorageAdvice = Entry(DataframeLeft, textvariable=self.StorageAdvice, font = ('arial', 13, 'bold'), width=33)
        txtstorageAdvice.grid(row=2, column=3)

        lblMedication = Label(DataframeLeft, font = ('arial', 12, 'bold'), text='    Medication:', padx=2,pady=4)
        lblMedication.grid(row=3, column=2, sticky=W)
        txtMedication = Entry(DataframeLeft,textvariable=self.HowToUseMedication,  font = ('arial', 13, 'bold'), width=33)
        txtMedication.grid(row=3, column=3)

        lblPID = Label(DataframeLeft, font = ('arial', 12, 'bold'), text='    Patient ID:', padx=2,pady=4)
        lblPID.grid(row=4, column=2, sticky=W)
        txtPID = Entry(DataframeLeft, textvariable=self.PatientId, font = ('arial', 13, 'bold'), width=33)
        txtPID.grid(row=4, column=3)

        lblNHSnumber = Label(DataframeLeft, font = ('arial', 12, 'bold'), text='    NHS Number:', padx=2,pady=4)
        lblNHSnumber.grid(row=5, column=2, sticky=W)
        txtNHSnumber = Entry(DataframeLeft, textvariable=self.nhsNumber, font = ('arial', 13, 'bold'), width=33)
        txtNHSnumber.grid(row=5, column=3)
 
        lblPName = Label(DataframeLeft, font = ('arial', 12, 'bold'), text='    Patient Name:', padx=2,pady=4)
        lblPName.grid(row=6, column=2, sticky=W) 
        txtPName = Entry(DataframeLeft, textvariable=self.PatientName, font = ('arial', 13, 'bold'), width=33)
        txtPName.grid(row=6, column=3)
        
        lblDOB = Label(DataframeLeft, font = ('arial', 12, 'bold'), text='    Date Of Birth:', padx=2,pady=4)
        lblDOB.grid(row=7, column=2, sticky=W)
        txtDOB = Entry(DataframeLeft, textvariable=self.DateOfBirth, font = ('arial', 13, 'bold'), width=33)
        txtDOB.grid(row=7, column=3)

        lblPaddress = Label(DataframeLeft, font = ('arial', 12, 'bold'), text='    Patient Address:', padx=2,pady=4)
        lblPaddress.grid(row=8, column=2, sticky=W)
        txtPaddress = Entry(DataframeLeft,textvariable=self.PatientAddress, font = ('arial', 13, 'bold'), width=33)
        txtPaddress.grid(row=8, column=3)


        #======================================= DataFrame Right ====================================

        self.txtPrescription = Text(DataframeRight, font = ('arial', 12,'bold'), width=38, height=14,padx=2,pady=5)
        self.txtPrescription.grid(row=0,column=0)

        #======================================= Buttons ====================================

        btnPrescription = Button(Buttonframe, text= "Prescription", bg="green", fg="white", font = ("arial",12,"bold"), width=22, height=1, padx=2, pady=5 )
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(Buttonframe, text= "Prescription Data", bg="green", fg="white", font = ("arial",12,"bold"), width=22, height=1, padx=2, pady=5 )
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, text= "Update", bg="green", fg="white", font = ("arial",12,"bold"), width=21, height=1, padx=2, pady=5 )
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, text= "Delete", bg="green", fg="white", font = ("arial",12,"bold"), width=21, height=1, padx=2, pady=5 )
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe, text= "Clear", bg="green", fg="white", font = ("arial",12,"bold"), width=21, height=1, padx=2, pady=5 )
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe, text= "Exit", bg="green", fg="white", font = ("arial",12,"bold"), width=20, height=1, padx=2, pady=5 )
        btnExit.grid(row=0, column=5)

        #====================================== Table ===================================

        #============= Scrollbar ============

        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)

        self.hospital_table = ttk.Treeview(Detailsframe, column=("nameoftable",
                                                                    "ref",'dose','nooftablets','lot','issuedate',
                                                                    'expdate','dailydose','storage','nhsnumber',
                                                                    'pname','dob','address'),xscrollcommand=scroll_y.set, yscrollcommand=scroll_x.set)

        scroll_x.pack (side=BOTTOM, fill=X)
        scroll_y.pack (side=RIGHT, fill=Y)

        scroll_x =ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y =ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable",text="Name Of Tablets")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No Of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table['show']='headings'


        self.hospital_table.column("nameoftable",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=90)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=90)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=90)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=90)
        self.hospital_table.column("address",width=90)


        self.hospital_table.pack(fill=BOTH, expand=1)


        #================================== functionality declaration =================================

        



root=Tk()
ob=Hospital(root)
root.mainloop()
