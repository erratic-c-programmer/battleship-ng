from dataclasses import dataclass
from typing import Tuple


@dataclass
class Coord:
    col: int
    row: int


@dataclass
class Size2d:
    w: int
    h: int


Color = Tuple[int, int, int]
