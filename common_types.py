from dataclasses import dataclass


@dataclass
class Coord:
    col: int
    row: int


@dataclass
class Size2d:
    w: int
    h: int
