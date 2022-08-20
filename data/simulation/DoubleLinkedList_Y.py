from data.simulation.DoubleLinkedList_X import DoubleLinkedList_X
from .IndexNode import IndexNode
from .DoubleLinkedList_X import DoubleLinkedList_X


class DoubleLinkedList_Y:
    def __init__(self, size):
        self.next = None
        self.size = size

    def insertColumnAtEnd(self):
        for i in range(self.size):
            new_index = IndexNode(i)
            if self.next is None:
                self.next = new_index
            else:
                tmp = self.next
                while tmp.get_next() is not None:
                    tmp = tmp.get_next()
                tmp.set_next(new_index)
                new_index.prev = tmp

    def insertCell(self, pos_x_cell, pos_y_cell, isInfected):
        tmp = self.next
        
