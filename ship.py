import pygame as pg
import copy as copy


class Ship:
    """
    A ship.
    Lol
    """

    HOR = 0
    VER = 1

    def __init__(self, size, cell_size, colour):
        self.size = size
        self.colour = colour
        self.cell_size = cell_size

        self.surf = pg.Surface(
            (self.size[0] * self.cell_size[0], self.size[1] * self.cell_size[1])
        )
        return

    def draw(self):
        pg.draw.rect(
            self.surf,
            self.colour,
            (
                (0, 0),
                (self.size[0] * self.cell_size[0], self.size[1] * self.cell_size[1]),
            ),
        )
        return

    def get_surface(self):
        return copy.copy(self.surf)
