class DoublyList:
    def __init__(self):
        self.next = None
        self.size = 0

    def get_size(self):
        return self.size

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next
