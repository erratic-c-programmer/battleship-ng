import pygame as pg
import copy


class Grid:
    def __init__(self, grid_size, cell_size, line_width, line_colour, fill_colour):
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.line_width = line_width
        self.line_colour = line_colour
        self.fill_colour = fill_colour
        self.objcnt = 0  # No. of objects in the grid, also acts as ID==index for next obj

        self.total_size = ((grid_size[0] * (cell_size[0] + line_width) + line_width,
                            grid_size[1] * (cell_size[1] + line_width) + line_width))

        self.objects = []
        self.cell_objs_map = []
        for i in range(grid_size[0]):
            self.cell_objs_map.append([])
            for j in range(grid_size[1]):
                self.cell_objs_map[i].append([])

        self.surf = pg.Surface((self.total_size[0], self.total_size[1]))
        return

    def cell2surf(self, cell_coord):
        """
        Converts cell coordinates to surface coordinates
        """
        return (self.line_width + cell_coord[0] * (self.cell_size[0] + self.line_width),
                self.line_width + cell_coord[1] * (self.cell_size[1] + self.line_width))

    def add_obj(self, newsurf, cell_coord, box_size):
        self.objects.append((newsurf, self.cell2surf(cell_coord), box_size))
        for i in range(cell_coord[0], cell_coord[0] + box_size[0]):
            for j in range(cell_coord[1], cell_coord[1] + box_size[1]):
                self.cell_objs_map[i][j].append(self.objcnt)
        self.objcnt += 1

        return

    def draw(self):
        self.surf.fill(self.fill_colour)

        for i in range(0, self.total_size[0], self.cell_size[0] + self.line_width):
            pg.draw.line(
                self.surf, self.line_colour, (i, 0), (i,
                                                      self.total_size[1]), self.line_width
            )

        for i in range(0, self.total_size[1], self.cell_size[1] + self.line_width):
            pg.draw.line(
                self.surf, self.line_colour, (0, i), (
                    self.total_size[0], i), self.line_width
            )

        for s in self.objects:
            self.surf.blit(s[0], s[1])

    def get_cell_obj(self, cell):
        """
        Returns the IDs of objects which have parts in the cell, top-to-bottom
        """
        ret = copy.copy(self.cell_objs_map[cell[0]][cell[1]])
        ret.reverse()
        return ret
