import tkinter as tk
from PIL import Image, ImageTk
from modules.AdminPasswordWindow import AdminPasswordWindow


# user management page       
class SecondPage(tk.Frame):
    def __init__(self, parent, controller, db_manager):
        from modules.CreateSuperUserPage import CreateSuperUserPage
        from modules.CreateUserPage import CreateUserPage
        from modules.ThirdPage import ThirdPage
        from modules.StartPage import StartPage
        tk.Frame.__init__(self, parent)
        self.configure(bg='#d398fa')
        self.db_manager = db_manager
        
        # load the image using PhotoImage
        self.image_path = "D:\\Documents\\Facultate\\Software Engineering\\Project\\assets\\background.png"
        self.photo = self.load_and_resize_image(1080, 720)
        
        # create a label to display the image as the background
        self.background_label = tk.Label(self, image=self.photo)
        self.background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        # add user button
        AddUser = tk.Button(
            self,
            text ="Add User",
            command = lambda: controller.show_frame(CreateUserPage),
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 40,
            height = 2,
            anchor = 'center'
        )
        AddUser.place(relx = 0.5, rely = 0.1, anchor = "center")

        # add super user button
        AddSUser = tk.Button(
            self,
            text = "Add SuperUser",
            command = lambda: self.admin_pass_request(controller, CreateSuperUserPage),
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 40,
            height = 2,
            anchor = 'center'
        )
        AddSUser.place(relx = 0.5, rely = 0.178, anchor = "center")
        
        # edit user database button
        EditDB = tk.Button(
            self,
            text = "Edit User DB",
            command = lambda: self.admin_pass_request(controller, ThirdPage),
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 40,
            height = 2,
            anchor = 'center'
        )
        EditDB.place(relx = 0.5, rely = 0.256, anchor = "center")

        # back button
        Back1 = tk.Button(
            self,
            text = "Back",
            command = lambda: controller.show_frame(StartPage),
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 40,
            height = 2,
            anchor = 'center'
        )
        Back1.place(relx = 0.5, rely = 0.334, anchor = "center")

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