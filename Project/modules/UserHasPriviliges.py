import tkinter as tk
from tkinter import messagebox as ms
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import Scrollbar
import datetime
from modules.ToggleButton import ToggleButton
from modules.ThirdPage import ThirdPage

class UHP(tk.Frame):
    def __init__(self, parent, controller, db_manager):
        from modules.Privileges import Privileges
        from modules.StartPage import StartPage
        tk.Frame.__init__(self, parent)
        self.configure(bg='#d398fa')
        self.db_manager = db_manager
        self. del_all_uhp_flag = False # flag to indicate if "Delete all" button was clicked
        
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
        self.tree = ttk.Treeview(tree_frame, columns=("UHP_ID", "Priv_ID", "User_ID", "Add_Date", "User_Add_ID", "Edit_Date", "User_Edit_ID", "Value", "Active"), show="headings")
       
       # define the headings of the treeview
        self.tree.heading("UHP_ID", text = "UHP ID")
        self.tree.heading("Priv_ID", text = "Priv ID")
        self.tree.heading("User_ID", text = "User ID")
        self.tree.heading("Add_Date", text = "Add date")
        self.tree.heading("User_Add_ID", text = "User Add ID ")
        self.tree.heading("Edit_Date", text = "Edit date")
        self.tree.heading("User_Edit_ID", text = "User Edit ID ")
        self.tree.heading("Value", text = "Value")
        self.tree.heading("Active", text = "Active")
    
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # configure tag colors for even and odd rows
        self.tree.tag_configure("tree_color", background = '#bca6e1')
        
        tableUP = "User_Has_Priv"
        
        UHP_data = db_manager.fetch_table(tableUP)
        
        for UP_data in UHP_data:
            self.tree.insert("", tk.END, values=UP_data, tags=("tree_color",))
        
        # create vertical scrollbar and link it to the treeview
        v_scroll = Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=v_scroll.set)
        v_scroll.pack(side="right", fill="y")
        
        # pack the Treeview within tree_frame 
        self.tree.pack(expand=True, fill="both")
        
        # create entries and labels to facilitate the management of the treeview data
        
        # uhp id and entry
        label_uhp_id =  tk.Label(
            self,
            text = "UHP ID:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_uhp_id.place(relx = 0.05, rely = 0.6, anchor = "w")
        
        self.uhp_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.uhp_entry.place(relx = 0.18, rely = 0.6, anchor = "center")
        
        # privilege id label and entry
        label_priv_idUP = tk.Label(
            self,
            text = "Privilege ID*:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_priv_idUP.place(relx = 0.25, rely = 0.6, anchor = "w")
        
        self.priv_id_UP_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.priv_id_UP_entry.place(relx = 0.41, rely = 0.6, anchor = "center")
        
        # user id label and entry
        label_user_id_UP = tk.Label(
            self,
            text = "User ID*:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_user_id_UP.place(relx = 0.48, rely = 0.6, anchor = "w")
        
        self.user_id_UP_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.user_id_UP_entry.place(relx = 0.61, rely = 0.6, anchor = "center")
        
        # add date label and entry
        label_add_dateUP = tk.Label(
            self, 
            text = "Add date:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_add_dateUP.place(relx = 0.685, rely = 0.6, anchor = "w")
        
        self.add_date_UP_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.add_date_UP_entry.place(relx = 0.818, rely = 0.6, anchor = "center")
        
        # user add id label and entry
        label_user_add_UP = tk.Label(
           self, 
           text = "User Add ID:",
           font = ('Footlight MT Light', 11),
           bg = '#c8a4d4',
           fg = '#12043e'
           )
        label_user_add_UP.place(relx = 0.05, rely = 0.65, anchor = "w")
       
        self.user_add_UP_entry = tk.Entry(
           self,
           font = ('Footlight MT Light', 11),
           fg = '#12043e',
           bg = '#dbb6ee',
           width = 12                         
           )
        self.user_add_UP_entry.place(relx = 0.215, rely = 0.65, anchor = "center")
        
        # edit date label and entry
        label_edit_date_UP = tk.Label(
            self, 
            text = "Edit date:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_edit_date_UP.place(relx = 0.32, rely = 0.65, anchor = "center")
        
        self.edit_date_UP_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.edit_date_UP_entry.place(relx = 0.419, rely = 0.65, anchor = "center")
        
        # user edit id label and entry
        label_user_edit_UP = tk.Label(
            self,
            text = "User Edit ID:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_user_edit_UP.place(relx = 0.54, rely = 0.65, anchor = "center")
        
        self.user_edit_UP = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.user_edit_UP.place(relx = 0.65, rely = 0.65, anchor = "center")
        
        # value label and entry
        label_value_UP = tk.Label(
            self,
            text = "Value*:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_value_UP.place(relx = 0.72, rely = 0.65, anchor = "w")
        
        self.value_UP_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.value_UP_entry.place(relx = 0.785, rely = 0.65, anchor = "w")
        
        # active label and button
        label_active_UP = tk.Label(
            self,
            text = "Active:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_active_UP.place(relx = 0.05, rely = 0.7, anchor = "w")
        
        self.active_UP = ToggleButton(
            self,
            command=self.active_UP,  
            font=('Footlight MT Light', 11),
            fg='#12043e',
            bg='#dbb6ee',
            width=6
        )
        self.active_UP.place(relx = 0.15, rely = 0.7, anchor = "center")
        
        # configure the tree_frame to adjust with window resizing
        tree_frame.columnconfigure(0, weight=1)
        tree_frame.rowconfigure(0, weight=1)
        
        # bind the Treeview selection event to update the entries with the selected row's data
        self.tree.bind("<<TreeviewSelect>>", self.populate_entries_UP)
    
        # button to add another privilege to the database
        self.AddUHP = tk.Button(
            self,
            text = "Add UHP",
            command = self.add_uhp,
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        self.AddUHP.place(relx = 0.1, rely = 0.8, anchor = "center")
        
        # button that submits the upgraded data of an existing sensor in the treeview
        self.EditUHP = tk.Button(
            self,
            text = "Edit UHP",
            command = self.edit_sel_uhp,
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        self.EditUHP.place(relx = 0.26, rely = 0.8, anchor = "center")
        
        # delete selected rows in the treeview
        self.DeleteSelected = tk.Button(
            self,
            text = "Delete selected",
            command =self.del_selected_uhp,
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
            text = "Delete all UHP",
            command = self.del_all_uhp,
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
            command = self.clear_entries_UP,
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        self.ClearEntry.place(relx = 0.74, rely = 0.8, anchor = "center")
        
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
        self.MainM.place(relx = 0.9, rely = 0.8, anchor = "center")
        
        # back button
        self.BackUHP = tk.Button(
            self,
            text = "Back",
            command = lambda: controller.show_frame(Privileges),
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        self.BackUHP.place(relx = 0.9, rely = 0.9, anchor = "center")
        
        # configure the tree_frame to adjust with window resizing
        tree_frame.columnconfigure(0, weight=1)
        tree_frame.rowconfigure(0, weight=1)
        
        # bind the resize callback to the parent window
        self.bind("<Configure>", self.on_window_resize)
    
    # function to toggle the state of the ToggleButton
    def active_UP(self):
        current_state = self.active_UP.cget("text")
        if current_state == "Yes":
            self.active_UP.config(text="No", relief=tk.RAISED)
        else:
            self.active_UP.config(text="Yes", relief=tk.SUNKEN)
            
    # function that populates the entry fields with data from selected row in the treeview
    def populate_entries_UP(self, event):
        selected_items = self.tree.selection()

        if not selected_items:
            # no row is selected, so clear the entry fields
            self.clear_entries_UP()
            return

        # get the selected item from the Treeview
        selected_item = selected_items[0]

        # get the data of the selected row
        data = self.tree.item(selected_item, "values")
    
        # update the entries with the data
        self.uhp_entry.delete(0, tk.END)
        self.uhp_entry.insert(0, data[0])
    
        self.priv_id_UP_entry.delete(0, tk.END)
        self.priv_id_UP_entry.insert(0, data[1])
    
        self.user_id_UP_entry.delete(0, tk.END)
        self.user_id_UP_entry.insert(0, data[2])
    
        self.add_date_UP_entry.delete(0, tk.END)
        self.add_date_UP_entry.insert(0, data[3])
        
        self.user_add_UP_entry.delete(0, tk.END)
        self.user_add_UP_entry.insert(0, data[4])
        
        self.edit_date_UP_entry.delete(0, tk.END)
        self.edit_date_UP_entry.insert(0, data[5])
        
        self.user_edit_UP.delete(0, tk.END)
        self.user_edit_UP.insert(0, data[6])
        
        self.value_UP_entry.delete(0, tk.END)
        self.value_UP_entry.insert(0, data[7])
        
        # update the active button state based on the data
        if data[8] == "1":
            self.active_UP.config(text="Yes", relief=tk.SUNKEN)
            self.active_UP.update()
        else:
            self.active_UP.config(text="No", relief=tk.RAISED)
            self.active_UP.update()
        
        self.active_UP.update_idletasks()
        
        # function that clears the entry fields - accessed throught the clear entries button
    def clear_entries_UP(self):
        # deselect any selected rows in the treeview
        selected_items = self.tree.selection()
        for item in selected_items:
            self.tree.selection_remove(item)
            
        self.uhp_entry.delete(0, tk.END)
        self.priv_id_UP_entry.delete(0, tk.END)
        self.user_id_UP_entry.delete(0, tk.END)
        self.add_date_UP_entry.delete(0, tk.END)
        self.user_add_UP_entry.delete(0, tk.END)
        self.edit_date_UP_entry.delete(0, tk.END)
        self.user_edit_UP.delete(0, tk.END)
        self.value_UP_entry.delete(0, tk.END)
        self.active_UP.config(text="No", bg="#dbb6ee", relief=tk.RAISED)
        
    def add_uhp(self):
        uhp_id = None
        priv_id_uhp = self.priv_id_UP_entry.get()
        user_id_uhp = self.user_id_UP_entry.get()
        add_date_uhp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        user_add_uhp = self.user_add_UP_entry.get()
        edit_date_uhp = None
        user_edit_uhp = None
        value_uhp = self.value_UP_entry.get()
        active_uhp = self.active_UP.cget("text")
        
        if not priv_id_uhp or not user_id_uhp or not value_uhp:
            ms.showerror("Error", "Please fill in all the required fields.*")
            return
        
        if active_uhp == "Yes":
            active_up = 1
        else:
            active_up = 0
            
        # check if data is already into the database before adding it    
        select_param = (priv_id_uhp, user_id_uhp, value_uhp)
        result = self.db_manager.execute_query("SELECT * FROM `User_Has_Priv` WHERE `Priv_ID` = %s AND `User_ID` = %s AND `Value` = %s", select_param)
        
        if(result):
            ms.showerror("Error", "The data already exists in the database.")
            return
        
        else:
            # insert data in database
            param = (uhp_id, priv_id_uhp, user_id_uhp, add_date_uhp, user_add_uhp, edit_date_uhp, user_edit_uhp, value_uhp, active_up)
            self.db_manager.execute_query("INSERT INTO `User_Has_Priv` (`UHP_ID`, `Priv_ID`, `User_ID`, `Add_Date`, `User_Add_ID`, `Edit_Date`, `User_Edit_ID`, `Value`, `Active`) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)", param)
        
            # insert the data into the table
            self.tree.insert("", tk.END, values=(uhp_id, priv_id_uhp, user_id_uhp, add_date_uhp, user_add_uhp, edit_date_uhp, user_edit_uhp, value_uhp, active_up), tags = ("tree_color",))
        
            # clear the entry fields
            self.clear_entries_UP()
        
    def edit_sel_uhp(self):
        selected_item = self.tree.selection()
        if not selected_item:
            ms.showerror("Error", "Please select a row to edit.")
            return
        self.edit_uhp_pop(selected_item[0])
        
    def disable_uhp(self):
        dis_uhp = [self.AddUHP, self.EditUHP, self.DeleteSelected, self.DeleteAll, self.ClearEntry, self.MainM, self.BackUHP, self.uhp_entry, self.priv_id_UP_entry, self.user_id_UP_entry, self.add_date_UP_entry, self.user_add_UP_entry, self.edit_date_UP_entry, self.user_edit_UP, self.value_UP_entry, self.active_UP]
        for button in dis_uhp:
            button.config(state=tk.DISABLED)
            
    def enable_uhp(self):
        enb_uhp = [self.AddUHP, self.EditUHP, self.DeleteSelected, self.DeleteAll, self.ClearEntry, self.MainM, self.BackUHP, self.uhp_entry, self.priv_id_UP_entry, self.user_id_UP_entry, self.add_date_UP_entry, self.user_add_UP_entry, self.edit_date_UP_entry, self.user_edit_UP, self.value_UP_entry, self.active_UP]
        for btn in enb_uhp:
            btn.config(state=tk.NORMAL)
            
    def active_UHP(self):
        c_state = self.active_uhp_pop.cget("text")
        if c_state == "Yes":
            self.active_uhp_pop.config(text="No", relief=tk.RAISED)
        else:
            self.active_uhp_pop.config(text="Yes", relief=tk.SUNKEN)
    
    def edit_uhp_pop(self, selected_item):
        # disable the buttons on the permissions page before creating the pop-up
        self.disable_uhp()
        
        # create a pop-up window for editing the selected uhp
        edit_uhp = tk.Toplevel(self)
        edit_uhp.title("Edit UHP")
        # edit_uhp.geometry("550x350")
        edit_uhp.configure(bg = '#c8a4d4')
        edit_uhp.attributes('-topmost', True)
        edit_uhp.focus_set()
        
        window_w = 550
        window_h = 350
        screen_w = edit_uhp.winfo_screenwidth()
        screen_h = edit_uhp.winfo_screenheight()
        
        center_x = int(screen_w /2 - window_w / 2)
        center_y = int(screen_h /2 - window_h / 2)
        
        edit_uhp.geometry(f'{window_w}x{window_h}+{center_x}+{center_y}')
        
        data = self.tree.item(selected_item, "values")
        
        # create and place entry fields with data from the selected row
        # label and entry priv id  
        label_priv_pop = tk. Label(
            edit_uhp,
            text = "Priv ID:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_priv_pop.place(relx = 0.05, rely = 0.05, anchor = "w")
        
        self.priv_pop_entry = tk.Entry(
            edit_uhp,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 15
            ) 
        self.priv_pop_entry.insert(0, data[1])
        self.priv_pop_entry.place(relx = 0.24, rely = 0.05, anchor = "w")
        
        # label and entry user id
        label_user_pop = tk.Label(
            edit_uhp,
            text = "User ID:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_user_pop.place(relx = 0.05, rely = 0.15, anchor = "w")
        
        self.user_pop_entry = tk.Entry(
            edit_uhp,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 15
            ) 
        self.user_pop_entry.insert(0, data[2])
        self.user_pop_entry.place(relx = 0.24, rely = 0.15, anchor = "w")
        
        # label and entry value
        label_value_uhp_pop = tk.Label(
            edit_uhp,
            text = "Value:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_value_uhp_pop.place(relx = 0.05, rely = 0.25, anchor = "w")
        
        self.value_uhp_entry = tk.Entry(
            edit_uhp,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 15
            ) 
        self.value_uhp_entry.insert(0, data[7])
        self.value_uhp_entry.place(relx = 0.24, rely = 0.25, anchor = "w")
        
        # label and entry user add 
        label_active_uhp_pop = tk.Label(
            edit_uhp,
            text = "Active:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_active_uhp_pop.place(relx = 0.05, rely = 0.35, anchor = "w")
        
        self.active_uhp_pop = ToggleButton(
            edit_uhp,
            command=self.active_UHP,  
            font=('Footlight MT Light', 11),
            fg='#12043e',
            bg='#dbb6ee',
            width=6)
        self.active_uhp_pop.place(relx = 0.24, rely = 0.35, anchor = "w")
        
        # update the active button based on the value in the selected row
        if data[8] == "1":
            self.active_uhp_pop.config(text="Yes", relief=tk.SUNKEN)
        else:
            self.active_uhp_pop.config(text="No", relief=tk.RAISED)
            
        # save button    
        save_uhp = tk.Button(
            edit_uhp, 
            text = "Save", 
            command = lambda: self.save_edited_uhp(edit_uhp, selected_item),
            font=('Footlight MT Light', 11),
            fg='#12043e',
            bg='#dbb6ee',
            width = 10
            )
        save_uhp.place(relx = 0.7, rely = 0.3, anchor = "center")
        
        # cancel button
        cancel_uhp = tk.Button(
            edit_uhp,
            text = "Cancel",
            command = lambda: self.cancel_edit_uhp(edit_uhp),
            font=('Footlight MT Light', 11),
            fg='#12043e',
            bg='#dbb6ee',
            width = 10
            )
        cancel_uhp.place(relx = 0.7, rely = 0.4, anchor = "center")
        
        edit_uhp.bind("<Destroy>", lambda event: self.cancel_edit_uhp(edit_uhp))
        
    def cancel_edit_uhp(self, edit_uhp):
        edit_uhp.destroy()
        self.enable_uhp()
        
    def save_edited_uhp(self, edit_uhp, selected_item):
        # retrieve the edited data from the entry fields
        activeUP = 1 if self.active_uhp_pop.cget("text") == "Yes" else 0
        
        # retrieve the current data the of the selected row
        current_uhp_data = self.tree.item(selected_item, "values")
        
        edited_uhp = (
            self.tree.item(selected_item, "values")[0],
            self.priv_pop_entry.get(),
            self.user_pop_entry.get(),
            self.tree.item(selected_item, "values")[3],        # add date
            self.tree.item(selected_item, "values")[4],        # user add 
            self.tree.item(selected_item, "values")[5],        # edit date
            self.tree.item(selected_item, "values")[6],        # user edit
            self.value_uhp_entry.get(),
            activeUP
            )
        

        changed = False
        for edited_val, current_val in zip(edited_uhp, current_uhp_data):
            edited_val_str = str(edited_val)
            current_val_str = str(current_val)
            
            if edited_val_str != current_val_str:
                changed = True
                break
    
        print("Changes Detected:", changed)
        
        if not changed:
            ms.showinfo("No Changes", "No changes were made.", parent = edit_uhp)
            edit_uhp.destroy()
            self.enable_uhp()
            return
            
        # ask for confirmation to save changes
        confirmation = ms.askyesnocancel("Save Changes", "Save changes to this user?", parent = edit_uhp)
        if confirmation:
            # update the database with the edited data
            active = 1 if edited_uhp[-1] == 1 else 0
                    
            edit_date_uhp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') # current time of the edit
            user_edit_uhp = None # none until login protocol
                    
            param = (
                edited_uhp[1], # priv id
                edited_uhp[2], # user id
                self.tree.item(selected_item, "values")[3],        # add date
                self.tree.item(selected_item, "values")[4],        # user add 
                edit_date_uhp,                                     # edit date
                user_edit_uhp,                                     # user edit
                edited_uhp[7],                                     # value
                active,                                            # active
                edited_uhp[0]                                      # uhp id
                )
                    
            # query to be sent to database
            self.db_manager.execute_query("UPDATE `User_Has_Priv` SET `Priv_ID` = %s, `User_ID` = %s, `Add_Date` = %s, `User_Add_ID` = %s, `Edit_Date` = %s, `User_Edit_ID` = %s, `Value` = %s, `Active` = %s WHERE `User_Has_Priv`.`UHP_ID` = %s", param)
                    
            # data to be inserted into treeview
            edited_uhp_treeview = (
                edited_uhp[0], # uhp id
                edited_uhp[1], # priv id
                edited_uhp[2], # user id
                edited_uhp[3], # add date
                edited_uhp[4], # user add id 
                edit_date_uhp, # edit date
                user_edit_uhp, # user edit id
                edited_uhp[7], # value
                active # active
                )
                    
            # insertion into treeview
            self.tree.item(selected_item, values = edited_uhp_treeview) 
                    
            edit_uhp.destroy()
            self.enable_uhp()
                
        elif confirmation is None:
            # user clicked "Cancel" in the pop-up, close the edit pop-up
            pass
        else:
            # user clicked "No" in the pop-up, close the edit pop-up
            edit_uhp.destroy()
            self.enable_uhp()
            
    def del_selected_uhp(self, selected_items=None):
        # if selected_items is None, get a list of selected items in the treeview
        if selected_items is None:
            selected_items = self.tree.selection()

        if not selected_items:
            ms.showerror("Error", "Please select one or more rows to delete.")
            return

        # if del_all_uhp_flag is True, skip the confirmation pop-up
        if not self.del_all_uhp_flag:
            # confirm the deletion with the user
            if not ms.askyesno("Confirm Deletion", "Are you sure you want to delete the selected row(s)?"):
                return

        # remove the selected rows from the Treeview
        for item in selected_items:
            uhp_id = self.tree.item(item, "values")[0]
            self.db_manager.execute_query("DELETE FROM `User_Has_Priv` WHERE `User_Has_Priv`.`UHP_ID` = %s", (uhp_id,))
            self.tree.delete(item)
            
    def del_all_uhp(self):
        # set the flag to indicate "Delete all uhp" button was clicked
        self.del_all_uhp_flag = True

        # confirm the deletion with the user
        if not ms.askyesno("Confirm Deletion", "Are you sure you want to delete all sensors?"):
            # reset the flag if the user cancels the action
            self.del_all_uhp_flag = False
            return

        # execute query to delete all rows from the database
        self.db_manager.execute_query("DELETE FROM `User_Has_Priv`", [])        

        # get all items in the Treeview and pass them to the delete_selected_rows function
        all_items = self.tree.get_children()
        self.del_selected_uhp(all_items)

        # reset the flag after the deletion
        self.del_all_uhp_flag = False
                
    # function that loads an image from a file path and resizes it to the specified dimensions    
    def load_and_resize_image(self, width, height):
        image = Image.open(self.image_path)
        image = image.resize((width, height), Image.LANCZOS)
        return ImageTk.PhotoImage(image)
            
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
