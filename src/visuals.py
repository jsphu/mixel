import tkinter as tk
import customtkinter as ctk

# Imports
from src.commons import Commons

class Visuals:

    def __init__(self, master):

        self.common = Commons()

        self.tops = ctk.CTkFrame(master)
        self.tops.pack(pady=20, padx=10, expand=True)
        # Create a frame for the table
        self.frame = ctk.CTkFrame(master)
        self.frame.pack(pady=10, padx=10, fill="both", expand=True)

        self.cell_name_label = ctk.CTkLabel(self.tops, text="CELL NAME")
        self.cell_name_label.pack(pady=10)

        # Create a button to calculate the sum of the first column
        self.clear_button = ctk.CTkButton(self.tops, text="Clear", command=self.common.clear_table)
        self.clear_button.pack(pady=10)
        

    
    """ DEPRECATED
    def create_table(self, rows, columns):
        self.table = [
            ctk.CTkLabel(self.frame, text=char).grid(
                row=0, column=index+1, padx=1, pady=1) 
            for index, char in enumerate(self.list_of_alphabet[:columns])
        ]
        for i in range(1,rows+1):
            row = [ctk.CTkLabel(self.frame, text=str(i)).grid(
                row=i, column=0, padx=5, pady=1)
            ]
            for j in range(1,columns+1):
                entry = ctk.CTkEntry(self.frame, width=100)
                entry.grid(row=i, column=j, padx=1, pady=1)
                row.append(entry)
                self.cell_names[entry] = f"{self.list_of_alphabet[j-1]}{i}"
            self.table.append(row)
    """


    def create_table(self, rows, columns):
        # Total cells include headers: (rows + 1) x (columns + 1)
        total_cells = (rows + 1) * (columns + 1)

        self.common.table = []

        for i in range(total_cells):
            row = i // (columns + 1)  # Calculate row index
            col = i % (columns + 1)  # Calculate column index

            if row == 0 and col == 0:
                # Top-left corner cell (empty)
                continue
            elif row == 0:
                # Column headers
                self.common.table.append(ctk.CTkLabel(self.frame, text=self.common.list_of_alphabet[col - 1]))
                self.common.table[-1].grid(row=row, column=col, padx=1, pady=1)
            elif col == 0:
                # Row headers
                self.common.table.append(ctk.CTkLabel(self.frame, text=str(row)))
                self.common.table[-1].grid(row=row, column=col, padx=5, pady=1)
            else:
                # Cell entries
                self.common.table.append(entry:=ctk.CTkEntry(self.frame, width=100))
                entry.grid(row=row, column=col, padx=1, pady=1)
                self.common.cell_names[entry] = f"{self.common.list_of_alphabet[col - 1]}{row}"