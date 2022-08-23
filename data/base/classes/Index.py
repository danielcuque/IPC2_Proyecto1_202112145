from data.simulation.DoubleLinkedList_X import DoubleLinkedList_X


class Index:
    def __init__(self, pos_x):  # index will be the row number
        self.pos_x = pos_x
        self.list_rows = DoubleLinkedList_X()

    def insert_new_row(self, size):
        self.list_rows.fill_row(self.pos_x, size)

    def get_pos_x(self):
        return self.pos_x

    def get_eje_x(self):
        return self.list_rows

    def get_size(self):
        return self.list_rows.size

    def show_row(self):
        self.list_rows.show_row()

    def get_cell_by_column_position(self, pos_x):
        return self.list_rows.get_cell_by_column_position(pos_x)
