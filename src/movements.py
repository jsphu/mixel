# CLASS IMPORTS
from src.commons import Commons
from src.cells import Cells

class Movements:
    
    def __init__(self, master):

        self.common = Commons()
        self.cells = Cells(master)

    def move_down(self, current):
        _, cell_char, cell_num = self.cells.cell_parser(current)
        return f"{cell_char}{cell_num + 1}"  
    def move_up(self, current):
        _, cell_char, cell_num = self.cells.cell_parser(current)
        return f"{cell_char}{cell_num - 1}"
    def move_right(self, current):
        index, _, cell_num = self.cells.cell_parser(current)
        if index < len(self.list_of_alphabet) - 1:
            return f"{self.list_of_alphabet[index + 1]}{cell_num}"
    def move_left(self,current):
        index, _, cell_num = self.cells.cell_parser(current)
        if index > 0:
            return f"{self.list_of_alphabet[index - 1]}{cell_num}"

    def movement_handler(self, event):
        # Move focus based on arrow key input
        if not (current := self.cells.get_cell_name(event)): return
        if event.keysym == "Down" or event.keysym == "Return": return self.move_down(current)
        elif event.keysym == "Up": return self.move_up(current)
        elif event.keysym == "Left": return self.move_left(current)
        elif event.keysym == "Right": return self.move_right(current)

    """ fix this...

    def shift_mode(self, event, current):

        while event.state & 0x0001: # While shift key is hold
            *_, cell_num = self.cell_parser(current)
            if cell_num > 0 and cell_num <= len(self.table) - 1:
                try:
                    current_new = self.movement_handler(event)
                    if current != current_new:
                        self.add_to_selection(current_new)
                    else:
                        break
                except KeyError:
                    pass
    """