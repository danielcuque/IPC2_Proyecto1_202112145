

class ListPacientHistorial():
    def __init__(self, pacient):
        self.pacient = pacient
        self.next = None

    def get_pacient(self):
        return self.pacient

    def save_state_matrix(self, matrix):
        if self.next is None:
            self.next = matrix
        else:
            tmp = self.next

