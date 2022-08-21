from .DoubleLinkedList_X import DoubleLinkedList_X


class IndexNode:
    def __init__(self, index, size):
        self.index = index
        self.eje_x = DoubleLinkedList_X(size, index)
        self.next = None
        self.prev = None

    def fill_row(self):
        self.eje_x.fill_row()

    def get_index(self):
        return self.index

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_next(self, next):
        self.next = next

    def set_prev(self, prev):
        self.prev = prev

    def get_eje_x(self):
        return self.eje_x

    def show_row(self):
        self.eje_x.show_row()
