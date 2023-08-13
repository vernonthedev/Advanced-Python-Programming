import tkinter as ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from applogic import logic

#main window configurations
root = tb.Window(themename='superhero')
root.title("Lofty Database Manager | ©️ Developed by vernonthedev")
root.geometry(('900x500'))
root.iconbitmap("assets/icon.ico")

#create the main notebook
main_notebook = tb.Notebook(root, bootstyle='light')
main_notebook.pack(expand='true', fill='both')

#the notebook menu tabs
tab1 = tb.Frame(main_notebook)
tab2 = tb.Frame(main_notebook)


#custom bootstrap button styling
createDBBtnStyle = tb.Style()
createDBBtnStyle.configure('info.Outline.TButton', font=("Quicksand Medium", 10))
deleteDBBtnStyle = tb.Style()
deleteDBBtnStyle.configure('danger.Outline.TButton', font=("Quicksand Medium", 10))
showDBBtnStyle = tb.Style()
showDBBtnStyle.configure('success.Outline.TButton', font=("Quicksand Medium", 10))


heading = tb.Label(tab1, text="Welcome to Lofty Your MySQL Database Manager", font=("Quicksand Medium", 11))
sep = tb.Separator(tab1, orient=HORIZONTAL, bootstyle=INFO)
heading.pack()
sep.pack(fill='x', padx=50)

databaseGroup = tb.LabelFrame(tab1, text="Manage Your Databases Here!", height=60)
databaseGroup.place(relx=0.05, rely=0.1)

createDatabaseButton = tb.Button(databaseGroup, text="Create Database", bootstyle="INFO OUTLINE", style='info.Outline.TButton', command=logic.createDB)
dropDatabaseButton = tb.Button(databaseGroup, text="Delete Database", bootstyle="DANGER OUTLINE", style='danger.Outline.TButton')
showDatabaseButton = tb.Button(databaseGroup, text="Show Databases", bootstyle="SUCCESS OUTLINE", style='success.Outline.TButton')

#widgets aligned in tab 1
createDatabaseButton.pack(padx=10, side='left', expand='true', fill='x')
dropDatabaseButton.pack(padx=10, side='left', expand='true', fill='x')
showDatabaseButton.pack(padx=10, side='left', expand='true', fill='x')


tableGroup = tb.LabelFrame(tab1, text="Manage Your Tables Here!", height=60)
tableGroup.place(relx=0.05, rely=0.3)

createTableButton = tb.Button(tableGroup, text="Create Table", bootstyle="INFO OUTLINE", style='info.Outline.TButton')
dropTableButton = tb.Button(tableGroup, text="Delete Table", bootstyle="DANGER OUTLINE", style='danger.Outline.TButton')

createTableButton.pack(padx=10, side='left', expand='true', fill='x')
dropTableButton.pack(padx=10, side='left', expand='true', fill='x')

tableGroup = tb.LabelFrame(tab1, text="Available Table Operations", height=60)
tableGroup.place(relx=0.05, rely=0.5)

insertButton = tb.Button(tableGroup, text="Create Table", bootstyle="INFO OUTLINE", style='info.Outline.TButton')
deleteButton = tb.Button(tableGroup, text="Delete Table", bootstyle="DANGER OUTLINE", style='danger.Outline.TButton')
updateTableButton = tb.Button(tableGroup, text="Create Table", bootstyle="INFO OUTLINE", style='info.Outline.TButton')
showButton = tb.Button(tableGroup, text="Delete Table", bootstyle="DANGER OUTLINE", style='success.Outline.TButton')

insertButton.pack(padx=10, side='left', expand='true', fill='x')
deleteButton.pack(padx=10, side='left', expand='true', fill='x')
updateTableButton.pack(padx=10, side='left', expand='true', fill='x')
showButton.pack(padx=10, side='left', expand='true', fill='x')


#add the frames to the notebook
main_notebook.add(tab1, text='Menu')
main_notebook.add(tab2, text='Settings')






#run the application
root.mainloop()
