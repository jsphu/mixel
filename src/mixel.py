import tkinter as tk
import customtkinter as ctk

# CLASS IMPORTS
from src.movements import Movements
from src.visuals import Visuals
from src.cells import Cells
from src.commons import Commons

class Mixel(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Mixel")

        self.common = Commons()
        self.movement = Movements(self)
        self.visual = Visuals(self)
        self.cells = Cells(self)
        
        # Create a table of Entry widgets
        self.visual.create_table(rows=20, columns=15)
        self.cells.set_default_color()

        self.bind("<Button-1>", self.cells.display_cell_name)
        self.bind("<Left>", self.key_down_handler)
        self.bind("<Right>", self.key_down_handler)
        self.bind("<Up>", self.key_down_handler)
        self.bind("<Down>", self.key_down_handler)
        self.bind("<Return>", self.key_down_handler)
        
    def run(self):
        self.mainloop()
                    
    def key_down_handler(self, event):
        
        current = self.movement_handler(event) # New cell updated.

        if event.state & 0x0001:
            pass#self.shift_mode(event, current) # fix this..
        else:
            self.clear_selection()
            self.focus_cell(current)
        self.display_cell_name(event)
