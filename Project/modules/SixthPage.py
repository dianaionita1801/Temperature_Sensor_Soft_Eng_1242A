import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import Scrollbar
from modules.AdminPasswordWindow import AdminPasswordWindow
import asyncio
import websockets
import nest_asyncio
import threading
import asynctkinter as at


nest_asyncio.apply()

class SixthPage(tk.Frame):
    def __init__(self, parent, controller, db_manager):
        from modules.TempPage import TempPage
        from modules.HumPage import HumPage
        from modules.StartPage import StartPage
        tk.Frame.__init__(self, parent)
        self.configure(bg='#d398fa')
        self.db_manager = db_manager
        self.delete_all_rooms_flag = False  # flag to indicate if "Delete all rooms" button was clicked 
        
        # load the image using PhotoImage
        self.image_path = "D:\\Documents\\Facultate\\Software Engineering\\Project\\assets\\background.png"
        self.photo = self.load_and_resize_image(1080, 720)
        
        # create a label to display the image as the background
        self.background_label = tk.Label(self, image = self.photo)
        self.background_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        
       # create a Frame to hold the Treeview and scrollbars
        tree_frame = tk.Frame(self)
        tree_frame.place(relx = 0.5, rely = 0.3, anchor = "center", relwidth = 0.9, relheight = 0.5)
    
        # configure the Treeview Colors
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview.Heading", background = "#bc90d8", foreground = "#1f1135")
        self.style.map("Treeview", background = [("selected", "#8056c7")], foreground = [("selected", "white")])
    
        # create the Treeview widget to display the data in a table
        self.tree = ttk.Treeview(tree_frame, columns = ("Monitoring_ID", "Sensor_ID", "Room_ID", "Temperature_ID", "Humidity_ID", "Date_of_Reading"), show="headings")
        
        # define the headings of the treeview
        self.tree.heading("Monitoring_ID", text = "Monitoring ID")
        self.tree.heading("Sensor_ID", text = "Sensor ID")
        self.tree.heading("Room_ID", text = "Room ID")
        self.tree.heading("Temperature_ID", text = "Temperature ID")
        self.tree.heading("Humidity_ID", text = "Humidity ID")
        self.tree.heading("Date_of_Reading", text = "Date of reading")
        self.tree.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
        
        # configure tag colors for even and odd rows
        self.tree.tag_configure("tree_color", background = '#bca6e1')
    
        self.fill_monitoring()
       
        tableM = "Monitoring" 
       
        # fetch data from the database
        monit_data = self.db_manager.fetch_table(tableM)

        # populate the Treeview with the fetched data
        for mon_data in monit_data:
           self.tree.insert("", tk.END, values=mon_data, tags=("tree_color",))
           
    
        # create vertical scrollbar and link it to the treeview
        v_scroll = Scrollbar(tree_frame, orient = "vertical", command = self.tree.yview)
        self.tree.configure(yscrollcommand = v_scroll.set)
        v_scroll.pack(side = "right", fill = "y")
    
        # pack the Treeview within tree_frame 
        self.tree.pack(expand = True, fill = "both")
        
        # define the headings and associate them with the Treeview columns
        headings = ("Monitoring ID", "Sensor ID", "Room ID", "Temperature ID", "Humidity ID", "Date of reading")
        for i, heading in enumerate(headings):
            self.tree.heading(i, text=heading)
    
        # button to start monitoring
        StartMon = tk.Button(
            self,
            text = "Start",
            command = lambda: threading.Thread(target=asyncio.run, args=(self.start_monitoring(),)).start(),
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        StartMon.place(relx = 0.13, rely = 0.75, anchor = "center")
        
        # button to stop monitoring
        StopMon = tk.Button(
            self,
            text = "Stop",
            command = lambda: threading.Thread(target=asyncio.run, args=(self.stop_monitoring(),)).start(),
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        StopMon.place(relx = 0.315, rely = 0.75, anchor = "center")
        
        # button to access the temperature table
        Temp = tk.Button(
            self,
            text = "Temperature",
            command = lambda: controller.show_frame(TempPage),
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        Temp.place(relx = 0.5, rely = 0.75, anchor = "center")
        
        # button to access the humidity table
        Hum = tk.Button(
            self,
            text = "Humidity",
            command = lambda: controller.show_frame(HumPage),
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 16,
            height = 2,
            anchor = 'center'
        )
        Hum.place(relx = 0.69, rely = 0.75, anchor = "center")
    
        # back button
        BackSix = tk.Button(
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
        BackSix.place(relx = 0.88, rely = 0.75, anchor = "center")
        
        # configure the tree_frame to adjust with window resizing
        tree_frame.columnconfigure(0, weight=1)
        tree_frame.rowconfigure(0, weight=1)        
        
        # bind the resize callback to the parent window
        self.bind("<Configure>", self.on_window_resize)
        
    def run_send_command(self, command):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.send_command(command))
        loop.close()

    async def send_command(self, command):
        uri = "ws://192.168.0.221:8765"
        async with websockets.connect(uri) as websocket:
            await websocket.send(command)

    async def start_monitoring(self):
        await self.send_command("start")

    async def stop_monitoring(self):
        await self.send_command("stop")

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
    
    # calls the admin password window before proceeding further granting restricted access to unauthorized personnel
    def admin_pass_request(self, controller, next_page):
        admin_pass_window = AdminPasswordWindow(controller, next_page)
        admin_pass_window.grab_set()  

    # function to fill the monitoring table
    def fill_monitoring(self):
        tableT = "Temperature"
        tableH = "Humidity"
        
        temp_rec = self.db_manager.fetch_table(tableT)
        hum_rec = self.db_manager.fetch_table(tableH)
        
        for temperature in temp_rec:
            temperature_id, _, sensor_id_t, room_id_t, date_of_reading_t = temperature
            
            for humidity in hum_rec: 
                humidity_id, _, sensor_id_h, room_id_h, date_of_reading_h = humidity
            
                monitoring_id = None
            
                if sensor_id_t == sensor_id_h and room_id_t == room_id_h and date_of_reading_t == date_of_reading_h:
                    
                    result = self.db_manager.execute_query("SELECT * FROM `Monitoring` WHERE `Temperature_ID` = %s AND `Humidity_ID` = %s", (temperature_id, humidity_id))
                
                    # If the result is empty, insert the data into the Monitoring table
                    if not result:
                        param = (monitoring_id, sensor_id_t, room_id_t, temperature_id, humidity_id, date_of_reading_h)
                        self.db_manager.execute_query("INSERT INTO `Monitoring` (`Monitoring_ID`, `Sensor_ID`, `Room_ID`, `Temperature_ID`, `Humidity_ID`, `Date_of_reading`) values (%s, %s, %s, %s, %s, %s)", param)
        
