import copy as copy
import pygame as pg
from typing import List

from common_types import Size2d, Coord, Color


class Ship:
    """
    A ship. Lol
    """

    HOR = 0
    VER = 1

    def __init__(
        self, size: Size2d, position: Coord, cell_size: Size2d, colour: Color
    ) -> None:
        self.size = size
        self.cell_size = cell_size
        self.position = position
        self.colour = colour

        self.surface: pg.Surface = pg.Surface(
            (self.size.x * self.cell_size.x, self.size.y * self.cell_size.y)
        )
        self.hitmap: List[List[bool]] = [
            [False for _ in range(self.cell_size.x)] for _ in range(self.cell_size.y)
        ]

    def hit_tile(self, cell_coord: Coord) -> None:
        self.hitmap[cell_coord.y][cell_coord.x] = True
        return

    def hit_tile_realpos(self, cell_coord: Coord) -> None:
        self.hitmap[cell_coord.y][cell_coord.x] = True
        return

    def is_tile_hit_p(self, cell_coord: Coord) -> bool:
        return self.hitmap[cell_coord.y][cell_coord.x]

    def is_ship_sunk_p(self) -> bool:
        ret: bool = True
        for i in range(self.cell_size.y):
            for j in range(self.cell_size.x):
                ret &= self.hitmap[i][j]

        return ret

    def draw(self) -> None:
        pg.draw.rect(
            self.surface,
            self.colour,
            (
                (0, 0),
                (self.size.x * self.cell_size.x, self.size.y * self.cell_size.y),
            ),
        )

    def get_surface(self) -> pg.Surface:
        return copy.copy(self.surface)
