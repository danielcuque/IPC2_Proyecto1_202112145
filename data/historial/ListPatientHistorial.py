from data.historial.MatrixNodeForHistorial import MatrixNodeForHistorial


class ListPatientHistorial:
    def __init__(self):
        self.start_node = None

    def insert_in_emptylist(self, matrix):
        if self.start_node is None:
            self.start_node = MatrixNodeForHistorial(matrix)
            return

    def insert_node_at_end(self, matrix):
        if self.start_node is None:
            new_node = MatrixNodeForHistorial(matrix)
            self.start_node = new_node
            return
        tmp = self.start_node
        while tmp.next is not None:
            tmp = tmp.next
        new_node = MatrixNodeForHistorial(matrix)
        tmp.next = new_node
        new_node.prev = tmp

    def show_list(self):
        tmp = self.start_node
        while tmp is not None:
            print(tmp.matrix.show_matrix())
            print("\n")
            tmp = tmp.next
