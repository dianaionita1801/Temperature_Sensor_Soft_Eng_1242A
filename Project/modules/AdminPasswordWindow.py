import tkinter as tk
from tkinter import messagebox as ms
import time


# window that prompts the user to enter an administrator password
class AdminPasswordWindow(tk.Toplevel): 
    def __init__(self, controller, next_page):
        tk.Toplevel.__init__(self)
        self.title("Warning!")
        self.configure(bg = '#c8a4d4')
        self.controller = controller
        self.next_page = next_page
        self.incorrect_attempts = 0 
        self.last_incorrect_attempt_time = 0
        self.input_blocked = False
        self.overrideredirect(True)
        
        adm_window_w = 650
        adm_window_h = 350
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        
        center_x = int(screen_w /2 - adm_window_w / 2)
        center_y = int(screen_h /2 - adm_window_h / 2)
        
        self.geometry(f'{adm_window_w}x{adm_window_h}+{center_x}+{center_y}')
        
        # disable the minimize and maximize buttons
        self.attributes('-topmost', True)  # bring the window to the top
        self.attributes('-toolwindow', True)  # remove the minimize and maximize buttons
        
        # if the access is blocked the windows becomes uncloseable and the input becomes blocked
        if self.controller.is_access_blocked:
            self.input_blocked = True
            self.overrideredirect(True)
            

        title_adm_pass = tk.Label(
            self,
            text = "RESTRICTED ACCESS AUTHORIZED PERSONNEL ONLY",
            font = ('Footlight MT Light', 15),
            bg = '#c8a4d4',
            fg = '#12043e'
        )
        title_adm_pass.place(relx = 0.5, rely = 0.1, anchor = "center")

        label_adm_pass = tk.Label(
            self,
            text = "Enter admin password:",
            font = ('Footlight MT Light', 13),
            bg = '#c8a4d4',
            fg = '#12043e'
        )
        label_adm_pass.place(relx = 0.25, rely = 0.3, anchor = "center")

        self.admin_pass_entry = tk.Entry(
            self,
            show = "*",
            font = ('Footlight MT Light', 13),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 40
        )
        self.admin_pass_entry.place(relx = 0.46, rely = 0.45, anchor = "center")
        
        # set the focus to the admin_pass_entry widget
        self.admin_pass_entry.focus_set()
        
        # bind the "Enter" key to the validate_admin_password() method
        self.admin_pass_entry.bind("<Return>", lambda event: self.validate_admin_password())

        # submit button
        submit_adm_pass = tk.Button(
            self,
            text = "Submit",
            command = self.validate_admin_password,
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 22,
            height = 2,
            anchor = 'center'
        )
        submit_adm_pass.place(relx = 0.262, rely = 0.7, anchor = "center")
        
        # cancel button
        Cancel = tk.Button(
            self,
            text = "Cancel",
            command = self.cancel_admin_password,
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 22,
            height = 2,
            anchor = 'center'
        )
        Cancel.place(relx = 0.653, rely = 0.7, anchor = "center")
    
    # function that handles the cancel button 
    def cancel_admin_password(self):
          # if the user is blocked the cancel button won't function anymore and instead it will display the remaining time of restriction
          if self.controller.is_access_blocked:
            remaining_time = int((self.controller.blocked_access_time + 180) - time.time())
            if remaining_time > 0:
                minutes = remaining_time // 60
                seconds = remaining_time % 60
                ms.showerror("Blocked", f"Access is blocked for {minutes} minutes and {seconds} seconds.", parent = self)
            else:
                # if the blocked access time has passed, reset the is_access_blocked flag
                self.controller.is_access_blocked = False
                # re-enable the admin_pass_entry
                self.admin_pass_entry.config(state=tk.NORMAL)
          else:
                
              self.destroy()
        

    # function checks if the entered password matches the true admin password, if after 3 tries the password is not correct it will block the password entry for 3 minutes
    def validate_admin_password(self):
        if self.input_blocked:
            self.cancel_admin_password()
            return
        
        admin_password = "admin123"  # replace with true admin password
        entered_password = self.admin_pass_entry.get()
        
        if entered_password == admin_password:
            # encrypted_password = self.password_entry.get()  # Replace password_entry with the corresponding Entry widget for the password column
            # self.controller.decrypt_password(encrypted_password)
            self.controller.is_access_blocked = False  # reset access block flag to false
            self.controller.show_frame(self.next_page)
            self.destroy()
        else:
            self.incorrect_attempts += 1
            if self.incorrect_attempts >= 3:
                self.block_access_for_3_minutes()
                self.admin_pass_entry.delete(0, tk.END)
            else:
                self.last_incorrect_attempt_time = time.time() 
                ms.showerror("Error", "Invalid admin password!", parent = self)
                self.admin_pass_entry.delete(0, tk.END)
                
    # function that blocks access for a 3 min period after 3 invalid admin pass tries            
    def block_access_for_3_minutes(self):
        self.controller.is_access_blocked = True  # set access block flag to true
        self.controller.blocked_access_time = time.time()  # save the time when access was blocked
        ms.showerror("Blocked", "Too many incorrect attempts. Access blocked for 3 minutes.", parent = self)
        self.input_blocked = True
        self.admin_pass_entry.config(state=tk.DISABLED)
        self.after(180000, self.unblock_access)
    
    # function that unblocks the access after 3 min have passed since the user was blocked
    def unblock_access(self):
        self.controller.is_access_blocked = False  # reset access block flag to false
        self.controller.blocked_access_time = 0  # reset the blocked access time
        self.admin_pass_entry.config(state=tk.NORMAL)
        self.incorrect_attempts = 0            
        self.input_blocked = False  # allow input again 
