class Cell:
    def __init__(self, pos_x, pos_y, isInfected):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.isInfected = isInfected

    def get_pos_x(self):
        return self.pos_x

    def get_pos_y(self):
        return self.pos_y

    def get_isInfected(self):
        return self.isInfected

    def set_isInfected(self, isInfected):
        self.isInfected = isInfected

    def set_pos_x(self, pos_x):
        self.pos_x = pos_x

    def set_pos_y(self, pos_y):
        self.pos_y = pos_y
