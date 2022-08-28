from data.base.classes.Patient import Patient
from data.base.classes.Cell import Cell
from data.base.nodes.NodeForDoublyList import NodeForDoublyList
from data.simulation.DoubleLinkedList_Y import DoubleLinkedList_Y


class VerifyMatrix:

    @staticmethod
    def verify_matrix(matrix1: DoubleLinkedList_Y, matrix2: DoubleLinkedList_Y):
        for row in range(matrix1.get_size()):
            for col in range(matrix1.get_size()):
                cell: Cell = matrix1.get_cell_by_row_number(row, col)
                count = matrix1.get_neighbors_cell_state(
                    cell.get_pos_x(), cell.get_pos_y())
                if cell.get_is_infected() == 0:
                    if count == 3:
                        cell: Cell = matrix2.get_cell_by_row_number(row, col)
                        cell.set_is_infected(1)

                if cell.get_is_infected() == 1:
                    if count == 2 or count == 3:
                        cell: Cell = matrix2.get_cell_by_row_number(row, col)
                        cell.set_is_infected(1)

    def found_illnes(self, patient: Patient, matrix_to_verify: DoubleLinkedList_Y):
        period_number = 0
        period_span = 0

        historial_patient = patient.get_historial()

        tmp: NodeForDoublyList = historial_patient.get_head()
        while tmp is not None:
            period_number += 1
            verify = VerifyMatrix().verify_equals_matrix(
                tmp.get_body(), matrix_to_verify)
            if verify:
                period_span = patient.get_historial().get_size() - period_number
                break
            else:
                tmp = tmp.get_next()

        if period_span == 1:
            patient.set_disease_severity("Mortal")
        elif period_span > 1:
            patient.set_disease_severity("Grave")

        patient.set_period_span(period_span)
        patient.set_period_number(period_number)

    @staticmethod
    def verify_equals_matrix(matrix1: DoubleLinkedList_Y, matrix2: DoubleLinkedList_Y):
        for row in range(matrix1.get_size()):
            for col in range(matrix1.get_size()):
                cell_mtx_1: Cell = matrix1.get_cell_by_row_number(row, col)
                cell_mtx_2: Cell = matrix2.get_cell_by_row_number(row, col)
                if cell_mtx_1.get_is_infected() == cell_mtx_2.get_is_infected():
                    continue
                else:
                    return False
        return True

    def create_new_period(self, patient: Patient):
        new_matrix = DoubleLinkedList_Y()
        for pos_x in range(patient.get_size()):
            new_matrix.insert_new_column(pos_x, patient.get_size())

        # Después comparamos la matriz que está a la cabeza del historial con la matriz que acabamos de crear
        self.verify_matrix(patient.get_matrix(), new_matrix)

        # Actualizamos la matriz del paciente con la matriz que acabamos de crear
        new_node = patient.historial.insert_new_period(new_matrix)
        patient.set_matrix(new_node)
        if patient.period_number == 0:
            self.found_illnes(patient, new_matrix)
