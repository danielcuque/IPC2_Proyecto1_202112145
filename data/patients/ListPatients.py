from ..base.classes.Patient import Patient
from data.base.lists.SimpleList import SimpleList


class ListPatients(SimpleList):
    def __init__(self):
        super().__init__()

    def insert_patient_at_end(self, name, age, size, periods):
        new_patient = Patient(name, age, size, periods)
        self.insert_node_at_end(new_patient)
        new_patient.fill_columns(size)
        new_patient.get_historial().insert_node_at_end(new_patient.get_matrix())

    def show_patients(self):
        tmp = self.head
        while tmp is not None:
            print("Matriz de: " + tmp.get_body().get_name())
            tmp.get_body().get_matrix().show_matrix()
            tmp = tmp.next

    def get_patient(self, name):
        tmp = self.head
        while tmp is not None:
            if tmp.get_body().get_name() == name:
                return tmp.get_body()
            tmp = tmp.get_next()
        return None
