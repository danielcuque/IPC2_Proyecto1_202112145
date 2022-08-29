# Graphviz libraries:
import graphviz as gv

# Classes
from data.base.classes.Cell import Cell
from data.base.classes.Index import Index
from data.base.classes.Patient import Patient

# Lists
from data.base.nodes.NodeForDoublyList import NodeForDoublyList
from data.simulation.DoubleLinkedList_Y import DoubleLinkedList_Y

# Helpers
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
            self.generate_cells(s, matrix_patient, number_period)

            s.edge(f'root_{number_period}', f'F0_{number_period}')
            s.edge(f'root_{number_period}', f'C0_{number_period}')

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

    def generate_cells(self, graph: gv.Digraph.subgraph, matrix_of_cells: DoubleLinkedList_Y, number_period: int):
        tmp: NodeForDoublyList = matrix_of_cells.get_head()
        while tmp is not None:
            # Get the row with the cells and generate the nodes
            self.generate_cell(graph, tmp.get_body(), number_period)
            tmp = tmp.get_next()

    def generate_cell(self, graph: gv.Digraph.subgraph, index_node: Index, number_period: int):
        index = index_node.get_pos_x()
        matrix_size = index_node.get_eje_x().get_size()
        with graph.subgraph() as s:
            s.attr(rank='same')
            for col in range(matrix_size):
                cell: Cell = index_node.get_cell_by_column_position(col)

                color = '#008af39' if cell.get_is_infected() == 1 else '#f39800'

                s.node(f'F{index}C{col}_{number_period}',
                       label=f'({index},{col})', fillcolor=color)
                if col == 0:
                    s.edge(f'F{index}_{number_period}',
                           f'F{index}C{col}_{number_period}')
                    s.edge(f'F{index}C{col}_{number_period}',
                           f'F{index}C{col+1}_{number_period}')
                if col < matrix_size-1 and col > 0:
                    s.edge(f'F{index}C{col}_{number_period}',
                           f'F{index}C{col+1}_{number_period}')

    def generate_cell_node(self, graph: gv.Digraph.subgraph, cell: Cell, number_period: int, list_size: int):

        with graph.subgraph() as s:
            # s.attr(rank='same')
            # Get the row and col of the cell
            get_pos_x = cell.get_pos_x()
            get_pos_y = cell.get_pos_y()

            # Create a name to display in the graph
            label_position_for_cell = f'({get_pos_x},{get_pos_y})'

            # Create the name of the node with the position of the cell
            position_in_matrix_of_cell = f'C{get_pos_y}F{get_pos_x}_{number_period}'
            color = '#008af39' if cell.get_is_infected() == 1 else '#f39800'

            # Create the node with the position of the cell
            s.node(position_in_matrix_of_cell,
                   label=label_position_for_cell, fillcolor=color)
            # Create the edge with the root of the cell
            s.edge(f'root_{number_period}', position_in_matrix_of_cell)
            # Create the edge with the previous cell
            if get_pos_x > 0:
                previous_cell = f'C{get_pos_y}F{get_pos_x - 1}_{number_period}'
                s.edge(position_in_matrix_of_cell, previous_cell)
