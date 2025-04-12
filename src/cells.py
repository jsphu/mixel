import tkinter as tk

# CLASS IMPORTS
from src.visuals import Visuals
from src.commons import Commons

class Cells:

    def __init__(self, master):

        self.visual = Visuals(master)
        self.common = Commons()

    def set_default_color(self, color:list=['#F9F9FA', '#343638']):
        if self.common.table:
            self.default_color = self.common.table[-1].cget("fg_color")
        else:
            self.default_color = color

    def get_cell_name(self, event):
        return self.common.cell_names[self.focus_get().grid_info()["in"]]

    def display_cell_name(self, event):
        if (cell_name:=self.get_cell_name(event)):
            self.visual.cell_name_label.configure(text=cell_name)

    def focus_cell(self, cell_name):
        # Focus on the cell with the given name
        for widget, name in self.common.cell_names.items():
            if name == cell_name:
                #print("Focused to", name)
                widget.focus_set()
                widget.select_range(0, tk.END)
                self.visual.cell_name_label.configure(text=cell_name)
                break

    def add_to_selection(self, cell_name):
        for widget, name in self.cell_names.items():
            if name == cell_name and widget not in self.common.selected_cells:
                self.selected_cells.append(widget)
                widget.configure(fg_color="lightblue")  # Highlight the selected cell

    def clear_selection(self):
        for widget in self.common.selected_cells:
            widget.configure(fg_color=self.default_color)  # Reset cell background
        self.common.selected_cells = []

    def cell_parser(self, current):
        cell_char = current[0]
        cell_num = int(current[1:])
        char_index = self.common.list_of_alphabet.index(cell_char)
        return (char_index, cell_char, cell_num)
