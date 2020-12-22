import copy as copy
import pygame as pg
from typing import Tuple

from common_types import *


class Ship:
    """
    A ship.
    Lol
    """

    HOR = 0
    VER = 1

    def __init__(self, size: Size2d, cell_size: Size2d, colour: Tuple[int, int, int]):
        self.size = size
        self.colour = colour
        self.cell_size = cell_size

        self.surf = pg.Surface(
            (self.size.w * self.cell_size.w, self.size.h * self.cell_size.h)
        )
        return

    def draw(self):
        pg.draw.rect(
            self.surf,
            self.colour,
            (
                (0, 0),
                (self.size.w * self.cell_size.w, self.size.h * self.cell_size.h),
            ),
        )
        return

    def get_surface(self):
        return copy.copy(self.surf)
