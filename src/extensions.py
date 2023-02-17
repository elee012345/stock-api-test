class Graph():
    def __init__(self, vert_scaling, horizontal_scaling, vert_offset=0, horizontal_offset=0):
        self.VERT_SCALING = vert_scaling
        self.HORIZONTAL_SCALING = horizontal_scaling
        self.vert_offset = vert_offset
        self.horizontal_offset = horizontal_offset

    def set_display(self, display):
        self.display = display

    def get_y(self, y):
        return (self.display.Info().current_h - self.vert_offset) - (y * self.VERT_SCALING)

    def get_x(self, x):
        return (x * self.HORIZONTAL_SCALING) + self.horizontal_offset

    def get_coords(self, x, y):
        return (self.get_x(x), self.get_y(y))
