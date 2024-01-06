import tkinter as tk
import re
from tkinter import messagebox as ms
import datetime
import hashlib
from modules.SecondPage import SecondPage


# create a new user form page 
class CreateUserPage(tk.Frame):
    def __init__(self, parent, controller, db_manager):
        tk.Frame.__init__(self, parent)
        self.configure(bg = '#c8a4d4')
        self.db_manager = db_manager
        
        title = tk.Label(
            self,
            text = "Add a new user",
            font = ('Footlight MT Light', 18),
            bg = '#c8a4d4',
            fg = '#12043e'
        )
        title.place(relx = 0.5, rely = 0.1, anchor = "center")
        
        # first name label and entry
        label_Fname = tk.Label(
            self,
            text = "First name*:",
            font = ('Footlight MT Light', 15),
            bg = '#c8a4d4',
            fg = '#12043e'
        )
        label_Fname.place(relx = 0.1, rely = 0.2, anchor = "w")

        self.Fname_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 15),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 40
        )
        self.Fname_entry.place(relx = 0.55, rely = 0.2, anchor = "center")
        
        # last name label and entry
        label_Lname = tk.Label(
            self,
            text = "Last name*:",
            font = ('Footlight MT Light', 15),
            bg = '#c8a4d4',
            fg = '#12043e'
        )
        label_Lname.place(relx = 0.1, rely = 0.25, anchor = "w")

        self.Lname_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 15),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 40
        )
        self.Lname_entry.place(relx = 0.55, rely = 0.25, anchor = "center")

        # email label and entry
        label_email = tk.Label(
            self,
            text = "Email*:",
            font = ('Footlight MT Light', 15),
            bg = '#c8a4d4',
            fg = '#12043e'
        )
        label_email.place(relx = 0.1, rely = 0.3, anchor = "w")

        self.email_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 15),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 40
        )
        self.email_entry.place(relx = 0.55, rely = 0.3, anchor = "center")
        
        # phone label and entry
        label_phone = tk.Label(
            self,
            text = "Phone number:",
            font = ('Footlight MT Light', 15),
            bg = '#c8a4d4',
            fg = '#12043e'
        )
        label_phone.place(relx = 0.1, rely = 0.35, anchor = "w")

        self.phone_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 15),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 40
        )
        self.phone_entry.place(relx = 0.55, rely = 0.35, anchor = "center")
        
        # password label and entry
        label_pass = tk.Label(
            self,
            text = "Password*:",
            font = ('Footlight MT Light', 15),
            bg = '#c8a4d4',
            fg = '#12043e'
        )
        label_pass.place(relx = 0.1, rely = 0.4, anchor = "w")
        
        self.pass_entry = tk.Entry(
            self,
            show = '*',
            font = ('Footlight MT Light', 15),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 40
        )
        self.pass_entry.place(relx = 0.55, rely = 0.4, anchor = "center")
        
        # repeat password label and entry
        label_rep_pass = tk.Label(
            self,
            text = "Repeat password*:",
            font = ('Footlight MT Light', 15),
            bg = '#c8a4d4',
            fg = '#12043e'
        )
        label_rep_pass.place(relx = 0.1, rely = 0.45, anchor = "w")
        
        self.rep_pass_entry = tk.Entry(
            self,
            show = '*',
            font = ('Footlight MT Light', 15),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 40
        )
        self.rep_pass_entry.place(relx = 0.55, rely = 0.45, anchor = "center")
        
        self.Fname_entry.focus_set()
        
        # bind the "Enter" key event to the submit_data() method on the frame
        self.bind('<Return>', self.insert_data)

        # submit button
        Submit = tk.Button(
            self,
            text = "Submit",
            command = self.insert_data,
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 25,
            height = 2,
            anchor = 'center'
        )
        Submit.place(relx = 0.415, rely = 0.6, anchor = "center")
        
        # back button
        Back3 = tk.Button(
            self,
            text = "Back",
            command = lambda: controller.show_frame(SecondPage),
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 25,
            height = 2,
            anchor = 'center'
        )
        Back3.place(relx = 0.68, rely = 0.6, anchor = "center")

    def insert_data(self):
        f_name = self.Fname_entry.get()
        l_name = self.Lname_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        password = self.pass_entry.get()
        rep_pass = self.rep_pass_entry.get()
        add_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        active = None
        user_id = None
        priv_id = None
        
        salt = "57c21b"
        pepper = "2p2o1v"
        
        # data insertion conditions
        
        # check if fields are uncompleted
        if(len(f_name) == 0):
           ms.showerror("ERROR", "First name cannot be empty!")
           return
       
        elif(len(l_name) == 0):
           ms.showerror("ERROR", "Last name cannot be empty!")
           return
       
        elif(len(email) == 0):
           ms.showerror("ERROR", "Email cannot be empty!")
           return
           
        elif(len(password) == 0):
           ms.showerror("ERROR", "Password cannot be empty!")
           return
        
        # check if first name contains digits
        if any(ch.isdigit() for ch in f_name):
            ms.showerror("Error", "First name can't have numbers!")
            return
        
        # check if last name contains digits
        if any(ch.isdigit() for ch in l_name):
            ms.showerror("Error", "Last name can't have numbers!")
            return
        
        # check the length of the first name to be between 2 and 100 characters
        if len(f_name) <= 2:
            ms.showerror("Error", "First name is too short!")
            return
        
        if len(f_name) > 100:
            ms.showerror("Error", "First name is too long!")
            return
        
        # check the length of the first name to be between 2 and 100 characters
        if len(l_name) <= 2:
            ms.showerror("Error", "Last name is too short!")
            return
        
        if len(l_name) > 100:
            ms.showerror("Error", "Last name is too long!")
            return
        
        # check if the email has the proper structure
        if not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email):
            ms.showerror("Error", "Invalid email address!")
            return
        
        # check if the length of the phone number is not more than 10 digits
        if len(phone) > 10:
            ms.showerror("Error", "Phone number is too long!")
            return
        
        # check if the password introduced is the same with the repeated password
        if password != rep_pass:
            ms.showerror("Error", "Passwords don't match!")
            return
        
        enc_pass = pepper + password + salt

        encrypted_password = hashlib.md5(enc_pass.encode())
            
        
        paramt = (user_id, f_name, l_name, email, phone, encrypted_password.hexdigest(), add_date, priv_id, active) 
        
        try:
            self.db_manager.execute_query("INSERT INTO `User` (`User_ID`, `First_name`, `Last_Name`, `Email`, `Phone_number`, `Password`, `Date_of_reg`, `Priv_ID`, `Active`) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)", paramt)
            
            
            # message to be shown if the registration was a success
            ms.showinfo("SUCCESS","Account created succesfully!")
    
            # reset input fields
            self.Fname_entry.delete(0, tk.END)
            self.Lname_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.pass_entry.delete(0, tk.END)
            self.rep_pass_entry.delete(0, tk.END)
            
            self.rep_pass_entry.unbind('<Return>')
            
        except Exception as e:
            ms.showerror("ERROR", f"An error occurred: {e}")