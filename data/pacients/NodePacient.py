from data.simulation.DoubleLinkedList_Y import DoubleLinkedList_Y


class NodePacient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.matrix = DoubleLinkedList_Y()
