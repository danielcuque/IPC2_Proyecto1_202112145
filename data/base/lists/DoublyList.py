from ..nodes.NodeForDoublyList import NodeForDoublyList


class DoublyList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_node_at_end(self, body):
        if self.head is None:
            new_node = NodeForDoublyList(body)
            self.size += 1
            self.head = new_node
            return

        tmp = self.head
        while tmp.next is not None:
            tmp = tmp.next
        new_node = NodeForDoublyList(body)
        self.size += 1
        tmp.next = new_node
        new_node.prev = tmp

    def get_size(self):
        return self.size

    def get_head(self):
        return self.head
