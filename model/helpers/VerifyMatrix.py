from data.base.classes.Patient import Patient
from data.base.classes.Cell import Cell
from data.historial.MatrixNodeForHistorial import MatrixNodeForHistorial
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
        count = 0
        historial_patient = patient.get_historial()

        tmp: MatrixNodeForHistorial = historial_patient.get_head()
        while tmp is not None:
            verify_tmp = self.verify_equals_matrix(
                tmp.get_body(), matrix_to_verify)
            if verify_tmp is True:
                count += 1

        return count

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
