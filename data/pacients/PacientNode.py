from data.simulation.DoubleLinkedList_Y import DoubleLinkedList_Y


class PacientNode:
    def __init__(self, name, age, size, periods):
        self.name = name
        self.age = age
        self.matrix = DoubleLinkedList_Y(size)
        self.periods = periods
        self.next = None

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_next(self):
        return self.next

    def get_matrix(self):
        return self.matrix

    def set_next(self, next):
        self.next = next

    def get_periods(self):
        return self.periods

    def fill_column(self):
        self.matrix.insertColumn()
