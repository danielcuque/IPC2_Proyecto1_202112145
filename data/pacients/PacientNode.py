from ..base.nodes.NodeForSimpleList import NodeForSimpleList
from ..base.classes.Pacient import Pacient


class PacientNode(NodeForSimpleList):
    def __init__(self, name, age, size, periods):
        super().__init__(Pacient(name, age, size, periods))
