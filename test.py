#! /usr/bin/python

import grid
import pygame as pg
from common_types import Size2d, Coord
import ship


pg.init()

# Set up the drawing window
screen = pg.display.set_mode((800, 800))

mygrid = grid.Grid(
    grid_size=Size2d(10, 10),
    cell_size=Size2d(50, 50),
    line_width=1,
    line_colour=(0, 0, 0),
    fill_colour=(255, 255, 255),
)

myship = ship.Ship(
    size=Size2d(3, 1),
    position=Coord(0, 0),
    cell_size=Size2d(51, 51),
    colour=(60, 70, 80),
)
myship.draw()
mygrid.add_obj(myship)

myship2 = ship.Ship(
    size=Size2d(1, 4),
    position=Coord(5, 7),
    cell_size=Size2d(51, 51),
    colour=(30, 170, 80),
)
myship2.draw()
mygrid.add_obj(myship2)

for i in range(10):
    for j in range(10):
        print(f"({i},{j}): ", end="")
        for oid in mygrid.get_cell_obj(Coord(i, j)):
            print(oid, end=",")
        print("")

# Run until the user asks to quit
running = True
while running:

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
