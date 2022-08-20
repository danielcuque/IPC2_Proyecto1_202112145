class CellNode:
    def __init__(self, pos_x_cell, pos_y_cell, isInfected):
        self.pos_x_cell = pos_x_cell
        self.pos_y_cell = pos_y_cell
        self.isInfected = isInfected
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

    def set_next(self, next):
        self.next = next

    def set_prev(self, prev):
        self.prev = prev

    def get_isInfected(self):
        return self.isInfected
