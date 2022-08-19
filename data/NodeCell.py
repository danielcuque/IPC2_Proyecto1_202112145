class NodeCell:
    def __init__(self, pos_x_cell, pos_y_cell):
        self.pos_x_cell = pos_x_cell
        self.pos_y_cell = pos_y_cell
        self.next = None
        self.prev = None

    def get_pos_x_cell(self):
        return self.pos_x_cell

    def get_pos_y_cell(self):
        return self.pos_y_cell

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev
