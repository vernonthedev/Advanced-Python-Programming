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

#widgets
list_options = tb.Label(tab1, text="Lofty Options", font=("Quicksand Medium", 13))
create_database_btn = tb.Button(tab2, text="Create Database", bootstyle='outline-success')

#widget alignment and placement inside the notebook
list_options.pack(pady=50)
create_database_btn.pack(pady=50)


#add the frames to the notebook
main_notebook.add(tab1, text='Menu')
main_notebook.add(tab2, text='Table Operations')
main_notebook.add(tab3, text='CRUD Operations')


root.mainloop()
