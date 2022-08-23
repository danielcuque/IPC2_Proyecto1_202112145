from data.base.lists.DoublyList import DoublyList
from ..base.lists.DoublyList import DoublyList
from ..base.classes.Index import Index


class DoubleLinkedList_Y(DoublyList):
    def __init__(self):
        super().__init__()

    def insert_new_column(self, pos_y, size):
        print("pos_y: " + str(pos_y))
        new_index = Index(pos_y)
        self.insert_node_at_end(new_index)
        new_index.insert_new_row(size)

    def change_cell_state(self, pos_x, pos_y, is_infected):
        tmp = self.next
        while tmp is not None:
            print("size: " + str(self.size))

    def show_matrix(self):
        tmp = self.next
        while tmp is not None:
            tmp.get_body().show_row()
            tmp = tmp.get_next()

    def get_size(self):
        return self.size

    def get_node(self):
        return self.next
