# Classes
from data.base.classes.Cell import Cell
from ..base.classes.Index import Index

# Lists and Nodes
from ..base.lists.DoublyList import DoublyList


from ..base.nodes.NodeForDoublyList import NodeForDoublyList


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

    def get_cells_infected(self):
        cells_infected = 0
        for row in range(self.size):
            for col in range(self.size):
                cell: Cell = self.get_cell_by_row_number(row, col)
                if cell.get_is_infected() == 1:
                    cells_infected += 1
        return cells_infected

    def get_healthy_cells(self):
        total_cells = self.size * self.size
        return total_cells - self.get_cells_infected()

    def get_neighbors_cell_state(self, pos_x, pos_y):
        count = 0
        for i in range(pos_x - 1, pos_x + 2):
            for j in range(pos_y - 1, pos_y + 2):
                if i == pos_x and j == pos_y:
                    continue
                else:
                    cell: Cell = self.get_cell_by_row_number(i, j)
                    if cell is not None:
                        if cell.get_is_infected() == 1:
                            count += 1
        return count

    def show_matrix(self):
        tmp = self.head
        while tmp is not None:
            tmp.get_body().show_row()
            tmp = tmp.get_next()

    def get_size(self):
        return self.size

    def get_node(self):
        return self.next
