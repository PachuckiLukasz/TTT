import pygame as pg
import library as lib
import drawing
import sys

import winner

pg.init()

drawing.prepare_grid()

while lib.running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            lib.running = False
        if not lib.game_over:
            if event.type == pg.MOUSEBUTTONDOWN and not lib.clicked:
                lib.clicked = True
            if event.type == pg.MOUSEBUTTONUP and lib.clicked:
                lib.clicked = False
                lib.pos = pg.mouse.get_pos()
                cell_x = lib.pos[0]
                cell_y = lib.pos[1]
                if lib.markers[cell_x // lib.grid_size][cell_y // lib.grid_size] == 0:
                    lib.markers[cell_x // lib.grid_size][cell_y // lib.grid_size] = lib.player
                    lib.player *= -1
                    winner.checkWinner()

    if lib.game_over:
        drawing.printWinner(lib.winner)
        # check does user clicked on play again rect
        if event.type == pg.MOUSEBUTTONDOWN and not lib.clicked:
            lib.clicked = True
        if event.type == pg.MOUSEBUTTONUP and lib.clicked:
            lib.clicked = False
            lib.pos = pg.mouse.get_pos()
            if drawing.play_again_rect.collidepoint(lib.pos):
                # reset var
                lib.markers = []
                lib.pos = []
                lib.player = 1
                lib.winner = 0
                lib.game_over = False
                for x in range(3):
                    row = [0] * 3
                    lib.markers.append(row)

    pg.display.update()
    # clear the screen
    drawing.window.fill((208, 219, 121))  # fill with background

    # draw the game objects here
    drawing.drawGrid()
    drawing.drawMarkers()

# after the loop close the pygame and quit game
pg.quit()
sys.exit()
