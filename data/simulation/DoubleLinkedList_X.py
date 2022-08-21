from .CellNode import CellNode


class DoubleLinkedList_X:
    def __init__(self, size, index):
        self.next = None
        self.size = size
        self.index = index

    def fill_row(self):
        for i in range(self.size):
            new_cell = CellNode(self.index, i, False)
            if self.next is None:
                self.next = new_cell
            else:
                tmp = self.next
                while tmp.get_next() is not None:
                    tmp = tmp.get_next()
                tmp.set_next(new_cell)
                new_cell.prev = tmp

    def change_cell_state(self, pos_x, pos_y, isInfected):
        tmp = self.next
        for i in range(self.size):
            if tmp.get_pos_x_cell() == pos_x:
                tmp.get_pos_y_cell() == pos_y
                tmp.get_isInfected() == isInfected
                tmp = tmp.get_next()

    def show_row(self):
        concatInfoCell = ""
        tmp = self.next
        while tmp is not None:
            concatInfoCell += "(" + str(tmp.get_pos_x_cell()) + " " + str(
                tmp.get_pos_y_cell()) + " " + str(tmp.get_isInfected()) + ") "
            tmp = tmp.get_next()
        print(concatInfoCell)

    def get_next(self):
        return self.next
