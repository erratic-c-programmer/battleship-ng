from dataclasses import dataclass
import pygame as pg
from typing import Tuple, Protocol


@dataclass
class Coord:
    col: int
    row: int


@dataclass
class Size2d:
    w: int
    h: int


class GridObject(Protocol):
    surface: pg.Surface
    position: Coord
    size: Size2d

    def draw(self) -> None:
        ...


Color = Tuple[int, int, int]
