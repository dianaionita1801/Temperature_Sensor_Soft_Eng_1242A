import tkinter as tk
from tkinter import messagebox as ms
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import Scrollbar
import datetime
from modules.ToggleButton import ToggleButton
from modules.AdminPasswordWindow import AdminPasswordWindow


class FifthPage(tk.Frame):
    def __init__(self, parent, controller, db_manager):
        from modules.StartPage import StartPage
        tk.Frame.__init__(self, parent)
        self.configure(bg='#d398fa')
        self.db_manager = db_manager
        self.delete_all_rooms_flag = False  # flag to indicate if "Delete all rooms" button was clicked 
        
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
        self.tree = ttk.Treeview(tree_frame, columns=("Room_ID", "Room_Name", "Add_Date", "User_Add_ID", "Edit_Date", "User_Edit_ID", "Active"), show="headings")
        
        # define the headings of the treeview
        self.tree.heading("Room_ID", text="Room ID")
        self.tree.heading("Room_Name", text="Room Name")
        self.tree.heading("Add_Date", text="Add date")
        self.tree.heading("User_Add_ID", text="User Add ID")
        self.tree.heading("Edit_Date", text="Edit date")
        self.tree.heading("User_Edit_ID", text="User Edit ID")
        self.tree.heading("Active", text="Active")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # configure tag colors for even and odd rows
        self.tree.tag_configure("tree_color", background = '#bca6e1')
    
        # add some sample data to the Treeview (replace this with data from your database)
        # self.tree.insert("", "end", values=(1, "Server Room", "2023-06-26", 1, "2023-06-26", 1, "Yes"),tags=("tree_color",))
        # self.tree.insert("", "end", values=(2, "IT", "2023-06-26", 2, "2023-07-18", 2, "No"), tags=("tree_color",))
        
        tableR = "Room"
       
        # fetch data from the database
        rooms_data = self.db_manager.fetch_table(tableR)

       # populate the Treeview with the fetched data
        for room_data in rooms_data:
           self.tree.insert("", tk.END, values=room_data, tags=("tree_color",))
    
        # create vertical scrollbar and link it to the treeview
        v_scroll = Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=v_scroll.set)
        v_scroll.pack(side="right", fill="y")
    
    
        # pack the Treeview within tree_frame 
        self.tree.pack(expand=True, fill="both")
    
        # create entries and labels to facilitate the management of the treeview data
        
        # room id label and entry
        label_room_id = tk.Label(
            self,
            text = "Room ID*:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_room_id.place(relx = 0.05, rely = 0.6, anchor = "w")
        
        self.room_id_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.room_id_entry.place(relx = 0.188, rely = 0.6, anchor = "center")
        
        # room name label and entry 
        label_room_name = tk.Label(
            self,
            text = "Room Name*:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_room_name.place(relx = 0.26, rely = 0.6, anchor = "w")
        
        self.room_name_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.room_name_entry.place(relx = 0.42, rely = 0.6, anchor = "center")
                
        # add date label and entry
        label_add_dater = tk.Label(
            self,
            text = "Add Date:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_add_dater.place(relx = 0.487, rely = 0.6, anchor = "w")
        
        self.add_dater_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.add_dater_entry.place(relx = 0.6245, rely = 0.6, anchor = "center")   
          
        # add user id label and entry
        label_user_add_idr = tk.Label(
            self,
            text = "Add User ID:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_user_add_idr.place(relx = 0.7, rely = 0.6, anchor = "w")  
        
        self.user_add_idr_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.user_add_idr_entry.place(relx = 0.857, rely = 0.6, anchor = "center")
        
        # edit date label and entry
        label_edit_dater = tk.Label(
            self,
            text = "Edit Date:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_edit_dater.place(relx = 0.05, rely = 0.65, anchor = "w")  
        
        self.edit_dater_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.edit_dater_entry.place(relx=0.185, rely=0.65, anchor="center")
        
        # edit user id label and entry
        label_user_edit_idr = tk.Label(
            self,
            text = "Edit User ID",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_user_edit_idr.place(relx = 0.26, rely = 0.65, anchor = "w") 
        
        self.user_edit_idr_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.user_edit_idr_entry.place(relx=0.414, rely=0.65, anchor="center")
        
        # active label and entry
        label_activer = tk.Label(
            self,
            text = "Active:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_activer.place(relx = 0.487, rely = 0.65, anchor = "w")
        
        self.activer_entry = ToggleButton(
            self,
            command = self.toggle_active, 
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 6)
        self.activer_entry.place(relx=0.59, rely=0.65, anchor="center")
    
    
        # bind the Treeview selection event to update the entries with the selected row's data
        self.tree.bind("<<TreeviewSelect>>", self.populate_entries)
    
        # button to add another sensor to the database
        self.AddRoom = tk.Button(
            self,
            text = "Add room",
            command = self.add_room,
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        self.AddRoom.place(relx = 0.1, rely = 0.85, anchor = "center")
        
        # button that submits the upgraded data of an existing sensor in the treeview
        self.EditRoom = tk.Button(
            self,
            text = "Edit room",
            command = self.edit_selected_room,
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        self.EditRoom.place(relx = 0.26, rely = 0.85, anchor = "center")
        
        # delete selected rows in the treeview
        self.DeleteSelectedR = tk.Button(
            self,
            text = "Delete selected",
            command = self.delete_selected_rooms,
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        self.DeleteSelectedR.place(relx = 0.42, rely = 0.85, anchor = "center")
        
        # delete all rows in the treeview
        self.DeleteAllR = tk.Button(
            self,
            text = "Delete all rooms",
            command = self.delete_all_rooms,
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        self.DeleteAllR.place(relx = 0.58, rely = 0.85, anchor = "center")
    
        # clear entries button
        self.ClearEntryR = tk.Button(
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
        self.ClearEntryR.place(relx = 0.74, rely = 0.85, anchor = "center")
        
        # back button
        self.BackFif = tk.Button(
            self,
            text = "Back",
            command = lambda: controller.show_frame(StartPage),
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        self.BackFif.place(relx = 0.9, rely = 0.85, anchor = "center")
        
        # configure the tree_frame to adjust with window resizing
        tree_frame.columnconfigure(0, weight=1)
        tree_frame.rowconfigure(0, weight=1)
        
        # bind the resize callback to the parent window
        self.bind("<Configure>", self.on_window_resize)
    
    # function to toggle the state of the ToggleButton
    def toggle_active(self):
        current_state = self.activer_entry.cget("text")
        if current_state == "Yes":
            self.activer_entry.config(text="No", relief=tk.RAISED)
        else:
            self.activer_entry.config(text="Yes", relief=tk.SUNKEN)    
    
    # function that retrieves data from the entry fields and inserts it into the treeview    
    def add_room(self):
        # retrieve data from the entry fields
        room_id = None
        room_name = self.room_name_entry.get()
        user_addr = self.user_add_idr_entry.get()
        edit_dater = None
        user_editr = None
    
        # get the text value of the ToggleButton ("Yes" or "No")
        active_state = self.activer_entry.cget("text")
        
        if not room_id or not room_name:
            ms.showerror("Error", "Please fill in all the required fields *.")
            return
        
        if active_state == "Yes":
            active = 1
        else:
            active = 0
            
        # get the current date and time
        add_dater = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        select_param = room_name
        result = self.db_manager.execute_query("SELECT * FROM `Room` WHERE `Room_Name` = %s", select_param)
        
        if(result):
            ms.showerror("Error", "The data already exists in the database.")
            return
        
        else:
            # pass the values of the parameters to the params list
            paramtr = (room_id, room_name, add_dater, user_addr, edit_dater, user_editr, active)
            
            self.db_manager.execute_query("INSERT INTO `Room` (`Room_ID`, `Room_Name`, `Add_Date`, `User_Add_ID`, `Edit_Date`, `User_Edit_ID`, `Active`) values (%s, %s, %s, %s, %s, %s, %s)", paramtr)
            
            # insert the data into the table
            self.tree.insert("", "end", values=(room_id, room_name, add_dater, user_addr, edit_dater, user_editr, active), tags = ("tree_color",))
        
            # clear the entry fields
            self.clear_entries()
    
    # function that clears the entry fields - accessed throught the clear entries button
    def clear_entries(self):
        # deselect any selected rows in the treeview
        selected_items = self.tree.selection()
        for item in selected_items:
            self.tree.selection_remove(item)
        
        self.room_id_entry.delete(0, tk.END)
        self.room_name_entry.delete(0, tk.END)
        self.add_dater_entry.delete(0, tk.END)
        self.user_add_idr_entry.delete(0, tk.END)
        self.edit_dater_entry.delete(0, tk.END)
        self.user_edit_idr_entry.delete(0, tk.END)
        self.activer_entry.config(text="No", bg="#dbb6ee", relief=tk.RAISED)
    
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
        self.room_id_entry.delete(0, tk.END)
        self.room_id_entry.insert(0, data[0])
    
        self.room_name_entry.delete(0, tk.END)
        self.room_name_entry.insert(0, data[1])
    
        self.add_dater_entry.delete(0, tk.END)
        self.add_dater_entry.insert(0, data[2])
    
        self.user_add_idr_entry.delete(0, tk.END)
        self.user_add_idr_entry.insert(0, data[3])
    
        self.edit_dater_entry.delete(0, tk.END)
        self.edit_dater_entry.insert(0, data[4])
    
        self.user_edit_idr_entry.delete(0, tk.END)
        self.user_edit_idr_entry.insert(0, data[5])
    
        # update the ToggleButton state based on the data
        if data[6] == "Yes":
            self.activer_entry.config(text="Yes", relief=tk.SUNKEN)
        else:
            self.activer_entry.config(text="No", relief=tk.RAISED)
            
    def toggle_active_p(self):
        current_st = self.active_room.cget("text")
        if current_st == "Yes":
            self.active_room.config(text="No", relief=tk.RAISED)
        else:
            self.active_room.config(text="Yes", relief=tk.SUNKEN)
    
    def dis_btn_room(self):
        btns_to_dis = [self.AddRoom, self.EditRoom, self.DeleteSelectedR, self.DeleteAllR, self.ClearEntryR, self.BackFif, self.room_id_entry, self.room_name_entry, self.add_dater_entry, self.user_add_idr_entry, self.edit_dater_entry, self.user_edit_idr_entry, self.activer_entry]
        for btn in btns_to_dis:
            btn.config(state=tk.DISABLED)

    def enab_btn_room(self):
        btns_to_enab = [self.AddRoom, self.EditRoom, self.DeleteSelectedR, self.DeleteAllR, self.ClearEntryR, self.BackFif, self.room_id_entry, self.room_name_entry, self.add_dater_entry, self.user_add_idr_entry, self.edit_dater_entry, self.user_edit_idr_entry, self.activer_entry]
        for btn in btns_to_enab:
            btn.config(state=tk.NORMAL)            
            
    def edit_selected_room(self):
        selected_room = self.tree.selection()
        if not selected_room:
            ms.showerror("Error", "Please select a row to edit.")    
            return
        self.edit_room_popup(selected_room[0])
     
    # function that updates an existing instance in the treeview after it was edited using the entries    
    def edit_room_popup(self, selected_room):
        # disable the buttons on the room management page before creating the pop-up
        self.dis_btn_room()
        
        edit_room_p =  tk.Toplevel(self)
        edit_room_p.title("Edit Room")
        # edit_room_p.geometry("480x250")
        
        room_window_w = 480
        room_window_h = 250
        room_screen_w = edit_room_p.winfo_screenwidth()
        room_screen_h = edit_room_p.winfo_screenheight()
        
        room_center_x = int(room_screen_w /2 - room_window_w / 2)
        room_center_y = int(room_screen_h /2 - room_window_h / 2)
        
        edit_room_p.geometry(f'{room_window_w}x{room_window_h}+{room_center_x}+{room_center_y}')
        
        edit_room_p.configure(bg = '#c8a4d4')
        edit_room_p.attributes('-topmost', True)
        edit_room_p.attributes('-toolwindow', True)
        edit_room_p.focus_set()
        
        # get the data of the selected row
        data = self.tree.item(selected_room, "values")
        
        # create and place entry fields with data from the selected row
        
        # label and entry room name
        label_room_name = tk.Label(
            edit_room_p,
            text = "Room Name:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_room_name.place(relx = 0.05, rely = 0.05, anchor = "w")
        
        self.room_name_entry_p = tk.Entry(
            edit_room_p,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 15
            )
        self.room_name_entry_p.insert(0, data[1])
        self.room_name_entry_p.place(relx = 0.3, rely = 0.05, anchor = "w")
        
        # label and entry active
        label_active_p = tk.Label(
            edit_room_p,
            text = "Active:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_active_p.place(relx = 0.05, rely = 0.2, anchor = "w")
        
        self.active_room = ToggleButton(
            edit_room_p,
            command=self.toggle_active_p,  
            font=('Footlight MT Light', 11),
            fg='#12043e',
            bg='#dbb6ee',
            width=6
            )
        self.active_room.place(relx = 0.3, rely = 0.2, anchor = "w")
        
        # update the active button based on the value in the selected row
        if data[6] == "1":
           self.active_room.config(text="Yes", relief=tk.SUNKEN)
        else:
           self.active_room.config(text="No", relief=tk.RAISED)
        
        # save button
        save_room_ed = tk.Button(
            edit_room_p, 
            text = "Save", 
            command = lambda: self.save_edit_room(edit_room_p, selected_room),
            font=('Footlight MT Light', 11),
            fg='#12043e',
            bg='#dbb6ee',
            width = 10
            )
        save_room_ed.place(relx = 0.5, rely = 0.57, anchor = "center")
        
        #cancel button
        cancel_room_ed = tk.Button(
            edit_room_p,
            text = "Cancel",
            command = lambda: self.cancel_edit_r(edit_room_p),
            font=('Footlight MT Light', 11),
            fg='#12043e',
            bg='#dbb6ee',
            width = 10
            )
        cancel_room_ed.place(relx = 0.5, rely = 0.75, anchor = "center")
        
        edit_room_p.bind("<Destroy>", lambda event: self.cancel_edit_r(edit_room_p))
        
    # function for the cancel button
    def cancel_edit_r(self, edit_room_p):
        edit_room_p.destroy()
        self.enab_btn_room()  
            
    # function for the save button
    def save_edit_room(self, edit_room_p, selected_room):
        # retrieve the edited data from the entry fields
        active_r = 1 if self.active_room.cget("text") == "Yes" else 0
        
        edited_room = (
            self.tree.item(selected_room, "values")[0], # room id
            self.room_name_entry_p.get(),
            self.tree.item(selected_room, "values")[2], # add date
            self.tree.item(selected_room, "values")[3], # user add id
            self.tree.item(selected_room, "values")[4], # edit date
            self.tree.item(selected_room, "values")[5], # user edit id
            active_r
            )
            
        # retrieve the current data the of the selected row
        current_room_data = self.tree.item(selected_room, "values")
            
        # compare edited data with current data to check for changes
        changed_room = False
        for edited_r, current_r in zip(edited_room, current_room_data):
            edited_r_str = str(edited_r)
            current_r_str = str(current_r)
            
            if edited_r_str != current_r_str:
                changed_room = True
                break
            
        print("Changes Detected:", changed_room)    
        
        if not changed_room:
           ms.showinfo("No Changes", "No changes were made.", parent = edit_room_p)
           edit_room_p.destroy()
           self.enab_btn_room()
           return 
        

           
        # ask for confirmation to save changes
        confirmation = ms.askyesnocancel("Save Changes", "Save changes to this user?", parent = edit_room_p)
        if confirmation:
        # update the database with the edited data
            active = 1 if edited_room[-1] == 1 else 0
            
            edit_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') # current time of the edit
            user_edit_id = None # none until login protocol
                
            params = (
                edited_room[1], # room name
                self.tree.item(selected_room, "values")[2], # add date
                self.tree.item(selected_room, "values")[3], #user add id
                edit_date, # edit date
                user_edit_id, # user edit id
                active, # active
                edited_room[0], # room id
                )
                
            # query to be sent to database
            self.db_manager.execute_query("UPDATE `Room` SET `Room_Name` = %s, `Add_Date` = %s, `User_Add_ID` = %s, `Edit_Date` = %s, `User_Edit_ID` = %s, `Active` = %s WHERE `Room`.`Room_ID` = %s", params)
                
            # data to be inserted into treeview
            edited_room_treeview = (
                edited_room[0], # room id
                edited_room[1], # room name
                self.tree.item(selected_room, "values")[2], # add date
                self.tree.item(selected_room, "values")[3], #user add id
                edit_date, # edit date
                user_edit_id, # user edit id
                active # active
                )
                
            # insertion into treeview
            self.tree.item(selected_room, values = edited_room_treeview)
                
            edit_room_p.destroy()
            self.enab_btn_room()
                
        elif confirmation is None:
            # user clicked "Cancel" in the pop-up, close the edit pop-up
            pass
        else:
            # user clicked "No" in the pop-up, close the edit pop-up
            edit_room_p.destroy()
            self.enab_btn_room()     
    
    # function that removes selected instances from the treeview
    def delete_selected_rooms(self, selected_items=None):
        # if selected_items is None, get a list of selected items in the treeview
        if selected_items is None:
            selected_items = self.tree.selection()

        if not selected_items:
            ms.showerror("Error", "Please select one or more rows to delete.")
            return

        # if delete_all_rooms_flag is True, skip the confirmation pop-up
        if not self.delete_all_rooms_flag:
            # confirm the deletion with the user
            if not ms.askyesno("Confirm Deletion", "Are you sure you want to delete the selected row(s)?"):
                return

        # remove the selected rows from the Treeview
        for item in selected_items:
            room_id = self.tree.item(item, "values")[0]
            self.db_manager.execute_query("DELETE FROM `Room` WHERE `Room`.`Room_ID` = %s", (room_id,))
            self.tree.delete(item)
    
    # function that removes all instances from the table
    def delete_all_rooms(self):
        # set the flag to indicate "Delete all rooms" button was clicked
        self.delete_all_rooms_flag = True

        # confirm the deletion with the user
        if not ms.askyesno("Confirm Deletion", "Are you sure you want to delete all rooms?"):
            # reset the flag if the user cancels the action
            self.delete_all_rooms_flag = False
            return
        
        # execute query to delete all rows from the database
        self.db_manager.execute_query("DELETE FROM `Room`", [])

        # get all items in the treeview and pass them to the delete_selected_rows function
        all_items = self.tree.get_children()
        self.delete_selected_rooms(all_items)

        # reset the flag after the deletion
        self.delete_all_rooms_flag = False        
    
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
