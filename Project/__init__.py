import tkinter as tk
from modules.DatabaseManager import DatabaseManager
from modules.StartPage import StartPage
from modules.LoginPage import LoginPage
from modules.SecondPage import SecondPage
from modules.ThirdPage import ThirdPage
from modules.Privileges import Privileges 
from modules.UserHasPriviliges import UHP
from modules.FourthPage import FourthPage
from modules.FifthPage import FifthPage
from modules.SixthPage import SixthPage
from modules.HumPage import HumPage
from modules.TempPage import TempPage
from modules.CreateSuperUserPage import CreateSuperUserPage
from modules.CreateUserPage import CreateUserPage

# main GUI application window
class OptimalTemperatureSensorApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.db_manager = DatabaseManager("192.168.0.221", "root", "root", "Temperature_Sensor")
        self.db_manager.connect()
        
        self.title('Optimal Temperature Sensor')
        
        main_window_w = 1080
        main_window_h = 720
        
        m_screen_w = self.winfo_screenwidth()
        m_screen_h = self.winfo_screenheight()
        
        m_center_x = int(m_screen_w /2 - main_window_w / 2)
        m_center_y = int(m_screen_h /2 - main_window_h / 2)
        
        self.geometry(f'{main_window_w}x{main_window_h}+{m_center_x}+{m_center_y}')
        
        self.configure(bg='#d398fa')
        
        self.is_access_blocked = False  # attribute to track access restriction
        self.blocked_access_time = 0    # attribute to track the blocked access time
        
        
        container = tk.Frame(self)
        container.pack(side ="top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (StartPage, SecondPage, ThirdPage, FourthPage, FifthPage, SixthPage, TempPage, HumPage, LoginPage, Privileges, UHP, CreateUserPage, CreateSuperUserPage):
            frame = F(container, self, self.db_manager)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(StartPage)  
        
        self.protocol("WM_DELETE_WINDOW", self.exit_application)
        self.bind("<Destroy>", lambda event: self.exit_application)
    
    # function to close the application
    def exit_application(self):
        self.destroy()
        self.db_manager.disconnect()

    # function that displays the frames
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

app = OptimalTemperatureSensorApp()
app.mainloop()

# if __name__ == "__main__":
#     # db_manager = DatabaseManager("192.168.15.4", "root", "root", "Temperature_Sensor")
#     # db_manager.connect()
    