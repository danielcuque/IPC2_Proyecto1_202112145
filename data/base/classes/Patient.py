from data.simulation.DoubleLinkedList_Y import DoubleLinkedList_Y
from ...historial.ListPacientHistorial import ListPacientHistorial


class Patient:
    def __init__(self, name, age, size, periods):
        self.name = name
        self.age = age
        self.periods = periods
        self.size = size
        self.matrix = DoubleLinkedList_Y()
        self.historial = ListPacientHistorial()

    def fill_columns(self, size):
        for pos_x in range(self.size):
            self.matrix.insert_new_column(pos_x, size)


    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_size(self):
        return self.matrix.get_size()

    def get_periods(self):
        return self.periods

    def get_matrix(self):
        return self.matrix

    def get_node(self):
        return self.matrix.get_node()

    def get_historial(self):
        return self.historial
