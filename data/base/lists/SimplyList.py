from ..nodes.NodeForSimplyList import NodeForSimplyList


class SimplyList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_node_at_end(self, body):
        new_node = NodeForSimplyList(body)
        self.size = + 1
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            tmp = self.head
            while tmp.get_next() is not None:
                tmp = tmp.get_next()
            tmp.set_next(new_node)

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def get_size(self):
        return self.size

    def set_head(self, head):
        self.head = head

    def set_tail(self, tail):
        self.tail = tail
