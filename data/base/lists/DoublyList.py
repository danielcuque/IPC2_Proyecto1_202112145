from ..nodes.NodeForDoublyList import NodeForDoublyList


class DoublyList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_node_at_end(self, body):
        new_node = NodeForDoublyList(body)
        if self.head is None:
            self.head = new_node
        else:
            tmp = self.head
            while tmp.get_next() is not None:
                tmp = tmp.get_next()
            tmp.set_next(new_node)
            new_node.set_prev(tmp)
        self.size += 1

    def get_size(self):
        return self.size

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next
