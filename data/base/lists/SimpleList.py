from ..nodes.NodeForSimpleList import NodeForSimpleList


class SimpleList:
    def __init__(self):
        self.next = None
        self.prev = None
        self.size = 0

    def insert_node_at_end(self, body):
        new_node = NodeForSimpleList(body)
        if self.next is None:
            self.next = new_node
            self.prev = new_node
        else:
            tmp = self.next
            while tmp.get_next() is not None:
                tmp = tmp.get_next()
            tmp.set_next(new_node)
            new_node.set_prev(tmp)
        self.size += 1

    def get_size(self):
        return self.size

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_next(self, next):
        self.next = next

    def set_prev(self, prev):
        self.prev = prev
