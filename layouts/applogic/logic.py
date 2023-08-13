import ttkbootstrap as tb
import tkinter as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview
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
