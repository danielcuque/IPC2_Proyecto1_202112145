from ..base.nodes.NodeForSimpleList import NodeForSimpleList
from ..base.classes.Patient import Patient


class PacientNode(NodeForSimpleList):
    def __init__(self, name, age, size, periods):
        super().__init__(Patient(name, age, size, periods))
