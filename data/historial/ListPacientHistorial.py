from ..base.lists.SimpleList import SimpleList


class ListPacientHistorial(SimpleList):
    def __init__(self):
        super().__init__()

    def insert_state_at_end(self, matrix):
        self.size += 1

        if self.next is None:
            self.next = matrix
            self.prev = matrix
        else:
            tmp = self.next
            while tmp.get_next() is not None:
                tmp = tmp.get_next()
            tmp.set_next(matrix)
            matrix.set_prev(tmp)
        
