import tkinter as tk
import customtkinter as ctk

class Excel(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Mini Excel")

        self.tops = ctk.CTkFrame(self)
        self.tops.pack(pady=20, padx=10, expand=True)
        # Create a frame for the table
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=10, padx=10, fill="both", expand=True)

        self.cell_name_label = ctk.CTkLabel(self.tops, text="CELL NAME")
        self.cell_name_label.pack(pady=10)

        # Create a button to calculate the sum of the first column
        self.clear_button = ctk.CTkButton(self.tops, text="Clear", command=self.clear_table)
        self.clear_button.pack(pady=10)

        self.selected_cells = []

        self.cell_names = {}
        self.list_of_alphabet =['A', 'B', 'C', 'D', 'E', 'F',
            'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        # Create a table of Entry widgets
        self.create_table(rows=20, columns=15)

        self.default_color = self.table[-1].cget("fg_color")

        self.bind("<Button-1>", self.display_cell_name)
        self.bind("<Left>", self.key_down_handler)
        self.bind("<Right>", self.key_down_handler)
        self.bind("<Up>", self.key_down_handler)
        self.bind("<Down>", self.key_down_handler)
        self.bind("<Return>", self.key_down_handler)
        
    """
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
        self.table=[]

        for i in range(total_cells):
            row = i // (columns + 1)  # Calculate row index
            col = i % (columns + 1)  # Calculate column index

            if row == 0 and col == 0:
                # Top-left corner cell (empty)
                continue
            elif row == 0:
                # Column headers
                self.table.append(ctk.CTkLabel(self.frame, text=self.list_of_alphabet[col - 1]))
                self.table[-1].grid(row=row, column=col, padx=1, pady=1)
            elif col == 0:
                # Row headers
                self.table.append(ctk.CTkLabel(self.frame, text=str(row)))
                self.table[-1].grid(row=row, column=col, padx=5, pady=1)
            else:
                # Cell entries
                self.table.append(entry:=ctk.CTkEntry(self.frame, width=100))
                entry.grid(row=row, column=col, padx=1, pady=1)
                self.cell_names[entry] = f"{self.list_of_alphabet[col - 1]}{row}"


    def clear_table(self):
        # Clear all entries in the table
        for cell in self.table:
            try: cell.delete(0, tk.END)
            except: continue

    def get_cell_name(self, event):
        return self.cell_names[self.focus_get().grid_info()["in"]]

    def display_cell_name(self, event):
        if (cell_name:=self.get_cell_name(event)):
            self.cell_name_label.configure(text=cell_name)

    def focus_cell(self, cell_name):
        # Focus on the cell with the given name
        for widget, name in self.cell_names.items():
            if name == cell_name:
                #print("Focused to", name)
                widget.focus_set()
                widget.select_range(0, tk.END)
                self.cell_name_label.configure(text=cell_name)
                break

    def add_to_selection(self, cell_name):
        for widget, name in self.cell_names.items():
            if name == cell_name and widget not in self.selected_cells:
                self.selected_cells.append(widget)
                widget.configure(fg_color="lightblue")  # Highlight the selected cell

    def clear_selection(self):
        for widget in self.selected_cells:
            widget.configure(fg_color=self.default_color)  # Reset cell background
        self.selected_cells = []

    def key_down_handler(self, event):
        # Move focus based on arrow key input
        current = self.get_cell_name(event)
        if not current:
            return

        cell_char = current[0]
        cell_num = int(current[1:])
        index = self.list_of_alphabet.index(cell_char)

        if event.keysym == "Down" or event.keysym == "Return":
            cell_char = self.list_of_alphabet[index]  # Stay in the same column
            cell_num += 1
        elif event.keysym == "Up":
            cell_char = self.list_of_alphabet[index]
            cell_num -= 1
        elif event.keysym == "Left":
            if index > 0:
                cell_char = self.list_of_alphabet[index - 1]
        elif event.keysym == "Right":
            if index < len(self.list_of_alphabet) - 1:
                cell_char = self.list_of_alphabet[index + 1]

        # Ensure the new cell is within bounds
        if cell_num > 0 and cell_num <= len(self.table) - 1:
            try:
                new_cell_name = f"{cell_char}{cell_num}"
                if event.state & 0x0001:  # Check if Shift key is pressed
                    self.add_to_selection(new_cell_name)
                else:
                    self.clear_selection()
                    self.focus_cell(new_cell_name)
            except KeyError:
                pass
        self.display_cell_name(event)



if __name__ == "__main__":
    app = Excel()
    app.mainloop()
