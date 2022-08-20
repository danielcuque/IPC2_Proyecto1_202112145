from data.pacients.NodePacient import NodePacient


class ListPacients:
    def __init__(self):
        self.head = None
        self.end = None
        self.size = 0

    def insertAtEndPacient(self, name, age):
        new_pacient = NodePacient(name, age)
        self.size += 1

        if self.head is None:
            self.head = new_pacient
            self.end = new_pacient
        else:
            # p1 > None
            tmp = self.head
            while tmp.get_next() is not None:
                tmp = tmp.get_next()
            tmp.set_next(new_pacient)

    def get_size(self):
        return self.size

    def get_head(self):
        return self.head

    def get_end(self):
        return self.end

    def show_pacients(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.name, tmp.age)
            tmp = tmp.next

    # def get_pacient(self, name):
    #     tmp = self.head
    #     while tmp is not None:
    #         if tmp.get_name() == name:
    #             return tmp
    #         tmp = tmp.get_next()
    #     return None

    # def get_pacient_age(self, name):
    #     tmp = self.head
    #     while tmp is not None:
    #         if tmp.get_name() == name:
    #             return tmp.get_age()
    #         tmp = tmp.get_next()
    #     return None
