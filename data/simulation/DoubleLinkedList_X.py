from ..base.classes.Cell import Cell
from ..base.lists.DoublyList import DoublyList


class DoubleLinkedList_X(DoublyList):
    def __init__(self):
        super().__init__()

    def fill_row(self, pos_x, size):
        for pos_y in range(size):
            new_cell = Cell(pos_x, pos_y, 0)
            self.insert_node_at_end(new_cell)

    def change_cell_state(self, pos_x, pos_y, is_infected):
        tmp = self.next
        for i in range(self.size):
            if tmp.get_body().get_pos_x() == pos_x:
                tmp.get_body().get_is_infected() == is_infected
                tmp = tmp.get_next()

    def show_row(self):
        concatInfoCell = ""
        tmp = self.next
        while tmp is not None:
            concatInfoCell += "(" + str(tmp.get_body().get_pos_x()) + " " + str(
                tmp.get_body().get_pos_y()) + " " + str(tmp.get_body().get_is_infected()) + ") "
            tmp = tmp.get_next()
        print(concatInfoCell)

    def get_next(self):
        return self.next
