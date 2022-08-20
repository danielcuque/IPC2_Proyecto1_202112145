from .IndexNode import IndexNode


class DoubleLinkedList_Y:
    def __init__(self, size):
        self.next = None
        self.size = size

    def insertColumn(self):
        for i in range(self.size):
            new_index = IndexNode(i, self.size)
            if self.next is None:
                self.next = new_index
            else:
                tmp = self.next
                while tmp.get_next() is not None:
                    tmp = tmp.get_next()
                tmp.set_next(new_index)
                new_index.prev = tmp

    def change_cell_state(self, pos_x, pos_y, isInfected):
        tmp = self.next
        while tmp is not None:
            if tmp.get_index() == pos_y:
                tmp.get_eje_x().change_cell_state(pos_x, isInfected)

    def show_column(self):
        tmp = self.next
        while tmp is not None:
            tmp.show_row()
            tmp = tmp.get_next()
