from dataclasses import dataclass
import pygame as pg
from typing import Tuple, Protocol


@dataclass
class Coord:
    x: int
    y: int


Size2d = Coord


class GridObject(Protocol):
    surface: pg.Surface
    position: Coord
    size: Size2d

    def draw(self) -> None:
        ...


Color = Tuple[int, int, int]
