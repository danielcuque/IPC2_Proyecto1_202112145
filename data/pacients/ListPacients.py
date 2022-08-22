from data.pacients.PacientNode import PacientNode
from data.base.lists.SimpleList import SimpleList


class ListPacients(SimpleList):
    def __init__(self):
        super().__init__()

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
        new_pacient.get_body().matrix.fill_column()

    def show_pacients(self):
        tmp = self.next
        while tmp is not None:
            print("Matriz de: " + tmp.get_body().get_name())
            tmp.get_body().get_matrix().show_matrix()
            tmp = tmp.next
