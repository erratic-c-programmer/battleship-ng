import pygame as pg

class Grid:
    def __init__(self, grid_size, cell_size, line_width, line_colour, fill_colour):
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.line_width = line_width
        self.line_colour = line_colour
        self.fill_colour = fill_colour

        self.total_size = ((grid_size[0] * (cell_size[0] + line_width) + line_width,
                            grid_size[1] * (cell_size[1] + line_width) + line_width))

        self.surf = pg.Surface((self.total_size[0], self.total_size[1]))
        return

    def draw(self):
        self.surf.fill(self.fill_colour)

        for i in range(0, self.total_size[0], self.cell_size[0] + self.line_width):
            pg.draw.line(self.surf, self.line_col, (i, 0), (i, self.total_size[1]), self.line_width)

        for i in range(0, self.total_size[1], self.cell_size[1] + self.line_width):
            pg.draw.line(self.surf, self.line_col, (0, i), (self.total_size[0], i), self.line_width)

        return;
