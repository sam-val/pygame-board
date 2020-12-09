## pygame-board
Making drawing board-oriented stuff a bit easier.

## Usage

```
import pygame as pg
from pygame_board import Board, MyRect

# set size of board **which is measured in cubes**.

BOARD_HEIGHT = 5 # five cubes high
BOARD_WIDTH = 5 # five cubes wide
CUBE_WIDTH = 100

# init pygame:

pg.display.init()
screen = pg.display.set_mode([BOARD_WIDTH*CUBE_WIDTH, BOARD_HEIGHT*CUBE_WIDTH])


# Generate your board:
my_cube = MyRect(size=(CUBE_WIDTH, CUBE_WIDTH), colour='red')
my_board = Board(screen, position(0,0), size=(BOARD_WIDTH, BOARD_HEIGHT),
		cube=my_cube, 
		line=True,
		border=True)

# game loop:
while True:
	# the program quits if 'q' is pressed.
	for e in pg.event.get():
		if e.type -- pg.KEYDOWN:
			if e.key == pg.K_q:
				pg.quit()
	
	# display board:
	my_board.draw()

	pg.display.flip()

```

## Gifs:
...
