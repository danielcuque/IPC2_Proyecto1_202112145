class Cell:
    def __init__(self, pos_x, pos_y, is_infected):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.is_infected = is_infected

    def get_pos_x(self):
        return self.pos_x

    def get_pos_y(self):
        return self.pos_y

    def get_is_infected(self):
        return self.is_infected

    def set_is_infected(self, is_infected):
        self.is_infected = is_infected

    def set_pos_x(self, pos_x):
        self.pos_x = pos_x

    def set_pos_y(self, pos_y):
        self.pos_y = pos_y
