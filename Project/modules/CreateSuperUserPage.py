import tkinter as tk
import re
from tkinter import messagebox as ms
import datetime
import hashlib
from modules.SecondPage import SecondPage

# create super user form page
class CreateSuperUserPage(tk.Frame):
    def __init__(self, parent, controller, db_manager):
        tk.Frame.__init__(self, parent)
        self.configure(bg = '#c8a4d4')
        self.db_manager = db_manager

        titleSUser = tk.Label(
            self,
            text = "Add a new super user",
            font = ('Footlight MT Light', 18),
            bg = '#c8a4d4',
            fg ='#12043e'
        )
        titleSUser.place(relx = 0.5, rely = 0.1, anchor = "center")
        
        # first name label and entry
        label_S_Fname = tk.Label(
            self,
            text = "First name*:",
            font = ('Footlight MT Light', 15),
            bg = '#c8a4d4',
            fg ='#12043e'
        )
        label_S_Fname.place(relx = 0.1, rely = 0.2, anchor = "w")

        self.S_Fname_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 15),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 40
        )
        self.S_Fname_entry.place(relx = 0.55, rely = 0.2, anchor = "center")
        
        # last name label and entry
        label_S_Lname = tk.Label(
            self,
            text = "Last name*:",
            font = ('Footlight MT Light', 15),
            bg = '#c8a4d4',
            fg = '#12043e'
        )
        label_S_Lname.place(relx = 0.1, rely = 0.25, anchor = "w")

        self.S_Lname_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 15),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 40
        )
        self.S_Lname_entry.place(relx = 0.55, rely = 0.25, anchor = "center")
        
        # email label and entry
        label_S_email = tk.Label(
            self,
            text = "Email*:",
            font = ('Footlight MT Light', 15),
            bg = '#c8a4d4',
            fg = '#12043e'
        )
        label_S_email.place(relx = 0.1, rely = 0.3, anchor = "w")

        self.S_email_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 15),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 40
        )
        self.S_email_entry.place(relx = 0.55, rely = 0.3, anchor = "center")
        
        # phone label and entry
        label_S_phone = tk.Label(
            self,
            text = "Phone number:",
            font = ('Footlight MT Light', 15),
            bg = '#c8a4d4',
            fg = '#12043e'
        )
        label_S_phone.place(relx = 0.1, rely = 0.35, anchor = "w")

        self.S_phone_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 15),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 40
        )
        self.S_phone_entry.place(relx = 0.55, rely = 0.35, anchor = "center")
        
        # password label and entry
        label_S_pass = tk.Label(
            self,
            text = "Password*:",
            font = ('Footlight MT Light', 15),
            bg = '#c8a4d4',
            fg = '#12043e'
        )
        label_S_pass.place(relx = 0.1, rely = 0.4, anchor = "w")
        
        self.S_pass_entry = tk.Entry(
            self,
            show = '*',
            font = ('Footlight MT Light', 15),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 40
        )
        self.S_pass_entry.place(relx = 0.55, rely = 0.4, anchor = "center")
        
        # repeat password label and entry
        label_S_rep_pass = tk.Label(
            self,
            text = "Repeat password*:",
            font = ('Footlight MT Light', 15),
            bg = '#c8a4d4',
            fg = '#12043e'
        )
        label_S_rep_pass.place(relx = 0.1, rely = 0.45, anchor = "w")
        
        self.S_rep_pass_entry = tk.Entry(
            self,
            show = '*',
            font = ('Footlight MT Light', 15),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 40
        )
        self.S_rep_pass_entry.place(relx = 0.55, rely = 0.45, anchor = "center")
        
        # submit button
        Sub = tk.Button(
            self,
            text = "Submit",
            command = self.insert_dataS,
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 40,
            height = 2,
            anchor = 'center'
        )
        Sub.place(relx = 0.5, rely = 0.55, anchor = "center")
        
        # back button
        BackS = tk.Button(
            self,
            text = "Back",
            command = lambda: controller.show_frame(SecondPage),
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 40,
            height = 2,
            anchor = 'center'
        )
        BackS.place(relx = 0.5, rely = 0.63, anchor = "center")
        

    def insert_dataS(self):
        S_f_name = self.S_Fname_entry.get()
        S_l_name = self.S_Lname_entry.get()
        S_email = self.S_email_entry.get()
        S_phone = self.S_phone_entry.get()
        S_password = self.S_pass_entry.get()
        S_rep_pass = self.S_rep_pass_entry.get()
        add_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        active = None
        user_id = None
        priv_id = None
        
        salt = "57c21b"
        pepper = "2p2o1v"
        
        # data insertion conditions
        
        # check if fields are uncompleted
        if(len(S_f_name) == 0):
           ms.showerror("ERROR", "First name cannot be empty!")
           return
       
        elif(len(S_l_name) == 0):
           ms.showerror("ERROR", "Last name cannot be empty!")
           return
       
        elif(len(S_email) == 0):
           ms.showerror("ERROR", "Email cannot be empty!")
           return
           
        elif(len(S_password) == 0):
           ms.showerror("ERROR", "Password cannot be empty!")
           return
        
        # check if first name contains digits
        if any(ch.isdigit() for ch in S_f_name):
            ms.showerror("Error", "First name can't have numbers!")
            return
        
        # check if last name contains digits
        if any(ch.isdigit() for ch in S_l_name):
            ms.showerror("Error", "Last name can't have numbers!")
            return
        
        # check the length of the first name to be between 2 and 100 characters
        if len(S_f_name) <= 2:
            ms.showerror("Error", "First name is too short!")
            return
        
        if len(S_f_name) > 100:
            ms.showerror("Error", "First name is too long!")
            return
        
        # check the length of the first name to be between 2 and 100 characters
        if len(S_l_name) <= 2:
            ms.showerror("Error", "Last name is too short!")
            return
        
        if len(S_l_name) > 100:
            ms.showerror("Error", "Last name is too long!")
            return
        
        # check if the email has the proper structure
        if not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', S_email):
            ms.showerror("Error", "Invalid email address!")
            return
        
        # check if the length of the phone number is not more than 10 digits
        if len(S_phone) > 10:
            ms.showerror("Error", "Phone number is too long!")
            return
        
        # check if the password introduced is the same with the repeated password
        if S_password != S_rep_pass:
            ms.showerror("Error", "Passwords don't match!")
            return
        
        enc_pass = pepper + S_password + salt

        encrypted_password = hashlib.md5(enc_pass.encode())
        
        param = (user_id, S_f_name, S_l_name, S_email, S_phone, encrypted_password.hexdigest(), add_date, priv_id, active)
        
        try:
            self.db_manager.execute_query("INSERT INTO `User` (`User_ID`, `First_name`, `Last_Name`, `Email`, `Phone_number`, `Password`, `Date_of_reg`, `Priv_ID`, `Active`) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)", param)        
            
            # message to be shown if the registration was a success
            ms.showinfo("SUCCESS","Super User account created succesfully!")

            # reset input fields
            self.S_Fname_entry.delete(0, tk.END)
            self.S_Lname_entry.delete(0, tk.END)
            self.S_email_entry.delete(0, tk.END)
            self.S_phone_entry.delete(0, tk.END)
            self.S_pass_entry.delete(0, tk.END)
            self.S_rep_pass_entry.delete(0, tk.END)
            
        except Exception as e:
            ms.showerror("ERROR", f"An error occurred: {e}")