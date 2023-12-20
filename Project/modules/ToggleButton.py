import tkinter as tk

class ToggleButton(tk.Button):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.state = False  # False for "No", True for "Yes"
        self.update_text()

    def toggle(self):
        self.state = not self.state
        self.update_text()

    def update_text(self):
        self.config(text="Yes" if self.state else "No")