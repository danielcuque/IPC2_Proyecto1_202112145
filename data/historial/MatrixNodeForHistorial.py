from ..simulation.DoubleLinkedList_Y import DoubleLinkedList_Y


class MatrixNodeForHistorial:
    def __init__(self, matrix):
        self.matrix: DoubleLinkedList_Y = matrix
        self.next = None
        self.prev = None
    
    def get_matrix(self):
        return self.matrix
    
    def get_next(self):
        return self.next
    
    def get_prev(self):
        return self.prev
    
    def set_next(self, next):
        self.next = next
    
    def set_prev(self, prev):
        self.prev = prev
    
    def get_size(self):
        return self.matrix.get_size()
    
    
    
