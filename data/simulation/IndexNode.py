from ..base.classes.Index import Index
from ..base.nodes.NodeForDoublyList import NodeForDoublyList


class IndexNode(NodeForDoublyList):
    def __init__(self, index, size):
        super().__init__(Index(index, size))

