#! /usr/bin/python

import grid
import pygame as pg
from common_types import Size2d, Coord
import ship


pg.init()

# Set up the drawing window
screen = pg.display.set_mode((800, 800))

mygrid = grid.Grid(Size2d(10, 10), Size2d(50, 50), 1, (0, 0, 0), (255, 255, 255))

mygrid.surf2cell(Coord(60, 60))
mygrid.surf2cell(Coord(10, 20))
mygrid.surf2cell(Coord(10, 110))

circlesurf = pg.Surface((101, 101))
pg.draw.circle(circlesurf, (255, 0, 0), (50.5, 50.5), 50.5)
mygrid.add_obj(grid.GridObj(circlesurf, Coord(0, 0), Size2d(2, 2)))

rectsurf = pg.Surface((152, 152))
pg.draw.rect(rectsurf, (0, 255, 255), ((0, 0), (152, 152)))
mygrid.add_obj(grid.GridObj(rectsurf, Coord(1, 1), Size2d(3, 3)))

nullsurf = pg.Surface((0, 0))

myship = ship.Ship(Size2d(3, 1), Size2d(51, 51), (60, 70, 80), nullsurf)
myship.draw()
mygrid.add_obj(grid.GridObj(myship.get_surface(), Coord(4, 4), Size2d(3, 1)))

myship2 = ship.Ship(Size2d(1, 4), Size2d(51, 51), (30, 170, 80), nullsurf)
myship2.draw()
mygrid.add_obj(grid.GridObj(myship2.get_surface(), Coord(5, 3), Size2d(1, 4)))

for i in range(10):
    for j in range(10):
        print(f"({i},{j}): ", end="")
        for oid in mygrid.get_cell_obj(Coord(i, j)):
            print(oid, end=",")
        print("")

# Run until the user asks to quit
running = True
while running:
    pg.time.wait(10)

    # Did the user click the window close button?
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    mygrid.draw()
    screen.blit(mygrid.surf, (0, 0))

    # Flip the display
    pg.display.flip()

# Done! Time to quit.
pg.quit()
