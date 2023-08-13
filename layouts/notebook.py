import tkinter as ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

#main window configurations
root = tb.Window(themename='flatly')
root.title("Lofty Notebook")
root.geometry(('900x500'))
root.iconbitmap("assets/icon.ico")

#create the main notebook
main_notebook = tb.Notebook(root, bootstyle='warning')
main_notebook.pack(expand='true', fill='both')

#the notebook menu tabs
tab1 = tb.Frame(main_notebook)
tab2 = tb.Frame(main_notebook)
tab3 = tb.Frame(main_notebook)

#custom bootstrap button styling
createDBBtnStyle = tb.Style()
createDBBtnStyle.configure('info.Outline.TButton', font=("Quicksand Medium", 10))
deleteDBBtnStyle = tb.Style()
deleteDBBtnStyle.configure('danger.Outline.TButton', font=("Quicksand Medium", 10))
showDBBtnStyle = tb.Style()
showDBBtnStyle.configure('success.Outline.TButton', font=("Quicksand Medium", 10))

#=========================TAB 2=========================================
#widgets in tab 1
heading = tb.Label(tab1, text="Welcome to Lofty", font=("Quicksand Medium", 11))
sep = tb.Separator(tab1, orient=HORIZONTAL, bootstyle=INFO)
heading.pack()
sep.pack(fill='x', padx=50)

databaseGroup = tb.LabelFrame(tab1, text="Manage Your Databases Here!", height=60)
databaseGroup.place(relx=0.05, rely=0.1)

createDatabaseButton = tb.Button(databaseGroup, text="Create Database", bootstyle="INFO OUTLINE", style='info.Outline.TButton')
dropDatabaseButton = tb.Button(databaseGroup, text="Delete Database", bootstyle="DANGER OUTLINE", style='danger.Outline.TButton')
showDatabaseButton = tb.Button(databaseGroup, text="Show Databases", bootstyle="SUCCESS OUTLINE", style='success.Outline.TButton')

#widgets aligned in tab 1
createDatabaseButton.pack(padx=10, side='left', expand='true', fill='x')
dropDatabaseButton.pack(padx=10, side='left', expand='true', fill='x')
showDatabaseButton.pack(padx=10, side='left', expand='true', fill='x')

#=========================TAB 2=========================================
#widgets in tab 2
headingTab2 = tb.Label(tab2, text="Welcome to Lofty", font=("Quicksand Medium", 11))
sepTab2 = tb.Separator(tab2, orient=HORIZONTAL, bootstyle=INFO)
headingTab2.pack()
sepTab2.pack(fill='x', padx=50)

tableGroup = tb.LabelFrame(tab2, text="Manage Your Tables Here!", height=60)
tableGroup.place(relx=0.05, rely=0.1)

createTableButton = tb.Button(tableGroup, text="Create Table", bootstyle="INFO OUTLINE", style='info.Outline.TButton')
dropTableButton = tb.Button(tableGroup, text="Delete Table", bootstyle="DANGER OUTLINE", style='danger.Outline.TButton')
#widgets aligned in tab 2
createTableButton.pack(padx=10, side='left', expand='true', fill='x')
dropTableButton.pack(padx=10, side='left', expand='true', fill='x')






#add the frames to the notebook
main_notebook.add(tab1, text='Menu')
main_notebook.add(tab2, text='Table Operations')
main_notebook.add(tab3, text='CRUD Operations')

#run the application
root.mainloop()
