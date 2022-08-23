from data.base.classes.Cell import Cell
from data.base.lists.DoublyList import DoublyList
from data.base.nodes.NodeForDoublyList import NodeForDoublyList
from ..base.lists.DoublyList import DoublyList
from ..base.classes.Index import Index


class DoubleLinkedList_Y(DoublyList):
    def __init__(self):
        super().__init__()

    def insert_new_column(self, pos_x, size):
        new_index = Index(pos_x)
        self.insert_node_at_end(new_index)
        new_index.insert_new_row(size)

    def change_cell_state(self, pos_x, pos_y, is_infected):
        cell: Cell = self.get_cell_by_row_number(pos_x, pos_y)
        if cell is not None:
            cell.set_is_infected(is_infected)

    def get_cell_by_row_number(self, pos_x, pos_y):
        tmp: NodeForDoublyList = self.head
        while tmp is not None:
            if tmp.get_body().get_pos_x() == pos_x:
                return tmp.get_body().get_cell_by_column_position(pos_y)
            tmp = tmp.get_next()
        return None

    def show_matrix(self):
        tmp = self.head
        while tmp is not None:
            tmp.get_body().show_row()
            tmp = tmp.get_next()

    def get_size(self):
        return self.size

    def get_node(self):
        return self.next
