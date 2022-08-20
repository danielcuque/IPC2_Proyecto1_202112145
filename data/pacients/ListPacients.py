from data.pacients.PacientNode import PacientNode


class ListPacients:
    def __init__(self):
        self.next = None
        self.prev = None
        self.size = 0

    def inserPacientAtEnd(self, name, age):
        new_pacient = PacientNode(name, age)
        self.size += 1

        if self.next is None:
            self.next = new_pacient
            self.prev = new_pacient
        else:
            # p1 > None
            tmp = self.next
            while tmp.get_next() is not None:
                tmp = tmp.get_next()
            tmp.set_next(new_pacient)

    def get_size(self):
        return self.size

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def show_pacients(self):
        tmp = self.next
        while tmp is not None:
            print(tmp.name, tmp.age)
            tmp = tmp.next

    # def get_pacient(self, name):
    #     tmp = self.next
    #     while tmp is not None:
    #         if tmp.get_name() == name:
    #             return tmp
    #         tmp = tmp.get_next()
    #     return None

    # def get_pacient_age(self, name):
    #     tmp = self.next
    #     while tmp is not None:
    #         if tmp.get_name() == name:
    #             return tmp.get_age()
    #         tmp = tmp.get_next()
    #     return None
