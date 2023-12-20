import tkinter as tk
from tkinter import messagebox as ms
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import Scrollbar
import datetime
import hashlib
from modules.ToggleButton import ToggleButton

# edit user db page
class ThirdPage(tk.Frame):
    def __init__(self, parent, controller, db_manager):
        
        tk.Frame.__init__(self, parent)
        from modules.Privileges import Privileges
        from modules.SecondPage import SecondPage
        from modules.StartPage import StartPage
        self.configure(bg='#d398fa')
        self.db_manager = db_manager
        self.delete_all_users_flag = False  # flag to indicate if "Delete all users" button was clicked

        # load the image using PhotoImage
        self.image_path = "D:\\Documents\\Facultate\\Software Engineering\\Project\\assets\\background.png"
        self.photo = self.load_and_resize_image(1080, 720)
        
        # create a label to display the image as the background
        self.background_label = tk.Label(self, image=self.photo)
        self.background_label.place(relx=0, rely=0, relwidth=1, relheight=1)
        
       # create a Frame to hold the Treeview and scrollbars
        tree_frame = tk.Frame(self)
        tree_frame.place(relx=0.5, rely=0.3, anchor="center", relwidth=0.9, relheight=0.5)
        

        # configure the Treeview Colors
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview.Heading", background = "#bc90d8", foreground = "#1f1135")
        self.style.map("Treeview", background=[("selected", "#8056c7")], foreground=[("selected", "white")])

        # create the Treeview widget to display the data in a table
        self.tree = ttk.Treeview(tree_frame, columns=("User_ID", "First_Name", "Last_Name", "Email", "Phone_number", "Password", "Date_of_reg", "Priv_ID", "Active"), show="headings")
        
        # define the headings of the treeview
        self.tree.heading("User_ID", text="User ID")
        self.tree.heading("First_Name", text="First Name")
        self.tree.heading("Last_Name", text="Last Name")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Phone_number", text="Phone number")
        self.tree.heading("Password", text="Password")
        self.tree.heading("Date_of_reg", text="Date of Registration")
        self.tree.heading("Priv_ID", text="Privilege ID")
        self.tree.heading("Active", text="Active")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # configure tag colors for even and odd rows
        self.tree.tag_configure("tree_color", background = '#bca6e1')
        
        # # add some sample data to the Treeview (replace this with data from your database)
        # self.tree.insert("", "end", values=(1, "John", "Doe", "john@example.com", "0722542347", "password1", "2023-07-18", 1, "Yes"), tags = ("tree_color",))
        # self.tree.insert("", "end", values=(2, "Alice", "Smith", "alice@example.com", "0755187342", "password2", "2023-07-18", 2, "No"), tags = ("tree_color",))
        
        tableU = "User"
        
        # fetch data from the database
        users_data = db_manager.fetch_table(tableU)

        # populate the Treeview with the fetched data
        for user_data in users_data:
            self.tree.insert("", tk.END, values=user_data, tags=("tree_color",))
            
        # create vertical scrollbar and link it to the treeview
        v_scroll = Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=v_scroll.set)
        v_scroll.pack(side="right", fill="y")

        # pack the Treeview within tree_frame 
        self.tree.pack(expand=True, fill="both")
        
        # define the headings and associate them with the Treeview columns
        headings = ("User ID", "First Name", "Last Name", "Email", "Phone number", "Password", "Date of Registration", "Privilege ID", "Active")
        for i, heading in enumerate(headings):
            self.tree.heading(i, text=heading)
        
        # create entries and labels to facilitate the management of the treeview data
        
        # user id label and entry
        label_user_id = tk.Label(
            self,
            text = "User ID:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_user_id.place(relx = 0.05, rely = 0.6, anchor = "w")
        
        self.user_id_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.user_id_entry.place(relx = 0.18, rely = 0.6, anchor = "center")
        
        # first name label and entry 
        label_first_name = tk.Label(
            self,
            text = "First Name*:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_first_name.place(relx = 0.25, rely = 0.6, anchor = "w")
        
        self.first_name_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.first_name_entry.place(relx = 0.405, rely = 0.6, anchor = "center")
        
        # last name label and entry
        label_last_name = tk.Label(
            self,
            text = "Last Name*:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_last_name.place(relx = 0.47, rely = 0.6, anchor = "w")
        
        self.last_name_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.last_name_entry.place(relx = 0.6189, rely = 0.6, anchor = "center")
        
        # email label and entry
        label_email = tk.Label(
            self,
            text = "Email*:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_email.place(relx = 0.69, rely = 0.6, anchor = "w")
        
        self.email_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 15                        
            )
        self.email_entry.place(relx = 0.825, rely = 0.6, anchor = "center")   
        
        #phone number label and entry
        label_phone = tk.Label(
            self,
            text = "Phone number*:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_phone.place(relx = 0.05, rely = 0.65, anchor = "w")
        
        self.phone_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.phone_entry.place(relx = 0.229, rely = 0.65, anchor = "center")
        
        # password label and entry
        label_password = tk.Label(
            self,
            text = "Password*:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_password.place(relx = 0.295, rely = 0.65, anchor = "w")  
        
        self.password_entry = tk.Entry(
            self,
            show = '*',
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.password_entry.place(relx = 0.437, rely = 0.65, anchor = "center")
        
        # date of registration label and entry
        label_date_of_reg = tk.Label(
            self,
            text = "Date of Reg:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_date_of_reg.place(relx = 0.504, rely = 0.65, anchor = "w")  
        
        self.date_of_reg_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.date_of_reg_entry.place(relx = 0.657, rely = 0.65, anchor = "center")
        
        # privilege id label and entry
        label_priv_id = tk.Label(
            self,
            text = "UP_Batch*:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_priv_id.place(relx = 0.73, rely = 0.65, anchor = "w") 
        
        self.priv_id_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.priv_id_entry.place(relx = 0.877, rely = 0.65, anchor = "center")
       
        # active label and entry
        label_active = tk.Label(
            self,
            text = "Active:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_active.place(relx = 0.05, rely = 0.7, anchor = "w")
        
        self.active_entry = ToggleButton(
            self,
            command = self.toggle_active, 
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 6)
        self.active_entry.place(relx = 0.168, rely = 0.7, anchor = "center")


        # bind the Treeview selection event to update the entries with the selected row's data
        self.tree.bind("<<TreeviewSelect>>", self.populate_entries)

        # button to add another user to the database
        self.AddUser = tk.Button(
            self,
            text = "Add user",
            command = self.add_user,
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        self.AddUser.place(relx = 0.1, rely = 0.85, anchor = "center")
        
        # button that submits the upgraded data of an existing user in the treeview
        self.EditUser = tk.Button(
            self,
            text = "Edit user",
            command = self.edit_selected_user,
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        self.EditUser.place(relx = 0.26, rely = 0.85, anchor = "center")
        
        # delete selected rows in the treeview
        self.DeleteSel = tk.Button(
            self,
            text = "Delete selected",
            command = self.delete_selected_rows,
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        self.DeleteSel.place(relx = 0.42, rely = 0.85, anchor = "center")
        
        # delete all rows in the treeview
        self.DeleteUsers = tk.Button(
            self,
            text = "Delete all users",
            command = self.delete_all_users,
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        self.DeleteUsers.place(relx = 0.58, rely = 0.85, anchor = "center")
        
        # clear entries button
        self.ClearEntry = tk.Button(
            self,
            text = "Clear entries",
            command = self.clear_entries,
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        self.ClearEntry.place(relx = 0.74, rely = 0.85, anchor = "center")
        
        # permissions button
        self.Perm = tk.Button(
            self,
            text = "Permissions",
            command = lambda: controller.show_frame(Privileges),
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        self.Perm.place(relx = 0.9, rely = 0.85, anchor = "center")
        
        # main menu button
        self.MainM = tk.Button(
            self,
            text = "Main menu",
            command = lambda: controller.show_frame(StartPage),
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        self.MainM.place(relx = 0.74, rely = 0.95, anchor = "center")
        
        # back button
        self.BackThir = tk.Button(
            self,
            text = "Back",
            command = lambda: controller.show_frame(SecondPage),
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        self.BackThir.place(relx = 0.9, rely = 0.95, anchor = "center")
        
        # configure the tree_frame to adjust with window resizing
        tree_frame.columnconfigure(0, weight=1)
        tree_frame.rowconfigure(0, weight=1)
        
        # bind the resize callback to the parent window
        self.bind("<Configure>", self.on_window_resize)
    

    # function to toggle the state of the active button
    def toggle_active(self):
        current_state = self.active_entry.cget("text")
        if current_state == "Yes":
            self.active_entry.config(text="No", relief=tk.RAISED)
        else:
            self.active_entry.config(text="Yes", relief=tk.SUNKEN) 

    # function that retrieves data from the entry fields and inserts it into the treeview + database     
    def add_user(self):
        # retrieve data from the entry fields
        user_id = None
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        password = self.password_entry.get()
        # date_of_reg = self.date_of_reg_entry.get()
        priv_id = self.priv_id_entry.get()
        
        salt = "57c21b"
        pepper = "2p2o1v" 
        
        # Check if any of the required fields are empty
        if not user_id or not first_name or not last_name or not email or not phone or not password or not priv_id:
            ms.showerror("Error", "Please fill in all the required fields*.")
            return
    
        # get the text value of the ToggleButton ("Yes" or "No")
        active_state = self.active_entry.cget("text")
        
        if active_state == "Yes":
            active = 1
        else:
            active = 0
        
        enc_pass = pepper + password + salt
        encrypted_password = hashlib.md5(enc_pass.encode())
            
            
        # get the current date and time
        date_of_reg = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # pass the values of the parameters to the params list
        params = (user_id, first_name, last_name, email, phone, encrypted_password.hexdigest(), date_of_reg, priv_id, active)
        
        self.db_manager.execute_query("INSERT INTO `User` (`User_ID`, `First_name`, `Last_Name`, `Email`, `Phone_number`, `Password`, `Date_of_reg`, `Priv_ID`, `Active`) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)", params)
    
        # insert the data into the table
        self.tree.insert("", tk.END, values=(user_id, first_name, last_name, email, phone, encrypted_password.hexdigest(), date_of_reg, priv_id, active), tags = ("tree_color",))
    
        # clear the entry fields
        self.clear_entries()
    
    
    # function that clears the entry fields - accessed throught the clear entries button
    def clear_entries(self):
        # deselect any selected rows in the treeview
        selected_items = self.tree.selection()
        for item in selected_items:
            self.tree.selection_remove(item)
            
        # clear th entries
        self.user_id_entry.delete(0, tk.END)
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.date_of_reg_entry.delete(0, tk.END)
        self.priv_id_entry.delete(0, tk.END)
        self.active_entry.config(text="No", bg="#dbb6ee", relief=tk.RAISED)
    
    # function that loads an image from a file path and resizes it to the specified dimensions    
    def load_and_resize_image(self, width, height):
        image = Image.open(self.image_path)
        image = image.resize((width, height), Image.LANCZOS)
        return ImageTk.PhotoImage(image)
    
    # function that populates the entry fields with data from selected row in the treeview
    def populate_entries(self, event):
        selected_items = self.tree.selection()

        if not selected_items:
            # no row is selected, so clear the entry fields
            self.clear_entries()
            return

        # get the selected item from the Treeview
        selected_item = selected_items[0]

        # get the data of the selected row
        data = self.tree.item(selected_item, "values")

        # update the entries with the data
        self.user_id_entry.delete(0, tk.END)
        self.user_id_entry.insert(0, data[0])

        self.first_name_entry.delete(0, tk.END)
        self.first_name_entry.insert(0, data[1])

        self.last_name_entry.delete(0, tk.END)
        self.last_name_entry.insert(0, data[2])

        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(0, data[3])

        self.phone_entry.delete(0, tk.END)
        self.phone_entry.insert(0, data[4])        

        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, data[5])

        self.date_of_reg_entry.delete(0, tk.END)
        self.date_of_reg_entry.insert(0, data[6])

        self.priv_id_entry.delete(0, tk.END)
        self.priv_id_entry.insert(0, data[7])

        # update the active button state based on the data
        if data[8] == "1":
            self.active_entry.config(text="Yes", relief=tk.SUNKEN)
            self.active_entry.update()
        else:
            self.active_entry.config(text="No", relief=tk.RAISED)
            self.active_entry.update()
        
        self.active_entry.update_idletasks()
            
    def edit_selected_user(self):
        selected_item = self.tree.selection()
        if not selected_item:
            ms.showerror("Error", "Please select a row to edit.")
            return
        self.edit_user_popup(selected_item[0])
    
    # update the active button state in edit user popup based on the data
    def toggle_active_popup(self):
        current_state = self.active_entry_popup.cget("text")
        if current_state == "Yes":
            self.active_entry_popup.config(text="No", relief=tk.RAISED)
        else:
            self.active_entry_popup.config(text="Yes", relief=tk.SUNKEN)
    
    def disable_buttons(self):
        btns_to_disable = [self.AddUser, self.EditUser, self.DeleteSel, self.DeleteUsers, self.ClearEntry, self.Perm, self.MainM, self.BackThir]
        for button in btns_to_disable:
            button.config(state=tk.DISABLED)
            
    def enable_buttons(self):
        btns_to_enable = [self.AddUser, self.EditUser, self.DeleteSel, self.DeleteUsers, self.ClearEntry, self.Perm, self.MainM, self.BackThir]
        for button in btns_to_enable:
            button.config(state=tk.NORMAL)
            
    # function that updates preexistent instances after they where modified from the entries    
    def edit_user_popup(self, selected_item):
        
        # disable the buttons on the edit user db page before creating the pop-up
        self.disable_buttons()
        
        # create a pop-up window for editing the selected user
        edit_popup = tk.Toplevel(self)
        edit_popup.title("Edit User")
        # edit_popup.geometry("650x350")
        
        user_window_w = 650
        user_window_h = 350
        usr_screen_w = edit_popup.winfo_screenwidth()
        usr_screen_h = edit_popup.winfo_screenheight()
        
        user_center_x = int(usr_screen_w / 2 - user_window_w / 2)
        user_center_y = int(usr_screen_h / 2 - user_window_h / 2)
        
        edit_popup.geometry(f'{user_window_w}x{user_window_h}+{user_center_x}+{user_center_y}')
        
        edit_popup.configure(bg = '#c8a4d4')
        edit_popup.attributes('-topmost', True)  # bring the window to the top
        edit_popup.attributes('-toolwindow', True)
        edit_popup.focus_set()
        
        # get the data of the selected row
        data = self.tree.item(selected_item, "values")
        
        # create and place entry fields with data from the selected row
        # label and entry user id
        label_user_idP = tk.Label(
            edit_popup,
            text = "User ID:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_user_idP.place(relx = 0.05, rely = 0.05, anchor = "w")
        
        self.user_id_entry_popup = tk.Entry(
            edit_popup,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 15
            )
        self.user_id_entry_popup.insert(0, data[0])
        self.user_id_entry_popup.place(relx = 0.2, rely = 0.05, anchor = "w")
        
        # label and entry first name
        label_first_nameP = tk.Label(
            edit_popup,
            text = "First Name:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_first_nameP.place(relx = 0.05, rely = 0.15, anchor = "w")
        
        self.first_name_entry_popup = tk.Entry(
            edit_popup,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 15
            )
        self.first_name_entry_popup.insert(0, data[1])
        self.first_name_entry_popup.place(relx = 0.2, rely = 0.15, anchor = "w")
        
        # label and entry last name
        label_last_nameP = tk.Label(
            edit_popup,
            text = "Last Name:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_last_nameP.place(relx = 0.05, rely = 0.25, anchor = "w")
        
        self.last_name_entry_popup = tk.Entry(
            edit_popup,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 15
            )
        self.last_name_entry_popup.insert(0, data[2])
        self.last_name_entry_popup.place(relx = 0.2, rely = 0.25, anchor = "w")
        
        # label and entry email
        label_emailP = tk.Label(
            edit_popup,
            text = "Email:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_emailP.place(relx = 0.05, rely = 0.35, anchor = "w")
        
        self.email_entry_popup = tk.Entry(
            edit_popup,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 15
            )
        self.email_entry_popup.insert(0, data[3])
        self.email_entry_popup.place(relx = 0.2, rely = 0.35, anchor = "w")
        
        # label and entry phone 
        label_phoneP = tk.Label(
            edit_popup,
            text = "Phone:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_phoneP.place(relx = 0.05, rely = 0.45, anchor = "w")   
        
        self.phone_entry_popup = tk.Entry(
            edit_popup,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 15
            )
        self.phone_entry_popup.insert(0, data[4])
        self.phone_entry_popup.place(relx = 0.2, rely = 0.45, anchor = "w")
        
        # label and entry password
        label_passwordP = tk.Label(
            edit_popup,
            text = "Password:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_passwordP.place(relx = 0.05, rely = 0.55, anchor = "w")
        
        self.password_entry_popup = tk.Entry(
            edit_popup,
            show = '*',
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 15
            )
        self.password_entry_popup.insert(0, data[5])
        self.password_entry_popup.place(relx = 0.2, rely = 0.55, anchor = "w")
        
        # label and entry priv id
        label_priv_idP = tk.Label(
            edit_popup,
            text = "UP_Batch:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_priv_idP.place(relx = 0.05, rely = 0.65, anchor = "w")
        
        self.priv_id_entry_popup = tk.Entry(
            edit_popup,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 15
            )
        self.priv_id_entry_popup.insert(0, data[7])
        self.priv_id_entry_popup.place(relx = 0.2, rely = 0.65, anchor = "w")
        
        # label and button active
        label_activeP = tk.Label(
            edit_popup,
            text = "Active:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_activeP.place(relx = 0.05, rely = 0.75, anchor = "w")
        
        self.active_entry_popup = ToggleButton(
            edit_popup,
            command=self.toggle_active_popup,  
            font=('Footlight MT Light', 11),
            fg='#12043e',
            bg='#dbb6ee',
            width=6
        )
        self.active_entry_popup.place(relx = 0.2, rely = 0.75, anchor = "w")

        # update the active button based on the value in the selected row
        if data[8] == "1":
            self.active_entry_popup.config(text="Yes", relief=tk.SUNKEN)
        else:
            self.active_entry_popup.config(text="No", relief=tk.RAISED)
        
        # save button   
        save_button = tk.Button(
            edit_popup, 
            text = "Save", 
            command = lambda: self.save_edited_user(edit_popup, selected_item),
            font=('Footlight MT Light', 11),
            fg='#12043e',
            bg='#dbb6ee',
            width = 10
            )
        save_button.place(relx = 0.7, rely = 0.3, anchor = "center")
        
        # cancel button
        cancel_button = tk.Button(
            edit_popup,
            text = "Cancel",
            command = lambda: self.cancel_edit_popup(edit_popup),
            font=('Footlight MT Light', 11),
            fg='#12043e',
            bg='#dbb6ee',
            width = 10
            )
        cancel_button.place(relx = 0.7, rely = 0.4, anchor = "center")
        
        edit_popup.bind("<Destroy>", lambda event: self.cancel_edit_popup(edit_popup))
    
    def cancel_edit_popup(self, edit_popup):
        edit_popup.destroy()
        self.enable_buttons()
    
    # function for save button
    def save_edited_user(self, edit_popup, selected_item):
        
        active_user = 1 if self.active_entry_popup.cget("text") == "Yes" else 0
        # retrieve the edited data from the entry fields
        edited_data = (
            self.user_id_entry_popup.get(),
            self.first_name_entry_popup.get(),
            self.last_name_entry_popup.get(),
            self.email_entry_popup.get(),
            self.phone_entry_popup.get(),
            self.password_entry_popup.get(),
            self.tree.item(selected_item, "values")[6],
            self.priv_id_entry_popup.get(),
            active_user
        )
        
        salt = "57c21b"
        pepper = "2p2o1v" 
        
        # retrieve the current data of the selected row
        current_data = self.tree.item(selected_item, "values")
    
        # compare edited data with current data to check for changes
        changed_u = False
        for edited_u_val, current_u_val in zip(edited_data, current_data):
            edited_u_val_str = str(edited_u_val)
            current_u_val_str = str(current_u_val)
            
            if edited_u_val_str != current_u_val_str:
               changed_u = True
               break
        print("Changes Detected:", changed_u)
        
        if not changed_u:
            ms.showinfo("No Changes", "No changes were made.", parent = edit_popup)
            edit_popup.destroy()
            self.enable_buttons()
            return
            
    
        # ask for confirmation to save changes
        confirmation = ms.askyesnocancel("Save Changes", "Save changes to this user?", parent = edit_popup)
        if confirmation:
            # update the database with the edited data
            active = 1 if edited_data[-1] == "Yes" else 0
            
            # encrypt the password if it was modified
            edited_password = edited_data[5]
            current_password = current_data[5]
            if edited_password != current_password:
                enc_pass = pepper + edited_data[5] + salt
                encrypted_password = hashlib.md5(enc_pass.encode())
            else:
                enc_pass = pepper + current_data[5] + salt
                encrypted_password = hashlib.md5(enc_pass.encode())
            
            params = (
                edited_data[1],  # First Name
                edited_data[2],  # Last Name
                edited_data[3],  # Email
                edited_data[4],  # Phone
                encrypted_password.hexdigest(),  # Password
                edited_data[7],  # Privilege ID
                active,
                edited_data[0]  # User ID
                
            )
            
            # query to be sent to database
            self.db_manager.execute_query("UPDATE `User` SET `First_name` = %s, `Last_Name` = %s, `Email` = %s, `Phone_number` = %s, `Password` = %s, `Priv_ID` = %s, `Active` = %s WHERE `User`.`User_ID` = %s", params)
        
            # data to be inserted in the treeview
            edited_data_for_treeview = (
                edited_data[0],
                edited_data[1],
                edited_data[2],
                edited_data[3],
                edited_data[4],
                encrypted_password.hexdigest(),
                edited_data[6],
                edited_data[7],
                active  
            )
            
            # insertion into treeview
            self.tree.item(selected_item, values=edited_data_for_treeview)
        
            edit_popup.destroy()
            self.enable_buttons()
            
        elif confirmation is None:
            # user clicked "Cancel" in the pop-up, close the edit pop-up
            pass
        else:
            # user clicked "No" in the pop-up, close the edit pop-up
            edit_popup.destroy()
            self.enable_buttons()
        
    def delete_selected_rows(self, selected_items=None):
        # if selected_items is None, get a list of selected items in the treeview
        if selected_items is None:
            selected_items = self.tree.selection()

        if not selected_items:
            ms.showerror("Error", "Please select one or more rows to delete.")
            return

        # if delete_all_users_flag is True, skip the confirmation pop-up
        if not self.delete_all_users_flag:
            # confirm the deletion with the user
            if not ms.askyesno("Confirm Deletion", "Are you sure you want to delete the selected row(s)?"):
                return

        # remove the selected rows from the Treeview
        for item in selected_items:
            user_id = self.tree.item(item, "values")[0]
            self.db_manager.execute_query("DELETE FROM `User` WHERE `User`.`User_ID` = %s", (user_id,))
            self.tree.delete(item)

    def delete_all_users(self):
        # set the flag to indicate "Delete all users" button was clicked
        self.delete_all_users_flag = True

        # confirm the deletion with the user
        if not ms.askyesno("Confirm Deletion", "Are you sure you want to delete all users?"):
            # reset the flag if the user cancels the action
            self.delete_all_users_flag = False
            return
        
        # execute query to delete all rows from the database
        self.db_manager.execute_query("DELETE FROM `User`", [])

        # get all items in the Treeview and pass them to the delete_selected_rows function
        all_items = self.tree.get_children()
        self.delete_selected_rows(all_items)

        # reset the flag after the deletion
        self.delete_all_users_flag = False
        
    # callback function triggered when the window is resized and resizes the background image to fit the new window dimensions
    def on_window_resize(self, event):
        
        # resize the tree columns to fit the window
        for col in range(len(self.tree["columns"])):
            self.tree.column(col, width=int(self.tree.winfo_width() / len(self.tree["columns"])))
            
        # get the updated window size
        new_width = event.width
        new_height = event.height

        # resize the image and update the label
        self.photo = self.load_and_resize_image(new_width, new_height)
        self.background_label.configure(image=self.photo)
