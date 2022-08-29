from cProfile import label
import graphviz as gv
from data.base.classes.Cell import Cell
from data.base.classes.Patient import Patient
from data.simulation.DoubleLinkedList_X import DoubleLinkedList_X
from data.simulation.DoubleLinkedList_Y import DoubleLinkedList_Y

from model.simulation.UploadInformation import UploadInformation


class GenerateGraphvizDoc:
    @staticmethod
    def generate_graphviz_doc(path: str):
        patients_list = UploadInformation().patients_list

        tmp = patients_list.get_head()
        while tmp is not None:
            GenerateGraphvizDoc().generate_graph_by_patient(tmp.get_body())
            tmp = tmp.get_next()

    def generate_graph_by_patient(self, patient: Patient):
        # Count to know the number of periods
        count = 0

        # With the historial, create a Digraph
        patient_historial = patient.get_historial()

        # G1 is the main graph, filename is the name of the file to save the graph, format is the format of the graph
        g = gv.Digraph(
            f'G_{patient.get_name()}', filename=f'{patient.get_name()}_simulation')
        # Set the nodes attributes
        g.attr('node', shape='box', style='filled', color='#FFEDBB')

        # Set compound false to avoid the overlap of the subgraphs
        g.attr(compound='true')

        # Set the edges attributes
        g.attr('edge', dir="both")

        # Create the subgraphs for each period
        tmp = patient_historial.get_head()
        while tmp is not None:
            self.generate_subgraph_by_period(
                g, tmp.get_body(), count)
            count += 1
            tmp = tmp.get_next()

        # Joint the subgraphs
        # self.join_subgraphs(g, count)
        # Save the graph
        g.view()

    def generate_subgraph_by_period(self, g: gv.Graph, matrix_patient: DoubleLinkedList_Y, number_period: int):
        with g.subgraph(name=f'cluster_period{number_period}') as s:
            s.attr(style='filled', color='lightgrey',
                   label=f'Periodo {number_period}', fontsize='14')

            self.generate_rows(s, matrix_patient.get_size(), number_period)
            self.generate_cols(s, matrix_patient.get_size(), number_period)

            s.edge(f'root_{number_period}', f'F0_{number_period}')
            s.edge(f'root_{number_period}', f'C0_{number_period}')
            # self.generate_cells(s, matrix_patient, number_period)

    def generate_rows(self, graph: gv.Digraph.subgraph, rows, number_period):
        # with graph
        with graph.subgraph() as s:
            for row in range(rows):
                s.node(f'F{row}_{number_period}', label=f'{row}')
                if row < rows - 1:
                    s.edge(f'F{row}_{number_period}',
                           f'F{row + 1}_{number_period}')

    def generate_cols(self, graph: gv.Digraph.subgraph, cols, number_period):
        with graph.subgraph() as m:
            m.attr(rank='same')
            # Creamos la raiz
            m.node(f"root_{number_period}", label="0,0", group='1')
            for col in range(cols):
                m.node(f'C{col}_{number_period}',
                       label=f'{col}', group=f'{col + 1}')
                if col < cols - 1:
                    m.edge(f'C{col}_{number_period}',
                           f'C{col + 1}_{number_period}')

    def generate_cells(self, graph: gv.Digraph, cells: DoubleLinkedList_Y, number_period: int):
        tmp = cells.get_head()
        while tmp is not None:
            # Agarrae el index node junto con el doubly linked list x
            self.generate_cell(graph, tmp.get_body().list_rows, number_period)
            tmp = tmp.get_next()

    def generate_cell(self, graph: gv.Digraph, cell: DoubleLinkedList_X, number_period: int):
        tmp = cell.get_head()
        while tmp is not None:
            self.generate_cell_node(
                graph, tmp.get_body(), number_period, cell.get_size())
            tmp = tmp.get_next()

    def generate_cell_node(self, graph: gv.Digraph, cell: Cell, number_period: int, list_size: int):
        with graph.subgraph() as s:
            s.attr(rank='same')
            # Get the row and col of the cell
            get_pos_x = cell.get_pos_x()
            get_pos_y = cell.get_pos_y()

            # Create the node with the position of the cell
            row_number_of_matrix = f'F{get_pos_x}_{number_period}'
            label_position_for_cell = f'({get_pos_x},{get_pos_y})'

            # Create the name of the node with the position of the cell
            position_in_matrix_of_cell = f'C{get_pos_y}F{get_pos_x}_{number_period}'
            color = '#008af39' if cell.get_is_infected() == 1 else '#f39800'
            s.node(position_in_matrix_of_cell,
                   label=label_position_for_cell, fillcolor=color)
            if get_pos_y == 0:
                s.node(row_number_of_matrix)
                s.edge(row_number_of_matrix, position_in_matrix_of_cell)
            elif get_pos_y < list_size - 1 and get_pos_y > 0:
                prev_position_in_matrix_of_cell = f'C{get_pos_y}F{get_pos_x - 1}_{number_period}'
                s.node(prev_position_in_matrix_of_cell)
                s.edge(position_in_matrix_of_cell,
                       prev_position_in_matrix_of_cell)
