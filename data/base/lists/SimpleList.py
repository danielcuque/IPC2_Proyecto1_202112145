class SimpleList:
    def __init__(self):
        self.next = None
        self.prev = None
        self.size = 0

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
