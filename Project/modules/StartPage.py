import tkinter as tk
from PIL import Image, ImageTk
from modules.AdminPasswordWindow import AdminPasswordWindow
from modules.LoginPage import LoginPage
from modules.SecondPage import SecondPage
from modules.FourthPage import FourthPage
from modules.FifthPage import FifthPage
from modules.SixthPage import SixthPage

# main page    
class StartPage(tk.Frame):
    def __init__(self, parent, controller, db_manager):
        tk.Frame.__init__(self, parent)
        self.configure(bg = '#d398fa')
        
        # load the image using PhotoImage
        self.image_path = "D:\\Documents\\Facultate\\Software Engineering\\Project\\assets\\background.png"
        self.photo = self.load_and_resize_image(1080, 720)

        # create a label to display the image as the background
        self.background_label = tk.Label(self, image=self.photo)
        self.background_label.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        # login button
        Login = tk.Button(
            self,
            text = "Login",
            command = lambda: controller.show_frame(LoginPage),
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 40,
            height = 2,
            anchor = 'center'
            # borderwidth = 8
        )
        Login.place(relx = 0.5, rely = 0.2565, anchor = "center")

        # user management button
        UserM = tk.Button(
            self,
            text = "User management",
            command = lambda: controller.show_frame(SecondPage),
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 40,
            height = 2,
            anchor = 'center'
        )
        UserM.place(relx = 0.5, rely = 0.334, anchor = "center")
        
        # sensor management button
        SensorM = tk.Button(
            self,
            text = "Sensor management",
            command =  lambda: self.admin_pass_request(controller, FourthPage),
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 40,
            height = 2,
            anchor = 'center'
        )
        SensorM.place(relx = 0.5, rely = 0.4115, anchor = "center")
       
        # room management button
        RoomM = tk.Button(
            self,
            text = "Room management",
            command =  lambda: self.admin_pass_request(controller, FifthPage),
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 40,
            height = 2,
            anchor = 'center'
        )
        RoomM.place(relx = 0.5, rely = 0.4895, anchor = "center")
        
        # monitoring button
        Monitor = tk.Button(
            self,
            text = "Monitoring",
            command = lambda: self.admin_pass_request(controller, SixthPage),
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 40,
            height = 2,
            anchor = 'center'
        )
        Monitor.place(relx = 0.5, rely = 0.5675, anchor = "center")
       
        # exit button
        Exit = tk.Button(
            self,
            text = "Exit",
            command = controller.exit_application,
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 40,
            height = 2,
            anchor = 'center'
        )
        Exit.place(relx = 0.5, rely = 0.6455, anchor = "center")

        # bind the resize callback to the parent window
        self.bind("<Configure>", self.on_window_resize)

    # function that loads an image from a file path and resizes it to the specified dimensions
    def load_and_resize_image(self, width, height):
        image = Image.open(self.image_path)
        image = image.resize((width, height), Image.LANCZOS)
        return ImageTk.PhotoImage(image)

    # callback function triggered when the window is resized and resizes the background image to fit the new window dimensions
    def on_window_resize(self, event):
        # get the updated window size
        new_width = event.width
        new_height = event.height

        # resize the image and update the label
        self.photo = self.load_and_resize_image(new_width, new_height)
        self.background_label.configure(image=self.photo)
    
    # calls the admin password window before proceeding further granting restricted access to unauthorized personnel
    def admin_pass_request(self, controller, next_page):
        admin_pass_window = AdminPasswordWindow(controller, next_page)
        admin_pass_window.grab_set()
