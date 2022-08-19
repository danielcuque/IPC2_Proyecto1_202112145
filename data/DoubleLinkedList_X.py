from NodeCell import NodeCell


class DoubleLinkedList_X:
    def __init__(self):
        self.head = None

    def insertCell(self, pos_x, pos_y):
        new_cell = NodeCell(pos_x, pos_y)
        if self.head is None:
            self.head = new_cell
        else:
            tmp = self.head
            while tmp.get_next() is not None:
                tmp = tmp.get_next()
            tmp.set_next(new_cell)
            new_cell.prev = tmp
