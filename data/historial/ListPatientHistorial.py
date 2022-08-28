from data.base.lists.DoublyList import DoublyList


class ListPatientHistorial(DoublyList):
    def __init__(self):
        super().__init__()
        # self.start_node = None

    def insert_in_emptylist(self, matrix):
        if self.head is None:
            # self.start_node = MatrixNodeForHistorial(matrix)
            self.head = self.insert_node_at_end(matrix)
            return

    def insert_new_period(self, matrix):
        return self.insert_node_at_end(matrix)

    def show_list(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.matrix)
            tmp = tmp.next
        print("\n")

    def get_historial_size(self):
        return self.get_size()

    def get_last_node(self):
        return self.tail

    def get_head(self):
        return self.head
