import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import Scrollbar
import matplotlib.pyplot as plt
import datetime
import random
from modules.TempPage import TempPage
from modules.SixthPage import SixthPage
from modules.StartPage import StartPage

class HumPage(tk.Frame):
    def __init__(self, parent, controller, db_manager):
        tk.Frame.__init__(self, parent)
        self.configure(bg='#d398fa')
        self.db_manager = db_manager
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
        self.tree = ttk.Treeview(tree_frame, columns = ("Humidity_ID", "Humidity_Value", "Sensor_ID", "Room_ID", "Date_of_Reading"), show="headings")
        
        # define the headings of the treeview
        self.tree.heading("Humidity_ID", text = "Humidity_ID")
        self.tree.heading("Humidity_Value", text = "Humidity_Value %")
        self.tree.heading("Sensor_ID", text = "Sensor ID")
        self.tree.heading("Room_ID", text = "Room ID")
        self.tree.heading("Date_of_Reading", text = "Date of reading")
        self.tree.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
        
        # configure tag colors for even and odd rows
        self.tree.tag_configure("tree_color", background = '#bca6e1')
        
        tableH = "Humidity"
        
        # fetch data from the database
        hums_data = self.db_manager.fetch_table(tableH)
        
        # self.update_data()

        # populate the Treeview with the fetched data
        for hum_data in hums_data:
           self.tree.insert("", tk.END, values=hum_data, tags=("tree_color",))
        
    
        # create vertical scrollbar and link it to the treeview
        v_scroll = Scrollbar(tree_frame, orient = "vertical", command = self.tree.yview)
        self.tree.configure(yscrollcommand = v_scroll.set)
        v_scroll.pack(side = "right", fill = "y")

    
        # pack the Treeview within tree_frame 
        self.tree.pack(expand = True, fill = "both")
        
        # define the headings and associate them with the Treeview columns
        headings = ("Humidity_ID", "Humidity_Value %", "Sensor ID", "Room ID", "Date of reading")
        for i, heading in enumerate(headings):
            self.tree.heading(i, text=heading)
              
    
        # button to start monitoring
        StartHum = tk.Button(
            self,
            text = "Start",
            # command = self.add_room,
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 14,
            height = 2,
            anchor = 'center'
        )
        StartHum.place(relx = 0.125, rely = 0.8, anchor = "center")
        
        # button to stop monitoring
        StopHum = tk.Button(
            self,
            text = "Stop",
            # command = self.edit_room,
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 14,
            height = 2,
            anchor = 'center'
        )
        StopHum.place(relx = 0.271, rely = 0.8, anchor = "center")
        
        PltH = tk.Button(
            self,
            text = "Plot",
            command = self.plot_humidity_data,
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 14,
            height = 2,
            anchor = 'center'
        )
        PltH.place(relx = 0.425, rely = 0.8, anchor = "center")
        
        # button to access the humidity table
        Temp = tk.Button(
            self,
            text = "Temperature",
            command = lambda: controller.show_frame(TempPage),
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 14,
            height = 2,
            anchor = 'center'
        )
        Temp.place(relx = 0.575, rely = 0.8, anchor = "center")
    
        # back button
        BackHum = tk.Button(
            self,
            text = "Back",
            command = lambda: controller.show_frame(SixthPage),
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 14,
            height = 2,
            anchor = 'center'
        )
        BackHum.place(relx = 0.725, rely = 0.8, anchor = "center")
        
        # main menu button
        MainMenuH = tk.Button(
            self,
            text = "Main menu",
            command = lambda: controller.show_frame(StartPage),
            font = ('Footlight MT Light', 10, 'bold'),
            fg = '#1f1135',
            bg = '#bc90d8',
            activebackground = '#e5c5f1',
            width = 14,
            height = 2,
            anchor = 'center'
        )
        MainMenuH.place(relx = 0.875, rely = 0.8, anchor = "center")
        
        # configure the tree_frame to adjust with window resizing
        tree_frame.columnconfigure(0, weight=1)
        tree_frame.rowconfigure(0, weight=1)        
        
        # bind the resize callback to the parent window
        self.bind("<Configure>", self.on_window_resize)   
        
    # def update_data(self):
    #     # Fetch the updated data from the database
    #     hums_data = self.db_manager.fetch_hum()
    
    #     # Create a set to store the IDs of new humidity records
    #     new_ids = set()
    
    #     # Iterate through the existing humidity records and check if they are still in the database
    #     for index in self.tree.get_children():
    #         humidity_id = self.tree.item(index, "values")[0]
    #         new_ids.add(humidity_id)
    
    #     # Insert the new humidity records into the Treeview
    #     for humidity_data in hums_data:
    #         if humidity_data[0] in new_ids:
    #             self.tree.insert("", tk.END, values=humidity_data, tags=("tree_color",))
    
    #     # Schedule the next update after 200 milliseconds (1/5 second)
    #     self.after(200, self.update_data)

        
    def plot_humidity_data(self):
        # Get the humidity values and sensor IDs from the Treeview
        humidity_values = [float(self.tree.item(item, 'values')[1]) for item in self.tree.get_children()]
        sensor_ids = [int(self.tree.item(item, 'values')[2]) for item in self.tree.get_children()]
        
        # Get the corresponding date and time for each humidity value (assuming it's in the last column)
        date_time_values = [self.tree.item(item, 'values')[-1] for item in self.tree.get_children()]
        
        # Convert the date and time strings to datetime objects (you may need to adjust the format)
        date_time_objects = [datetime.datetime.strptime(dt_str , '%Y-%m-%d %H:%M:%S') for dt_str in date_time_values]

        # Group humidity values and date-time objects by sensor ID
        data_by_sensor = {}
        for sensor_id, humidity_value, dt_object in zip(sensor_ids, humidity_values, date_time_objects):
            if sensor_id not in data_by_sensor:
                data_by_sensor[sensor_id] = {"humidity_values": [], "date_time_objects": []}
            data_by_sensor[sensor_id]["humidity_values"].append(humidity_value)
            data_by_sensor[sensor_id]["date_time_objects"].append(dt_object)

        # Create the plot
        plt.figure(figsize=(8, 6))

        # Plot data for each sensor with different colors
        for sensor_id, data in data_by_sensor.items():
            color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            plt.plot(data["date_time_objects"], data["humidity_values"], marker='o', linestyle='-', label=f"Sensor {sensor_id}", color=color)

        plt.xlabel('Date and Time')
        plt.ylabel('Humidity (%)')
        plt.title('Humidity Measurement Progress')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.legend()

        # Show the plot
        plt.tight_layout()
        plt.show()    


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
