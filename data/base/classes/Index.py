from data.simulation.DoubleLinkedList_X import DoubleLinkedList_X


class Index:
    def __init__(self, index):  # index will be the row number
        self.index = index
        self.list_rows = DoubleLinkedList_X()

    def insert_new_row(self, size):
        self.list_rows.fill_row(self.index, size)

    def get_index_row(self):
        return self.index

    def get_index(self):
        return self.index

    def get_eje_x(self):
        return self.list_rows

    def get_size(self):
        return self.list_rows.size

    def show_row(self):
        self.list_rows.show_row()

    def change_cell_state(self, pos_x, pos_y, is_infected):
        self.list_rows.change_cell_state(pos_x, pos_y, is_infected)
