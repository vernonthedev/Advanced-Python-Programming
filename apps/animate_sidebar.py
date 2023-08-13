import customtkinter as ctk
from PIL import Image, ImageTk


#the slide menu class
class SlidePanel(ctk.CTkFrame):
    def  __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent)

        #the general attributes
        self.start_pos = start_pos + 0.04
        self.end_pos = end_pos - 0.03
        self.width = abs(start_pos - end_pos)

        #animation logic
        self.pos = self.start_pos
        self.in_start_pos = True

        #layout
        self.place(relx=self.start_pos, rely=0.05, relwidth=self.width , relheight=0.9)

    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()

    def animate_forward(self):
        if self.pos > self.end_pos:
            self.pos -= 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width , relheight=0.9)
            self.after(10, self.animate_forward)
        else:
            self.in_start_pos = False

    def animate_backwards(self):
        if self.pos < self.start_pos:
            self.pos += 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width , relheight=0.9)
            self.after(10, self.animate_backwards)
        else:
            self.in_start_pos = True



#the window
window = ctk.CTk()
window.title("Animated Sidebar | vernonthedev")
window.geometry('600x400')
ctk.set_appearance_mode('dark')

#image importations
menuImage = Image.open('U:\\.advancedpython\\apps\\menu.png')
menuTkImage = ctk.CTkImage(menuImage)

dashboardImage = Image.open('U:\\.advancedpython\\apps\\dashboard.png')
dashboardTkImage = ctk.CTkImage(dashboardImage)

homeImage = Image.open('U:\\.advancedpython\\apps\\home.png')
homeTkImage = ctk.CTkImage(homeImage)

toolsImage = Image.open('U:\\.advancedpython\\apps\\tools.png')
toolsTkImage = ctk.CTkImage(toolsImage)

exitImage = Image.open('U:\\.advancedpython\\apps\\exit.png')
exitTkImage = ctk.CTkImage(exitImage)


#animated widget
animatedPanel = SlidePanel(window, 1.0, 0.7)
ctk.CTkLabel(animatedPanel, text="CodersLounge", font=("&MatchMaker", 19)).pack(expand=True, fill='both', padx=2)
ctk.CTkButton(animatedPanel, text='Dashboard',font=("Trebuchet MS", 13), corner_radius=0, image=dashboardTkImage, compound='left').pack(expand=True, fill='both')
ctk.CTkButton(animatedPanel, text='Home',font=("Trebuchet MS", 13) ,corner_radius=0, image=homeTkImage, compound='left').pack(expand=True, fill='both')
ctk.CTkButton(animatedPanel, text='Tools',font=("Trebuchet MS", 13) ,corner_radius=0, image=toolsTkImage, compound='left').pack(expand=True, fill='both')
ctk.CTkButton(animatedPanel, text='Exit', font=("Trebuchet MS", 13),image=exitTkImage, compound='left').pack(expand=True, fill='both', pady=2)


menuBtn = ctk.CTkButton(window, text="Menu", font=("Trebuchet MS", 13),command=animatedPanel.animate, corner_radius=0, image=menuTkImage, compound="left")
menuBtn.place(relx=0.0, rely=0.0, )







# run the app
window.mainloop()
