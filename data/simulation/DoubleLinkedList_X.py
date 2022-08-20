from .CellNode import CellNode


class DoubleLinkedList_X:
    def __init__(self, size):
        self.next = None
        self.size = size

    def insertCellAtPosition(self, pos_x_cell, pos_y_cell, isInfected):
        new_cell = CellNode(pos_x_cell, pos_y_cell, isInfected)
        if self.next is None:
            self.next = new_cell
        else:
            tmp = self.next
            while tmp.get_next() is not None:
                tmp = tmp.get_next()
            tmp.set_next(new_cell)
            new_cell.prev = tmp
