from ..base.lists.SimpleList import SimpleList


class ListPatientHistorial(SimpleList):
    def __init__(self):
        super().__init__()

    def insert_matrix_historial(self, matrix):
        self.insert_node_at_end(matrix)
