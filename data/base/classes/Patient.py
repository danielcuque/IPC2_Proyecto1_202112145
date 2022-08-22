from data.simulation.DoubleLinkedList_Y import DoubleLinkedList_Y


class Patient:
    def __init__(self, name, age, periods, size):
        self.name = name
        self.age = age
        self.periods = periods
        self.matrix = DoubleLinkedList_Y(size)

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


