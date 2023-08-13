import tkinter as ttk
import customtkinter as ctk
from PIL import Image, ImageTk

window = ctk.CTk()
window.title("Lofty Database Management System | developed by vernonthedev")
window.geometry(('600x400'))
window.resizable(False, False)
window.iconbitmap("assets/icon.ico")

#defining the frames
left_frame = ctk.CTkFrame(window, corner_radius=0)
right_frame = ctk.CTkFrame(window, fg_color='#F2EA6F', corner_radius=0)

#image definitions
wallpaper_img = Image.open("assets/wallpaper.jpg")
wallpaper = ctk.CTkImage(wallpaper_img, size=(300, 600))
logo_img = Image.open("assets/manager.png")
logo = ctk.CTkImage(logo_img, size=(60,60))
login_img = Image.open("assets/login.png")
login = ctk.CTkImage(login_img)
user_img = Image.open("assets/user.png")
user = ctk.CTkImage(user_img)
passwd_img = Image.open("assets/password.png")
passd = ctk.CTkImage(passwd_img)

#my widgets
my_labe_limg = ctk.CTkLabel(left_frame, image=wallpaper,text="Lofty", font=("&MatchMaker", 50), text_color='black')


other_label = ctk.CTkLabel(right_frame, text="Lofty", image=logo, compound="right", text_color='#75163F', width=300, font=("&MatchMaker", 30))


username_entry = ctk.CTkEntry(right_frame, corner_radius=20, placeholder_text='Enter Username', placeholder_text_color='grey', font=("Quicksand Medium", 13))
password_entry = ctk.CTkEntry(right_frame, corner_radius=20, placeholder_text="Enter Password", placeholder_text_color='grey', font=("Quicksand Medium", 13))
login_btn = ctk.CTkButton(right_frame, text="Login", corner_radius=20, image=login, compound='left', fg_color='#75163F', font=("Quicksand Medium", 13), hover_color='black')


#widget packs
my_labe_limg.pack(fill='both', expand='true')


other_label.pack(pady='50')
username_entry.pack(pady='20', fill='x', padx='30')
password_entry.pack(pady='10', fill='x', padx='30')
login_btn.pack(pady='20')


#frame packs
left_frame.pack(side='left',fill='both', expand='true')
right_frame.pack(side='left',fill='both', expand='false')









window.mainloop()
