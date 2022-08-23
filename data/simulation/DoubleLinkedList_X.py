from ..base.classes.Cell import Cell
from ..base.lists.DoublyList import DoublyList


class DoubleLinkedList_X(DoublyList):
    def __init__(self):
        super().__init__()

    def fill_row(self, pos_x, size):
        for pos_y in range(size):
            new_cell = Cell(pos_x, pos_y, 0)
            self.insert_node_at_end(new_cell)

    def get_cell_by_column_position(self, pos_y):
        tmp = self.head
        while tmp is not None:
            if tmp.get_body().get_pos_y() == pos_y:
                return tmp.get_body()
            tmp = tmp.get_next()
        return None

    def show_row(self):
        concatInfoCell = ""
        tmp = self.head
        while tmp is not None:
            concatInfoCell += "(" + str(tmp.get_body().get_pos_x()) + " " + str(
                tmp.get_body().get_pos_y()) + " " + str(tmp.get_body().get_is_infected()) + ") "
            tmp = tmp.get_next()
        print(concatInfoCell)
