import tkinter as tk
import re
from tkinter import messagebox as ms
from PIL import Image, ImageTk
import hashlib

# login page
class LoginPage(tk.Frame):
    def __init__(self, parent, controller, db_manager):
        from modules.StartPage import StartPage
        tk.Frame.__init__(self, parent)
        self.configure(bg = '#c8a4d4')
        self.db_manager = db_manager
        self.image_path = "D:\\Documents\\Facultate\\Software Engineering\\Project\\assets\\background.png"
        self.photo = self.load_and_resize_image(1080, 720)
        
        # create a label to display the image as the background
        self.background_label = tk.Label(self, image=self.photo)
        self.background_label.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        titleL = tk.Label(
            self,
            text = "Login",
            font = ('Footlight MT Light', 18),
            bg = '#c8a4d4',
            fg = '#12043e'
        )
        titleL.place(relx = 0.5, rely = 0.1, anchor = "center")        

        # email label and entry
        label_emailL = tk.Label(
            self,
            text = "Email*:",
            font = ('Footlight MT Light', 15),
            bg = '#c8a4d4',
            fg = '#12043e'
        )
        label_emailL.place(relx = 0.1, rely = 0.3, anchor = "w")

        self.emailL_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 15),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 40
        )
        self.emailL_entry.place(relx = 0.55, rely = 0.3, anchor = "center")
        
        # password label and entry
        label_passL = tk.Label(
            self,
            text = "Password*:",
            font = ('Footlight MT Light', 15),
            bg = '#c8a4d4',
            fg = '#12043e'
        )
        label_passL.place(relx = 0.1, rely = 0.4, anchor = "w")
        
        self.passL_entry = tk.Entry(
            self,
            show = '*',
            font = ('Footlight MT Light', 15),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 40
        )
        self.passL_entry.place(relx = 0.55, rely = 0.4, anchor = "center")

        # submit button
        SubmitL = tk.Button(
            self,
            text = "Submit",
            command = self.validate_data,
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 25,
            height = 2,
            anchor = 'center'
        )
        SubmitL.place(relx = 0.415, rely = 0.6, anchor = "center")
        
        # back button
        BackL = tk.Button(
            self,
            text = "Back",
            command = lambda: controller.show_frame(StartPage),
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 25,
            height = 2,
            anchor = 'center'
        )
        BackL.place(relx = 0.68, rely = 0.6, anchor = "center")
        
        # bind the resize callback to the parent window
        self.bind("<Configure>", self.on_window_resize)

    def validate_data(self):
        salt = "57c21b"
        pepper = "2p2o1v" 
        email = self.emailL_entry.get()
        password = self.passL_entry.get()
        
        # data insertion conditions
        
        # check if fields are uncompleted
        if(len(email) == 0):
           ms.showerror("ERROR", "Email cannot be empty!", parent = self)
           return
           
        elif(len(password) == 0):
           ms.showerror("ERROR", "Password cannot be empty!", parent = self)
           return
        
        # check if the email has the proper structure
        if not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email):
            ms.showerror("Error", "Invalid email address!", parent = self)
            return
        
        tableL = "User"
        
        # fetch data from the database
        users_data = self.db_manager.fetch_table(tableL)
        
        enc_passwd = pepper + password + salt
        encry_pass = hashlib.md5(enc_passwd.encode())
        
        matched_user = None
        for user in users_data:
            if user[3] == email:
                matched_user = user
                break
        
        if matched_user is None:
            ms.showerror("Error", "Invalid email or password!", parent = self)
            self.passL_entry.delete(0, tk.END)
            return
    
        if matched_user[5] == encry_pass.hexdigest():
            # Successful login
            ms.showinfo("Success", "Login successful!", parent = self)
            self.emailL_entry.delete(0, tk.END)
            self.passL_entry.delete(0, tk.END)
        else:
            ms.showerror("Error", "Invalid email or password!", parent = self)
            self.passL_entry.delete(0, tk.END)

        # reset input fields
        self.emailL_entry.delete(0, tk.END)
        self.pass_entry.delete(0, tk.END)
    
    def setup_submit_on_enter(self):
        # bind the "Enter" key event to the submit_data() method on the frame
        self.bind("<Return>", self.validate_data)

    def remove_submit_on_enter(self):
        # unbind the "Enter" key event from the submit_data() method on the frame
        self.unbind("<Return>")
     
        

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
