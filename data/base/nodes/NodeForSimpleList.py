class NodeForSimpleList:
    def __init__(self, body):
        self.body = body
        self.next = None
        self.prev = None
    
    def get_body(self):
        return self.body
    
    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev
    
    def set_next(self, next):
        self.next = next
    
    def set_prev(self, prev):
        self.prev = prev
    

