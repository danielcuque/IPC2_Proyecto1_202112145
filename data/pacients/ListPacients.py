from data.pacients.PacientNode import PacientNode


class ListPacients:
    def __init__(self):
        self.next = None
        self.prev = None
        self.size = 0

    def insertPacientAtEnd(self, name, age, size, periods):
        new_pacient = PacientNode(name, age, size, periods)
        self.size += 1

        if self.next is None:
            self.next = new_pacient
            self.prev = new_pacient

        else:
            tmp = self.next
            while tmp.get_next() is not None:
                tmp = tmp.get_next()
            tmp.set_next(new_pacient)
        new_pacient.matrix.fill_column()

    def show_pacients(self):
        tmp = self.next
        while tmp is not None:
            print("Matriz de: " + tmp.get_name())
            tmp.get_matrix().show_matrix()
            tmp = tmp.next

    def get_size(self):
        return self.size

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev
