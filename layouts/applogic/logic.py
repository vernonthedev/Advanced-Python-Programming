import ttkbootstrap as tb
import tkinter as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview
import customtkinter as ctk
#=================MY FUNCTIONS=======================

def createDB():
    app = tb.Toplevel("Create New Database")
    app.geometry(('600x100'))
    app.resizable(False, False)
    app.iconbitmap('assets/icon.ico')

    #the ui for the create database window
    data = tb.Label(app, text="Enter Database Name:",font=("Quicksand Medium", 7))
    databaseName = tb.Entry(app)
    createbutton = tb.Button(app, bootstyle="success-outline", text="Create")

    data.pack(side='left', padx=5)
    databaseName.pack(side='left', fill='x', expand='true', padx=5)
    createbutton.pack(side='bottom', expand='true', padx=5)

    app.mainloop()


def dropDB():
    app = tb.Toplevel("Delete Existing Database")
    app.geometry(('600x100'))
    app.resizable(False, False)
    app.iconbitmap('assets/icon.ico')

    #the ui for the create database window
    data = tb.Label(app, text="Enter Database Name:",font=("Quicksand Medium", 7))
    databaseName = tb.Entry(app)
    createbutton = tb.Button(app, bootstyle="danger-outline", text="Delete")

    data.pack(side='left', padx=5)
    databaseName.pack(side='left', fill='x', expand='true', padx=5)
    createbutton.pack(side='bottom', expand='true', padx=5)

    app.mainloop()

def showDBs():
    app = tb.Toplevel("Available MySQL Databases")
    app.geometry(('600x400'))
    app.resizable(False, False)
    app.iconbitmap('assets/icon.ico')

    #the column row data
    coldata =[
        {"text": "No."},
        {"text":"Database Name"}
    ]

    table = Tableview(master=app, coldata=coldata, rowdata="", paginated=True, bootstyle="success",)
    table.pack(expand='true', fill='both')

    app.mainloop()


#table operations
def createTableWindow():
    app = tb.Toplevel("Create New Table")
    app.geometry(('600x600'))
    app.resizable(False, False)
    app.iconbitmap('assets/icon.ico')

    mainFrame = tb.Frame(app)
    mainFrame.pack(side='left',fill='both', expand='false')


    tableName = ctk.CTkEntry(mainFrame, corner_radius=0, placeholder_text='Enter Table Name', font=("Quicksand Medium", 13))
    coderId = ctk.CTkEntry(mainFrame,corner_radius=0, placeholder_text='Enter Coder\'s Id', font=("Quicksand Medium", 13))
    firstName = ctk.CTkEntry(mainFrame,corner_radius=0, placeholder_text='Enter First Name', font=("Quicksand Medium", 13))
    lastName = ctk.CTkEntry(mainFrame,corner_radius=0, placeholder_text='Enter Last Name', font=("Quicksand Medium", 13))
    gender = ctk.CTkEntry(mainFrame,corner_radius=0, placeholder_text='Enter Gender', font=("Quicksand Medium", 13))
    phoneNumber = ctk.CTkEntry(mainFrame,corner_radius=0,placeholder_text='Enter Phone Number', font=("Quicksand Medium", 13))
    location = ctk.CTkEntry(mainFrame,corner_radius=0, placeholder_text='Enter Location', font=("Quicksand Medium", 13))
    createbutton = tb.Button(mainFrame, bootstyle="success-outline", text="Create Table")

    tableName.pack(pady='20', fill='x', padx='30')
    coderId.pack(pady='10', fill='x', padx='30')
    firstName.pack(pady='10', fill='x', padx='30')
    lastName.pack(pady='10', fill='x', padx='30')
    gender.pack(pady='10', fill='x', padx='30')
    phoneNumber.pack(pady='10', fill='x', padx='30')
    location.pack(pady='10', fill='x', padx='30')

    createbutton.pack(pady='20')


    mainFrame.pack(expand='true', fill='x', pady=5)


    app.mainloop()


#the logic to drop the available table
def dropTable():
    app = tb.Toplevel("Delete Existing Table")
    app.geometry(('600x100'))
    app.resizable(False, False)
    app.iconbitmap('assets/icon.ico')

    #the ui for the create database window
    data = tb.Label(app, text="Enter Table Name:",font=("Quicksand Medium", 7))
    databaseName = tb.Entry(app)
    createbutton = tb.Button(app, bootstyle="danger-outline", text="Delete")

    data.pack(side='left', padx=5)
    databaseName.pack(side='left', fill='x', expand='true', padx=5)
    createbutton.pack(side='bottom', expand='true', padx=5)

    app.mainloop()


def showTables():
    app = tb.Toplevel("List of Available Tables")
    app.geometry(('600x500'))
    app.resizable(False, False)
    app.iconbitmap('assets/icon.ico')

    #the ui for the create database window
    data = tb.Label(app, text="Enter Database Name:",font=("Quicksand Medium", 7))
    databaseName = tb.Entry(app)
    createbutton = tb.Button(app, bootstyle="success-outline", text="Search")

    data.pack(padx=5)
    databaseName.pack(fill='x', expand='true', padx=20)
    createbutton.pack(expand='true', padx=5)


    #the column row data
    coldata =[
        {"text": "No."},
        {"text":"Table Name"}
    ]

    table = Tableview(master=app, coldata=coldata, rowdata="", paginated=True, bootstyle="success",)
    table.pack(expand='true', fill='both')

    app.mainloop()
