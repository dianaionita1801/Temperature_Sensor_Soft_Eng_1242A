import tkinter as tk
from tkinter import messagebox as ms
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import Scrollbar
import datetime
from modules.ToggleButton import ToggleButton
from modules.AdminPasswordWindow import AdminPasswordWindow

class Privileges(tk.Frame):
    def __init__(self, parent, controller, db_manager):
        from modules.StartPage import StartPage
        from modules.UserHasPriviliges import UHP
        from modules.ThirdPage import ThirdPage
        tk.Frame.__init__(self, parent)
        self.configure(bg='#d398fa')
        self.db_manager = db_manager
        self.delete_all_priv_flag = False # flag to indicate if "Delete all privileges" button was clicked
        
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
        self.tree = ttk.Treeview(tree_frame, columns=("Privilege_ID", "Type", "Value", "Codename", "Add_Date", "User_Add_ID", "Edit_Date", "User_Edit_ID", "Active"), show="headings")
        
        # define the headings of the treeview
        self.tree.heading("Privilege_ID", text = "Privilege ID")
        self.tree.heading("Type", text = "Type")
        self.tree.heading("Value", text = "Value")
        self.tree.heading("Codename", text = "Codename")
        self.tree.heading("Add_Date", text = "Add date")
        self.tree.heading("User_Add_ID", text = "User Add ID ")
        self.tree.heading("Edit_Date", text = "Edit date")
        self.tree.heading("User_Edit_ID", text = "User Edit ID ")
        self.tree.heading("Active", text = "Active")
    
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # configure tag colors for even and odd rows
        self.tree.tag_configure("tree_color", background = '#bca6e1')
    
        # # add some sample data to the Treeview (replace this with data from your database)
        # self.tree.insert("", "end", values=(1, "Read User DB", 1, "can_read_user_db"),tags=("tree_color",))
        # self.tree.insert("", "end", values=(2, "Write User DB", 1, "can_write_user_db"), tags=("tree_color",))
        
        tableP = "Privileges"
        
        # fetch data from the database
        privs_data = db_manager.fetch_table(tableP)

        # populate the Treeview with the fetched data
        for priv_data in privs_data:
            self.tree.insert("", tk.END, values=priv_data, tags=("tree_color",))
    
        # create vertical scrollbar and link it to the treeview
        v_scroll = Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=v_scroll.set)
        v_scroll.pack(side="right", fill="y")
    
    
        # pack the Treeview within tree_frame 
        self.tree.pack(expand=True, fill="both")
        
    
        # create entries and labels to facilitate the management of the treeview data
        
        # privilege id label and entry
        label_priv_id = tk.Label(
            self,
            text = "Privilege ID*:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_priv_id.place(relx = 0.05, rely = 0.6, anchor = "w")
        
        self.priv_id_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.priv_id_entry.place(relx = 0.215, rely = 0.6, anchor = "center")
        
        # type label and entry 
        label_type = tk.Label(
            self,
            text = "Type*:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_type.place(relx = 0.279, rely = 0.6, anchor = "w")
        
        self.type_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.type_entry.place(relx = 0.394, rely = 0.6, anchor = "center")
        
        # value label and entry
        label_value = tk.Label(
            self,
            text = "Value*:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_value.place(relx = 0.46, rely = 0.6, anchor = "w")
        
        self.value_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.value_entry.place(relx = 0.583, rely = 0.6, anchor = "center")
        
        # codename label and entry
        label_codename = tk.Label(
            self,
            text = "Codename*:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_codename.place(relx = 0.65, rely = 0.6, anchor = "w")
        
        self.codename_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.codename_entry.place(relx = 0.805, rely = 0.6, anchor = "center")
        
        # add date label and entry
        label_add_date = tk.Label(
            self, 
            text = "Add date:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_add_date.place(relx = 0.05, rely = 0.65, anchor = "w")
        
        self.add_date_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.add_date_entry.place(relx = 0.183, rely = 0.65, anchor = "center")
        
        # user add id label and entry
        label_user_add_p = tk.Label(
            self, 
            text = "User Add ID*:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_user_add_p.place(relx = 0.3, rely = 0.65, anchor = "center")
        
        self.user_add_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.user_add_entry.place(relx = 0.412, rely = 0.65, anchor = "center")
        
        # edit date label and entry
        label_edit_date_entry = tk.Label(
            self, 
            text = "Edit date:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_edit_date_entry.place(relx = 0.515, rely = 0.65, anchor = "center")
        
        self.edit_date_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.edit_date_entry.place(relx = 0.615, rely = 0.65, anchor = "center")
        
        # user edit id label and entry
        label_user_edit = tk.Label(
            self,
            text = "User Edit ID:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_user_edit.place(relx = 0.685, rely = 0.65, anchor = "w")
        
        self.user_edit_p = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.user_edit_p.place(relx = 0.785, rely = 0.65, anchor = "w")
        
        # active label and button
        label_active_p = tk.Label(
            self,
            text = "Active:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_active_p.place(relx = 0.05, rely = 0.7, anchor = "w")
        
        self.active_p = ToggleButton(
            self,
            command=self.active_p,  
            font=('Footlight MT Light', 11),
            fg='#12043e',
            bg='#dbb6ee',
            width=6
        )
        self.active_p.place(relx = 0.15, rely = 0.7, anchor = "center")
        
        # bind the Treeview selection event to update the entries with the selected row's data
        self.tree.bind("<<TreeviewSelect>>", self.populate_entries)
    
        # button to add another privilege to the database
        self.AddPriv = tk.Button(
            self,
            text = "Add privilege",
            command = self.add_priv,
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        self.AddPriv.place(relx = 0.1, rely = 0.8, anchor = "center")
        
        # button that submits the upgraded data of an existing sensor in the treeview
        self.EditPriv = tk.Button(
            self,
            text = "Edit privilege",
            command = self.edit_sel_priv,
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        self.EditPriv.place(relx = 0.26, rely = 0.8, anchor = "center")
        
        # delete selected rows in the treeview
        self.DeleteSelected = tk.Button(
            self,
            text = "Delete selected",
            command =self.delete_selected_priv,
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        self.DeleteSelected.place(relx = 0.42, rely = 0.8, anchor = "center")
        
        # delete all rows in the treeview
        self.DeleteAll = tk.Button(
            self,
            text = "Delete all privileges",
            command = self.delete_all_priv,
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        self.DeleteAll.place(relx = 0.58, rely = 0.8, anchor = "center")
    
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
        self.ClearEntry.place(relx = 0.74, rely = 0.8, anchor = "center")
        
        self.User_Priv = tk.Button(
            self,
            text = "User_has_Priv",
            command = lambda: controller.show_frame(UHP),
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        self.User_Priv.place(relx = 0.9, rely = 0.8, anchor = "center")
        
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
        self.MainM.place(relx = 0.74, rely = 0.9, anchor = "center")
        
        # back button
        self.BackPriv = tk.Button(
            self,
            text = "Back",
            command = lambda: controller.show_frame(ThirdPage),
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        self.BackPriv.place(relx = 0.9, rely = 0.9, anchor = "center")
        
        # configure the tree_frame to adjust with window resizing
        tree_frame.columnconfigure(0, weight=1)
        tree_frame.rowconfigure(0, weight=1)
        
        # bind the resize callback to the parent window
        self.bind("<Configure>", self.on_window_resize)
    
    # function to toggle the state of the ToggleButton
    def active_p(self):
        current_state = self.active_p.cget("text")
        if current_state == "Yes":
            self.active_p.config(text="No", relief=tk.RAISED)
        else:
            self.active_p.config(text="Yes", relief=tk.SUNKEN) 
    
    # function that retrieves data from the entry fields and inserts it into the treeview    
    def add_priv(self):
        # retrieve data from the entry fields
        priv_id = None
        type_p = self.type_entry.get()
        value_p = self.value_entry.get()
        codename = self.codename_entry.get()
        add_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        user_add_p = self.user_add_entry.get()
        edit_date =  None
        user_edit = None
        active_p = self.active_p.cget("text")
        
        # check if any of the required fields are empty
        if not type_p or not value_p or not codename or not user_add_p:
            ms.showerror("Error", "Please fill in all the required fields.*")
            return
        
        if active_p == "Yes":
            active = 1
        else:
            active = 0
        
        params = (priv_id, type_p, value_p, codename, add_date, user_add_p, edit_date, user_edit, active)
        
        self.db_manager.execute_query("INSERT INTO `Privileges` (`Privilege_ID`, `Type`, `Value`, `Codename`, `Add_Date`, `User_Add_ID`, `Edit_Date`, `User_Edit_ID`, `Active`) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)", params)
    
        # insert the data into the table
        self.tree.insert("", tk.END, values=(priv_id, type_p, value_p, codename, add_date, user_add_p, edit_date, user_edit, active), tags = ("tree_color",))
    
        # clear the entry fields
        self.clear_entries()
        
    
    # function that clears the entry fields - accessed throught the clear entries button
    def clear_entries(self):
        # deselect any selected rows in the treeview
        selected_items = self.tree.selection()
        for item in selected_items:
            self.tree.selection_remove(item)
            
        self.priv_id_entry.delete(0, tk.END)
        self.type_entry.delete(0, tk.END)
        self.value_entry.delete(0, tk.END)
        self.codename_entry.delete(0, tk.END)
        self.add_date_entry.delete(0, tk.END)
        self.user_add_entry.delete(0, tk.END)
        self.edit_date_entry.delete(0, tk.END)
        self.user_edit_p.delete(0, tk.END)
        self.active_p.config(text="No", bg="#dbb6ee", relief=tk.RAISED)
        
    
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
        self.priv_id_entry.delete(0, tk.END)
        self.priv_id_entry.insert(0, data[0])
    
        self.type_entry.delete(0, tk.END)
        self.type_entry.insert(0, data[1])
    
        self.value_entry.delete(0, tk.END)
        self.value_entry.insert(0, data[2])
    
        self.codename_entry.delete(0, tk.END)
        self.codename_entry.insert(0, data[3])
        
        self.add_date_entry.delete(0, tk.END)
        self.add_date_entry.insert(0, data[4])
        
        self.user_add_entry.delete(0, tk.END)
        self.user_add_entry.insert(0, data[5])
        
        self.edit_date_entry.delete(0, tk.END)
        self.edit_date_entry.insert(0, data[6])
        
        self.user_edit_p.delete(0, tk.END)
        self.user_edit_p.insert(0, data[7])
        
        # update the active button state based on the data
        if data[8] == "1":
            self.active_p.config(text="Yes", relief=tk.SUNKEN)
            self.active_p.update()
        else:
            self.active_p.config(text="No", relief=tk.RAISED)
            self.active_p.update()
        
        self.active_p.update_idletasks()
        
    def edit_sel_priv(self):
        selected_item = self.tree.selection()
        if not selected_item:
            ms.showerror("Error", "Please select a row to edit.")
            return
        self.edit_priv_pop(selected_item[0])
        
    def disable_priv(self):
        dis_btns = [self.AddPriv, self.EditPriv, self.DeleteSelected, self.DeleteAll, self.ClearEntry, self.User_Priv, self.MainM, self.BackPriv]
        for button in dis_btns:
            button.config(state=tk.DISABLED)
            
    def enable_priv(self):
        enab_btns = [self.AddPriv, self.EditPriv, self.DeleteSelected, self.DeleteAll, self.ClearEntry, self.User_Priv, self.MainM, self.BackPriv]
        for button in enab_btns:
            button.config(state=tk.NORMAL)
            
    def active_pop(self):
        current_state = self.active_priv.cget("text")
        if current_state == "Yes":
            self.active_priv.config(text="No", relief=tk.RAISED)
        else:
            self.active_priv.config(text="Yes", relief=tk.SUNKEN)
        
    # function that updates an existing instance in the table after it was edited using the entries
    def edit_priv_pop(self, selected_item):
        # disable the buttons on the permissions page before creating the pop-up
        self.disable_priv()
        
        # create a pop-up window for editing the selected privilege
        edit_priv = tk.Toplevel(self)
        edit_priv.title("Edit User")
        # edit_priv.geometry("550x350")
        
        priv_window_w = 550
        priv_window_h = 350
        priv_screen_w = edit_priv.winfo_screenwidth()
        priv_screen_h = edit_priv.winfo_screenheight()
        
        priv_center_x = int(priv_screen_w /2 - priv_window_w / 2)
        priv_center_y = int(priv_screen_h /2 - priv_window_h / 2)
        
        edit_priv.geometry(f'{priv_window_w}x{priv_window_h}+{priv_center_x}+{priv_center_y}')
        
        
        edit_priv.configure(bg = '#c8a4d4')
        edit_priv.attributes('-topmost', True)  # bring the window to the top
        edit_priv.attributes('-toolwindow', True)
        edit_priv.focus_set()
        
        # get the data of the selected row
        data = self.tree.item(selected_item, "values")
        
        # create and place entry fields with data from the selected row

        # label and entry type
        label_type_p = tk.Label(
            edit_priv,
            text = "Type:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_type_p.place(relx = 0.05, rely = 0.05, anchor = "w")
        
        self.type_p = tk.Entry(
            edit_priv,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 15
            ) 
        self.type_p.insert(0, data[1])
        self.type_p.place(relx = 0.24, rely = 0.05, anchor = "w")
        
        # label and entry value
        label_value_p = tk.Label(
            edit_priv,
            text = "Value:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_value_p.place(relx = 0.05, rely = 0.15, anchor = "w")
        
        self.value_p = tk.Entry(
            edit_priv,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 15
            ) 
        self.value_p.insert(0, data[2])
        self.value_p.place(relx = 0.24, rely = 0.15, anchor = "w")
        
        #label and entry codename
        label_codename_p = tk.Label(
            edit_priv,
            text = "Codename:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_codename_p.place(relx = 0.05, rely = 0.25, anchor = "w")
        
        self.codename_p = tk.Entry(
            edit_priv,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 15
            )
        self.codename_p.insert(0, data[3])
        self.codename_p.place(relx = 0.24, rely = 0.25, anchor = "w")
        
        # label and entry active
        label_active_pop = tk.Label(
            edit_priv,
            text = "Active:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_active_pop.place(relx = 0.05, rely = 0.35, anchor = "w")
        
        self.active_priv = ToggleButton(
            edit_priv,
            command=self.active_pop,  
            font=('Footlight MT Light', 11),
            fg='#12043e',
            bg='#dbb6ee',
            width=6)
        self.active_priv.place(relx = 0.24, rely = 0.35, anchor = "w")
        
        # update the active button based on the value in the selected row
        if data[8] == "1":
            self.active_priv.config(text="Yes", relief=tk.SUNKEN)
        else:
            self.active_priv.config(text="No", relief=tk.RAISED)
        
        # save button   
        save_priv = tk.Button(
            edit_priv, 
            text = "Save", 
            command = lambda: self.save_edited_priv(edit_priv, selected_item),
            font=('Footlight MT Light', 11),
            fg='#12043e',
            bg='#dbb6ee',
            width = 10
            )
        save_priv.place(relx = 0.7, rely = 0.3, anchor = "center")
        
        # cancel button
        cancel_priv = tk.Button(
            edit_priv,
            text = "Cancel",
            command = lambda: self.cancel_edit_priv(edit_priv),
            font=('Footlight MT Light', 11),
            fg='#12043e',
            bg='#dbb6ee',
            width = 10
            )
        cancel_priv.place(relx = 0.7, rely = 0.4, anchor = "center")
        
        edit_priv.bind("<Destroy>", lambda event: self.cancel_edit_priv(edit_priv))
    
    def cancel_edit_priv(self, edit_priv):
        edit_priv.destroy()
        self.enable_priv()
        
    def save_edited_priv(self, edit_priv, selected_item):
        
        active_priv = 1 if self.active_priv.cget("text") == "Yes" else 0
        
        # retrieve the edited data from the entry fields
        edited_priv = (
            self.tree.item(selected_item, "values")[0], # priv id
            self.type_p.get(),
            self.value_p.get(),
            self.codename_p.get(),
            self.tree.item(selected_item, "values")[4], # add date
            self.tree.item(selected_item, "values")[5], # user add id 
            self.tree.item(selected_item, "values")[6], # edit date
            self.tree.item(selected_item, "values")[7], # user edit id
            active_priv
            )
        
        # retrieve the current data the of the selected row
        current_priv_data = self.tree.item(selected_item, "values")
        
        print("Edited Data:", edited_priv)
        print("Current Data:", current_priv_data)

        
        # compare edited data with current data to check for changes
        changed_priv = False
        for ed_priv, current_priv in zip(edited_priv, current_priv_data):
            ed_priv_str = str(ed_priv)
            current_priv_str = str(current_priv)
            
            if ed_priv_str != current_priv_str:
                changed_priv = True
                break
        
        print("Changes Detected:", changed_priv)   
        
        if not changed_priv:
            ms.showinfo("No Changes", "No changes were made.", parent = edit_priv)
            edit_priv.destroy()
            self.enable_priv()
            return
        
        # ask for confirmation to save changes
        confirmation = ms.askyesnocancel("Save Changes", "Save changes to this user?", parent = edit_priv)
        if confirmation:
            # update the database with the edited data
            active = 1 if edited_priv[-1] == 1 else 0
            
            edit_date_priv = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') # current time of the edit
            user_edit_priv = None # none until login protocol
            
            params = (
                edited_priv[1], # type
                edited_priv[2], # value
                edited_priv[3], # codename
                self.tree.item(selected_item, "values")[4], # add date
                self.tree.item(selected_item, "values")[5], # user add id
                edit_date_priv, # edit date
                user_edit_priv, # user edit id
                active, # active
                edited_priv[0] # priv id
                )
        
            # query to be sent to database
            self.db_manager.execute_query("UPDATE `Privileges` SET `Type` = %s, `Value` = %s, `Codename` = %s, `Add_Date` = %s, `User_Add_ID` = %s,`Edit_Date` = %s, `User_Edit_ID` = %s, `Active` = %s WHERE `Privileges`.`Privilege_ID` = %s", params)
            
            # data to be inserted into treeview
            edited_priv_treeview = (
                edited_priv[0], # priv id
                edited_priv[1], # type
                edited_priv[2], # value
                edited_priv[3], # codename
                self.tree.item(selected_item, "values")[4], # add date
                self.tree.item(selected_item, "values")[5], #user add id
                edit_date_priv, # edit date
                user_edit_priv, # user edit id
                active # active
                )
            
            # insertion into treeview
            self.tree.item(selected_item, values = edited_priv_treeview)
            
            edit_priv.destroy()
            self.enable_priv()
            
        elif confirmation is None:
            # user clicked "Cancel" in the pop-up, close the edit pop-up
            pass
        else:
            # user clicked "No" in the pop-up, close the edit pop-up  
            edit_priv.destroy()
            self.enable_priv()
            
    # function that removes selected instances from the table
    def delete_selected_priv(self, selected_items=None):
        # if selected_items is None, get a list of selected items in the treeview
        if selected_items is None:
            selected_items = self.tree.selection()

        if not selected_items:
            ms.showerror("Error", "Please select one or more rows to delete.")
            return

        # if delete_all_priv_flag is True, skip the confirmation pop-up
        if not self.delete_all_priv_flag:
            # confirm the deletion with the user
            if not ms.askyesno("Confirm Deletion", "Are you sure you want to delete the selected row(s)?"):
                return

        # remove the selected rows from the Treeview
        for item in selected_items:
            priv_id = self.tree.item(item, "values")[0]
            self.db_manager.execute_query("DELETE FROM `Privileges` WHERE `Privileges`.`Privilege_ID` = %s", (priv_id,))
            self.tree.delete(item)
            
    # function that removes all instances from the table
    def delete_all_priv(self):
        # set the flag to indicate "Delete all privileges" button was clicked
        self.delete_all_priv_flag = True

        # confirm the deletion with the user
        if not ms.askyesno("Confirm Deletion", "Are you sure you want to delete all sensors?"):
            # reset the flag if the user cancels the action
            self.delete_all_priv_flag = False
            return

        # execute query to delete all rows from the database
        self.db_manager.execute_query("DELETE FROM `Privileges`", [])        

        # get all items in the Treeview and pass them to the delete_selected_rows function
        all_items = self.tree.get_children()
        self.delete_selected_priv(all_items)

        # reset the flag after the deletion
        self.delete_all_priv_flag = False
        
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
    
    # calls the admin password window before proceeding further granting restricted access to unauthorized personnel
    def admin_pass_request(self, controller, next_page):
        admin_pass_window = AdminPasswordWindow(controller, next_page)
        admin_pass_window.grab_set()
