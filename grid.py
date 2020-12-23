from typing import List
import copy
import pygame as pg
from common_types import Coord, Size2d, Color, GridObject


class Grid:
    def __init__(
        self,
        grid_size: Size2d,
        cell_size: Size2d,
        line_width: int,
        line_colour: Color,
        fill_colour: Color,
    ) -> None:
        self.grid_size: Size2d = grid_size
        self.cell_size: Size2d = cell_size
        self.line_width: int = line_width
        self.line_colour: Color = line_colour
        self.fill_colour: Color = fill_colour

        self.objcnt: int = (
            0  # No. of objects in the grid, also acts as ID==index for next obj
        )

        self.total_size: Size2d = Size2d(
            self.grid_size.w * (self.cell_size.w + self.line_width) + self.line_width,
            self.grid_size.h * (self.cell_size.h + self.line_width) + self.line_width,
        )

        self.objects: List[GridObject] = []
        self.cell_objs_map: List[List[List[int]]] = []
        for i in range(grid_size.h):
            self.cell_objs_map.append([])
            for _ in range(grid_size.w):
                self.cell_objs_map[i].append([])

        self.surf = pg.Surface((self.total_size.w, self.total_size.h))
        return

    def cell2surf(self, cell_coord: Coord) -> Coord:
        """
        Converts cell coordinates to surface coordinates
        """
        ret: Coord = Coord(
            (self.line_width + cell_coord.row * (self.cell_size.h + self.line_width)),
            (self.line_width + cell_coord.col * (self.cell_size.w + self.line_width)),
        )
        return ret

    def surf2cell(self, surf_coord: Coord) -> Coord:
        """
        Converts real coordinates to cell coordinates
        """

        return Coord(
            surf_coord.col // self.cell_size.h,
            surf_coord.row // self.cell_size.w,
        )

    def add_obj(self, obj: GridObject) -> None:
        self.objects.append(obj)
        for i in range(obj.position.row, obj.position.row + obj.size.h):
            for j in range(obj.position.col, obj.position.col + obj.size.w):
                self.cell_objs_map[i][j].append(self.objcnt)
        self.objcnt += 1
        return

    def move_obj(self, obj_id: int, new_cell_coord: Coord) -> None:
        self.objects[obj_id].position = self.cell2surf(new_cell_coord)
        return

    def rearrange_obj_up(self, obj_id: int, cell_coord: Coord) -> None:
        if obj_id in self.cell_objs_map[cell_coord.row][cell_coord.col]:
            try:
                i1: int = self.cell_objs_map[cell_coord.row][cell_coord.col].index(
                    obj_id
                )
                i2: int = self.cell_objs_map[cell_coord.row][cell_coord.col].index(
                    obj_id + 1
                )
                self.objects[i1], self.objects[i2] = self.objects[i2], self.objects[i1]
            except IndexError:
                pass

        return

    def rearrange_obj_down(self, obj_id: int, cell_coord: Coord) -> None:
        if obj_id in self.cell_objs_map[cell_coord.row][cell_coord.col]:
            try:
                i1: int = self.cell_objs_map[cell_coord.row][cell_coord.col].index(
                    obj_id
                )
                i2: int = self.cell_objs_map[cell_coord.row][cell_coord.col].index(
                    obj_id - 1
                )
                self.objects[i1], self.objects[i2] = self.objects[i2], self.objects[i1]
            except IndexError:
                pass

        return

    def draw(self) -> None:
        self.surf.fill(self.fill_colour)

        for s in self.objects:
            s.draw()
            self.surf.blit(
                s.surface,
                (self.cell2surf(s.position).col, self.cell2surf(s.position).row),
            )

        for i in range(0, self.total_size.w, self.cell_size.w + self.line_width):
            pg.draw.line(
                self.surf,
                self.line_colour,
                (i, 0),
                (i, self.total_size.h),
                self.line_width,
            )

        for i in range(0, self.total_size.h, self.cell_size.h + self.line_width):
            pg.draw.line(
                self.surf,
                self.line_colour,
                (0, i),
                (self.total_size.w, i),
                self.line_width,
            )

    def get_cell_obj(self, cell_coord: Coord) -> List[int]:
        """
        Returns the IDs of objects which have parts in the cell, top-to-bottom
        """
        ret = copy.copy(self.cell_objs_map[cell_coord.row][cell_coord.col])
        ret.reverse()
        return ret

    def get_surface(self) -> pg.Surface:
        return copy.copy(self.surf)
