from ..simulation.DoubleLinkedList_Y import DoubleLinkedList_Y


class MatrixNodeForHistorial:
    def __init__(self, matrix):
        self.matrix: DoubleLinkedList_Y = matrix
        self.next = None
        self.prev = None
    
