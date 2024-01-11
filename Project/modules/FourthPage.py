import tkinter as tk
from tkinter import messagebox as ms
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import Scrollbar
import datetime
from modules.ToggleButton import ToggleButton
from modules.AdminPasswordWindow import AdminPasswordWindow


class FourthPage(tk.Frame):
    def __init__(self, parent, controller, db_manager):
        from modules.StartPage import StartPage
        tk.Frame.__init__(self, parent)
        self.configure(bg='#d398fa')
        self.db_manager = db_manager
        self.delete_all_sensors_flag = False  # flag to indicate if "Delete all sensors" button was clicked
        
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
        self.tree = ttk.Treeview(tree_frame, columns=("Sensor_ID", "Sensor_Name", "Room_ID", "Add_Date", "User_Add_ID", "Edit_Date", "User_Edit_ID", "Active"), show="headings")
        
        # define the headings of the treeview
        self.tree.heading("Sensor_ID", text="Sensor ID")
        self.tree.heading("Sensor_Name", text="Sensor Name")
        self.tree.heading("Room_ID", text="Room ID")
        self.tree.heading("Add_Date", text="Add date")
        self.tree.heading("User_Add_ID", text="User Add ID")
        self.tree.heading("Edit_Date", text="Edit date")
        self.tree.heading("User_Edit_ID", text="User Edit ID")
        self.tree.heading("Active", text="Active")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # configure tag colors for even and odd rows
        self.tree.tag_configure("tree_color", background = '#bca6e1')
    
        # add some sample data to the Treeview (replace this with data from your database)
        # self.tree.insert("", "end", values=(1, "DHT22_1", 1, "2023-06-26", 1, "2023-06-26", 1, "Yes"),tags=("tree_color",))
        # self.tree.insert("", "end", values=(2, "DHT22_1", 2, "2023-06-26", 2, "2023-07-18", 2, "No"), tags=("tree_color",))
        
        tableS = "Sensor"
        
        # fetch data from the database
        sensors_data = self.db_manager.fetch_table(tableS)

       # populate the Treeview with the fetched data
        for sen_data in sensors_data:
           self.tree.insert("", tk.END, values = sen_data, tags=("tree_color",))
    
        # create vertical scrollbar and link it to the treeview
        v_scroll = Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=v_scroll.set)
        v_scroll.pack(side="right", fill="y")

        # pack the Treeview within tree_frame 
        self.tree.pack(expand=True, fill="both")
    
        # create entries and labels to facilitate the management of the treeview data
        
        # sensor id label and entry
        label_sen_id = tk.Label(
            self,
            text = "Sensor ID:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_sen_id.place(relx = 0.05, rely = 0.6, anchor = "w")
        
        self.sen_id_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.sen_id_entry.place(relx = 0.19, rely = 0.6, anchor = "center")
        
        # sensor name label and entry 
        label_sen_name = tk.Label(
            self,
            text = "Sensor Name:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_sen_name.place(relx = 0.263, rely = 0.6, anchor = "w")
        
        self.sen_name_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.sen_name_entry.place(relx = 0.423, rely = 0.6, anchor = "center")
        
        # room id label and entry
        label_room_id = tk.Label(
            self,
            text = "Room ID:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_room_id.place(relx = 0.4955, rely = 0.6, anchor = "w")
        
        self.room_id_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.room_id_entry.place(relx = 0.627, rely = 0.6, anchor = "center")
        
        # add date label and entry
        label_add_date = tk.Label(
            self,
            text = "Add Date:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_add_date.place(relx = 0.695, rely = 0.6, anchor = "w")
        
        self.add_date_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.add_date_entry.place(relx = 0.829, rely = 0.6, anchor = "center")   
          
        # add user id label and entry
        label_user_add_id = tk.Label(
            self,
            text = "Add User ID:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_user_add_id.place(relx = 0.05, rely = 0.65, anchor = "w")  
        
        self.user_add_id_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.user_add_id_entry.place(relx = 0.208, rely = 0.65, anchor = "center")
        
        # edit date label and entry
        label_edit_date = tk.Label(
            self,
            text = "Edit Date:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_edit_date.place(relx = 0.282, rely = 0.65, anchor = "w")  
        
        self.edit_date_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.edit_date_entry.place(relx=0.4157, rely=0.65, anchor="center")
        
        # edit user id label and entry
        label_user_edit_id = tk.Label(
            self,
            text = "Edit User ID:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_user_edit_id.place(relx = 0.486, rely = 0.65, anchor = "w") 
        
        self.user_edit_id_entry = tk.Entry(
            self,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 12                         
            )
        self.user_edit_id_entry.place(relx=0.643, rely=0.65, anchor="center")
        
        # active label and entry
        label_active = tk.Label(
            self,
            text = "Active:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_active.place(relx = 0.71, rely = 0.65, anchor = "w")
        
        self.active_entry = ToggleButton(
            self,
            command = self.toggle_active, 
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 6)
        self.active_entry.place(relx = 0.81, rely = 0.65, anchor = "center")
    
    
        # bind the Treeview selection event to update the entries with the selected row's data
        self.tree.bind("<<TreeviewSelect>>", self.populate_entries)
    
        # button to add another sensor to the database
        self.AddSensor = tk.Button(
            self,
            text = "Add sensor",
            command = self.add_sensor,
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        self.AddSensor.place(relx = 0.1, rely = 0.85, anchor = "center")
        
        # button that submits the upgraded data of an existing sensor in the treeview
        self.EditSensor = tk.Button(
            self,
            text = "Edit sensor",
            command = self.edit_selected_sensor,
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        self.EditSensor.place(relx = 0.26, rely = 0.85, anchor = "center")
        
        # delete selected rows in the treeview
        self.DeleteSelected = tk.Button(
            self,
            text = "Delete selected",
            command =self.delete_selected_sensors,
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        self.DeleteSelected.place(relx = 0.42, rely = 0.85, anchor = "center")
        
        # delete all rows in the treeview
        self.DeleteAll = tk.Button(
            self,
            text = "Delete all sensors",
            command = self.delete_all_sensors,
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        self.DeleteAll.place(relx = 0.58, rely = 0.85, anchor = "center")
    
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
        
        # back button
        self.BackFor = tk.Button(
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
        self.BackFor.place(relx = 0.9, rely = 0.85, anchor = "center")
        
        # configure the tree_frame to adjust with window resizing
        tree_frame.columnconfigure(0, weight=1)
        tree_frame.rowconfigure(0, weight=1)
        
        # bind the resize callback to the parent window
        self.bind("<Configure>", self.on_window_resize)
    
    # function to toggle the state of the ToggleButton
    def toggle_active(self):
        current_state = self.active_entry.cget("text")
        if current_state == "Yes":
            self.active_entry.config(text="No", relief=tk.RAISED)
        else:
            self.active_entry.config(text="Yes", relief=tk.SUNKEN) 
    
    # function that retrieves data from the entry fields and inserts it into the treeview    
    def add_sensor(self):
        # retrieve data from the entry fields
        sensor_id = None
        sensor_name = self.sen_name_entry.get()
        room_id = self.room_id_entry.get()
        add_date = self.add_date_entry.get()
        user_add = self.user_add_id_entry.get()
        edit_date = None
        user_edit = None
        
        # get the text value of the ToggleButton ("Yes" or "No")
        active_state = self.active_entry.cget("text")
        
        if not sensor_name or not room_id:
            ms.showerror("Error", "Please fill in all the required fields.")
            return
        
        if active_state == "Yes":
            active = 1
        else:
            active = 0
        
        # get the current date and time
        add_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        select_param = (sensor_name, room_id)
        result = self.db_manager.execute_query("SELECT * FROM `Sensor` WHERE `Sensor_Name` = %s AND `Room_ID` = %s", select_param)
        
        if(result):
            ms.showerror("Error", "The data already exists in the database.")
            return
        
        else:
            # pass the values of the parameters to the params list
            params = (sensor_id, sensor_name, room_id, add_date, user_add, edit_date, user_edit, active)
            
            self.db_manager.execute_query("INSERT INTO `Sensor` (`Sensor_ID`, `Sensor_Name`, `Room_ID`, `Add_Date`, `User_Add_ID`, `Edit_Date`, `User_Edit_ID`, `Active`) values (%s, %s, %s, %s, %s, %s, %s, %s)", params)
        
            # insert the data into the table
            self.tree.insert("", "end", values=(sensor_id, sensor_name, room_id, add_date, user_add, edit_date, user_edit, active), tags = ("tree_color",))
        
            # clear the entry fields
            self.clear_entries()
            

    # function that clears the entry fields - accessed throught the clear entries button
    def clear_entries(self):
        # deselect any selected rows in the treeview
        selected_items = self.tree.selection()
        for item in selected_items:
            self.tree.selection_remove(item)
            
        self.sen_id_entry.delete(0, tk.END)
        self.sen_name_entry.delete(0, tk.END)
        self.room_id_entry.delete(0, tk.END)
        self.add_date_entry.delete(0, tk.END)
        self.user_add_id_entry.delete(0, tk.END)
        self.edit_date_entry.delete(0, tk.END)
        self.user_edit_id_entry.delete(0, tk.END)
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
        self.sen_id_entry.delete(0, tk.END)
        self.sen_id_entry.insert(0, data[0])
    
        self.sen_name_entry.delete(0, tk.END)
        self.sen_name_entry.insert(0, data[1])
    
        self.room_id_entry.delete(0, tk.END)
        self.room_id_entry.insert(0, data[2])
    
        self.add_date_entry.delete(0, tk.END)
        self.add_date_entry.insert(0, data[3])
    
        self.user_add_id_entry.delete(0, tk.END)
        self.user_add_id_entry.insert(0, data[4])
    
        self.edit_date_entry.delete(0, tk.END)
        self.edit_date_entry.insert(0, data[5])
    
        self.user_edit_id_entry.delete(0, tk.END)
        self.user_edit_id_entry.insert(0, data[6])
    
        # update the ToggleButton state based on the data
        if data[7] == "Yes":
            self.active_entry.config(text="Yes", relief=tk.SUNKEN)
        else:
            self.active_entry.config(text="No", relief=tk.RAISED)
            
    def edit_selected_sensor(self):
        selected_sensor = self.tree.selection()
        if not selected_sensor:
            ms.showerror("Error", "Please select a row to edit.")    
            return
        self.edit_sensor_popup(selected_sensor[0])
    
    def toggle_active_pop(self):
        current_state = self.active_pop.cget("text")
        if current_state == "Yes":
            self.active_pop.config(text="No", relief=tk.RAISED)
        else:
            self.active_pop.config(text="Yes", relief=tk.SUNKEN)
            
    def disable_btn_sen(self):
        btns_to_dis = [self.AddSensor, self.EditSensor, self.DeleteSelected, self.DeleteAll, self.ClearEntry, self.BackFor, self.sen_id_entry, self.sen_name_entry, self.room_id_entry, self.add_date_entry, self.user_add_id_entry, self.edit_date_entry, self.user_edit_id_entry, self.active_entry]
        for button in btns_to_dis:
            button.config(state=tk.DISABLED)
    
    def enable_btn_sen(self):
        btns_to_en = [self.AddSensor, self.EditSensor, self.DeleteSelected, self.DeleteAll, self.ClearEntry, self.BackFor, self.sen_id_entry, self.sen_name_entry, self.room_id_entry, self.add_date_entry, self.user_add_id_entry, self.edit_date_entry, self.user_edit_id_entry, self.active_entry]
        for button in btns_to_en:
            button.config(state=tk.NORMAL)
        
    # function that updates an existing instance in the table after it was edited using the entries
    def edit_sensor_popup(self, selected_sensor):
        
        # disable the buttons on the sensor management page before creating the pop-up
        self.disable_btn_sen()
            
        edit_pop = tk.Toplevel(self)
        edit_pop.title("Edit Sensor")
        # edit_pop.geometry("550x250")
        
        sen_window_w = 550
        sen_window_h = 250
        sen_screen_w = edit_pop.winfo_screenwidth()
        sen_screen_h = edit_pop.winfo_screenheight()
        
        sen_center_x = int(sen_screen_w /2 - sen_window_w / 2)
        sen_center_y = int(sen_screen_h /2 - sen_window_h / 2)
        
        edit_pop.geometry(f'{sen_window_w}x{sen_window_h}+{sen_center_x}+{sen_center_y}')
        
        edit_pop.configure(bg = '#c8a4d4')
        edit_pop.attributes('-topmost', True)  # bring the window to the top
        edit_pop.attributes('-toolwindow', True)
        edit_pop.focus_set()
        
        # get the data of the selected row
        data = self.tree.item(selected_sensor, "values")
        
        # create and place entry fields with data from the selected row
        
        # label and entry sensor name
        label_sen_name = tk.Label(
            edit_pop,
            text = "Sensor Name:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_sen_name.place(relx = 0.05, rely = 0.05, anchor = "w")
        
        self.sen_name_entry_pop = tk.Entry(
            edit_pop,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 15
            )
        self.sen_name_entry_pop.insert(0, data[1])
        self.sen_name_entry_pop.place(relx = 0.3, rely = 0.05, anchor = "w")
        
        # label and entry room id
        label_room_id = tk.Label(
            edit_pop,
            text = "Room ID:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_room_id.place(relx = 0.05, rely = 0.2, anchor = "w")
        
        self.room_id_pop = tk.Entry(
            edit_pop,
            font = ('Footlight MT Light', 11),
            fg = '#12043e',
            bg = '#dbb6ee',
            width = 15
            )
        self.room_id_pop.insert(0, data[2])
        self.room_id_pop.place(relx = 0.3, rely = 0.2, anchor = "w")
        
        # label and entry active
        label_active = tk.Label(
            edit_pop,
            text = "Active:",
            font = ('Footlight MT Light', 11),
            bg = '#c8a4d4',
            fg = '#12043e'
            )
        label_active.place(relx = 0.05, rely = 0.35, anchor = "w")
        
        self.active_pop = ToggleButton(
            edit_pop,
            command=self.toggle_active_pop,  
            font=('Footlight MT Light', 11),
            fg='#12043e',
            bg='#dbb6ee',
            width=6
            )
        self.active_pop.place(relx = 0.3, rely = 0.35, anchor = "w")
        
        # update the active button based on the value in the selected row
        if data[7] == "1":
            self.active_pop.config(text="Yes", relief=tk.SUNKEN)
        else:
            self.active_pop.config(text="No", relief=tk.RAISED)
            
        # save button
        save_btn = tk.Button(
            edit_pop, 
            text = "Save", 
            command = lambda: self.save_edited_sensor(edit_pop, selected_sensor),
            font=('Footlight MT Light', 11),
            fg='#12043e',
            bg='#dbb6ee',
            width = 10
            )
        save_btn.place(relx = 0.5, rely = 0.7, anchor = "center")
        
        # cancel button
        cancel_btn = tk.Button(
            edit_pop,
            text = "Cancel",
            command = lambda: self.cancel_edit(edit_pop),
            font=('Footlight MT Light', 11),
            fg='#12043e',
            bg='#dbb6ee',
            width = 10
            )
        cancel_btn.place(relx = 0.5, rely = 0.85, anchor = "center")
        
        edit_pop.bind("<Destroy>", lambda event: self.cancel_edit(edit_pop))
        
    # function for the cancel button
    def cancel_edit(self, edit_pop):
        edit_pop.destroy()
        self.enable_btn_sen()
        
    # function for the save button
    def save_edited_sensor(self, edit_pop, selected_sensor):
        # retrieve the edited data from the entry fields
        active_s = 1 if self.active_pop.cget("text") == "Yes" else 0
        
        edited_sen_data = (
            self.tree.item(selected_sensor, "values")[0],   # sensor id
            self.sen_name_entry_pop.get(),
            self.room_id_pop.get(),
            self.tree.item(selected_sensor, "values")[3],   # add date
            self.tree.item(selected_sensor, "values")[4],   # user add id
            self.tree.item(selected_sensor, "values")[5],   # edit date
            self.tree.item(selected_sensor, "values")[6],   # user edit id
            active_s
            )
            
        # retrieve the current data the of the selected row
        current_sen_data = self.tree.item(selected_sensor, "values")
        
        changed_sen = False
        for edited_sen, current_sen in zip(edited_sen_data, current_sen_data):
            edited_sen_str = str(edited_sen)
            current_sen_str = str(current_sen)
            
            if edited_sen_str != current_sen_str:
                changed_sen = True
                break
            
        print("Changes Detected:", changed_sen)   
        
        if not changed_sen:
           ms.showinfo("No Changes", "No changes were made.", parent = edit_pop)
           edit_pop.destroy()
           self.enable_btn_sen()
           return 
           
        # ask for confirmation to save changes
        confirmation = ms.askyesnocancel("Save Changes", "Save changes to this sensor?", parent = edit_pop)
        if confirmation:
            # update the database with the edited data
            active = 1 if edited_sen_data[-1] == 1 else 0
            
            edit_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') # current time of the edit
            user_edit_id = None # none until login protocol
                
            params = (
                edited_sen_data[1], # sensor name
                edited_sen_data[2], #room id
                self.tree.item(selected_sensor, "values")[3], # add date
                self.tree.item(selected_sensor, "values")[4], #user add id
                edit_date, # edit date
                user_edit_id, # user edit id
                active, # active
                edited_sen_data[0], # sensor id
                )
                
            # query to be sent to database
            self.db_manager.execute_query("UPDATE `Sensor` SET `Sensor_Name` = %s, `Room_ID` = %s, `Add_Date` = %s, `User_Add_ID` = %s, `Edit_Date` = %s, `User_Edit_ID` = %s, `Active` = %s WHERE `Sensor`.`Sensor_ID` = %s", params)
                
            # data to be inserted into treeview
            edited_sen_treeview = (
                edited_sen_data[0], # sensor id
                edited_sen_data[1], # sensor name
                edited_sen_data[2], #room id
                self.tree.item(selected_sensor, "values")[3], # add date
                self.tree.item(selected_sensor, "values")[4], #user add id
                edit_date, # edit date
                user_edit_id, # user edit id
                active # active
                )
                
            # insertion into treeview
            self.tree.item(selected_sensor, values = edited_sen_treeview)
                
            edit_pop.destroy()
            self.enable_btn_sen()
                
        elif confirmation is None:
            # user clicked "Cancel" in the pop-up, close the edit pop-up
            pass
        else:
            # user clicked "No" in the pop-up, close the edit pop-up
            edit_pop.destroy()
            self.enable_btn_sen()    
            
            
    # function that removes selected instances from the table
    def delete_selected_sensors(self, selected_items=None):
        # if selected_items is None, get a list of selected items in the treeview
        if selected_items is None:
            selected_items = self.tree.selection()

        if not selected_items:
            ms.showerror("Error", "Please select one or more rows to delete.")
            return

        # if delete_all_sensors_flag is True, skip the confirmation pop-up
        if not self.delete_all_sensors_flag:
            # confirm the deletion with the user
            if not ms.askyesno("Confirm Deletion", "Are you sure you want to delete the selected row(s)?"):
                return
            
        # remove the selected rows from the treeview and database
        for item in selected_items:
            sen_id = self.tree.item(item, "values")[0]
            self.db_manager.execute_query("DELETE FROM `Sensor` WHERE `Sensor`.`Sensor_ID` = %s", (sen_id,))
            self.tree.delete(item)
            
            
    # function that removes all instances from the table
    def delete_all_sensors(self):
        # set the flag to indicate "Delete all sensors" button was clicked
        self.delete_all_sensors_flag = True

        # confirm the deletion with the user
        if not ms.askyesno("Confirm Deletion", "Are you sure you want to delete all sensors?"):
            # reset the flag if the user cancels the action
            self.delete_all_sensors_flag = False
            return
        
        # execute query to delete all rows from the database
        self.db_manager.execute_query("DELETE FROM `Sensor`", [])
        
        # get all items in the Treeview and pass them to the delete_selected_rows function
        all_items = self.tree.get_children()
        self.delete_selected_sensors(all_items)

        # reset the flag after the deletion
        self.delete_all_sensors_flag = False
        
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
