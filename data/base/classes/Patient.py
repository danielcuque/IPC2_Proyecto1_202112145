from data.historial.MatrixNodeForHistorial import MatrixNodeForHistorial
from data.simulation.DoubleLinkedList_Y import DoubleLinkedList_Y
from ...historial.ListPatientHistorial import ListPatientHistorial


class Patient:
    def __init__(self, name, age, size, periods):
        self.name = name
        self.age = age
        self.periods = periods
        self.size = size
        self.matrix = MatrixNodeForHistorial(DoubleLinkedList_Y())
        self.historial = ListPatientHistorial()

    def fill_columns(self, size):
        for pos_x in range(self.size):
            self.matrix.get_matrix().insert_new_column(pos_x, size)

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_size(self):
        return self.matrix.get_matrix().get_size()

    def get_periods(self):
        return self.periods

    def get_matrix(self):
        return self.matrix.get_matrix()

    def get_node(self):
        return self.matrix

    def get_historial(self):
        return self.historial

    def get_infected_cells(self):
        return self.matrix.get_matrix().get_cells_infected()

    def get_healthy_cells(self):
        return self.matrix.get_matrix().get_healthy_cells()

    def get_cell_by_row_number(self, pos_x, pos_y):
        return self.matrix.get_matrix().get_cell_by_row_number(pos_x, pos_y)

    def set_periods(self, periods):
        self.periods = periods

    def set_matrix(self, matrix):
        self.matrix = matrix
