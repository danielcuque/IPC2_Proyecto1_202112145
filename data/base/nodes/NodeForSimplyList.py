class NodeForSimplyList:
    def __init__(self, body):
        self.body = body
        self.next = None
    
    def get_body(self):
        return self.body
    
    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next
    

