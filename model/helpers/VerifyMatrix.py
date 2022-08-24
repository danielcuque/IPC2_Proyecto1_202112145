from data.simulation.DoubleLinkedList_Y import DoubleLinkedList_Y
from data.base.classes.Cell import Cell


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

    # def set_infected_cells(self, matrix):
    #     for row in range(self.size):
    #         for col in range(self.size):
    #             cell: Cell = self.get_cell_by_row_number(row, col)
    #             count = self.get_neighbors_cell_state(
    #                 cell.get_pos_x(), cell.get_pos_y())
    #             if cell.get_is_infected() == 0:
    #                 if count == 3:
    #                     cell: Cell = matrix.get_cell_by_row_number(row, col)
    #                     cell.set_is_infected(1)
    #             if cell.get_is_infected() == 1:
    #                 if count == 2 or count == 3:
    #                     cell: Cell = matrix.get_cell_by_row_number(row, col)
    #                     cell.set_is_infected(1)
