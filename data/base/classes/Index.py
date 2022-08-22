from data.simulation.DoubleLinkedList_X import DoubleLinkedList_X


class Index:
    def __init__(self, index, size):
        self.index = index
        self.eje_x = DoubleLinkedList_X(size, index)
        self.fill_row()

    def fill_row(self):
        self.eje_x.fill_row()

    def get_index(self):
        return self.index

    def get_eje_x(self):
        return self.eje_x

    def get_size(self):
        return self.eje_x.size

    def show_row(self):
        self.eje_x.show_row()

