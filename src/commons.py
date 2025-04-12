import tkinter as tk

class Commons:

    def __init__(self):

        self.table = []
        
        self.selected_cells = []

        self.cell_names = {}
        self.list_of_alphabet =['A', 'B', 'C', 'D', 'E', 'F',
            'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


    def clear_table(self):
        # Clear all entries in the table
        for cell in self.table:
            try: cell.delete(0, tk.END)
            except: continue
