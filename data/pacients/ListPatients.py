from data.pacients.PacientNode import PacientNode
from data.base.lists.SimpleList import SimpleList


class ListPatients(SimpleList):
    def __init__(self):
        super().__init__()

    def insert_patient_at_end(self, name, age, size, periods):
        new_patient = PacientNode(name, age, size, periods)
        self.size += 1

        if self.next is None:
            self.next = new_patient
            self.prev = new_patient

        else:
            tmp = self.next
            while tmp.get_next() is not None:
                tmp = tmp.get_next()
            tmp.set_next(new_patient)
        new_patient.get_body().matrix.fill_column()

    def show_patients(self):
        tmp = self.next
        while tmp is not None:
            print("Matriz de: " + tmp.get_body().get_name())
            tmp.get_body().get_matrix().show_matrix()
            tmp = tmp.next
