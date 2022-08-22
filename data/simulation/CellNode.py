from ..base.classes.Cell import Cell
from ..base.nodes.NodeForDoublyList import NodeForDoublyList


class CellNode(NodeForDoublyList):
    def __init__(self, pos_x, pos_y, isInfected):
        super().__init__(Cell(pos_x, pos_y, isInfected))
