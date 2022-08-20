from data.simulation.DoubleLinkedList_Y import DoubleLinkedList_Y


class NodePacient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.matrix = DoubleLinkedList_Y()
        self.next = None
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    # def get_matrix(self):
    #     return self.matrix
    
    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next
    
    # def set_matrix(self, matrix):
    #     self.matrix = matrix

