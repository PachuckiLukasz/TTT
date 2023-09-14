import random

import library as lib


def checkWinner():
    if all(cell != 0 for row in lib.markers for cell in row):
        lib.winner = 0
        lib.game_over = True
        return
    y_pos = 0
    for z in lib.markers:
        # rows
        if sum(z) == 3:
            lib.winner = 1
            lib.game_over = True
        if sum(z) == -3:
            lib.winner = 2
            lib.game_over = True
        # columns
        if lib.markers[0][y_pos] + lib.markers[1][y_pos] + lib.markers[2][y_pos] == 3:
            lib.winner = 1
            lib.game_over = True
        if lib.markers[0][y_pos] + lib.markers[1][y_pos] + lib.markers[2][y_pos] == -3:
            lib.winner = 2
            lib.game_over = True
        y_pos += 1
        # cross
        if lib.markers[0][0] + lib.markers[1][1] + lib.markers[2][2] == 3 or lib.markers[2][0] + lib.markers[1][1] + \
                lib.markers[0][2] == 3:
            lib.winner = 1
            lib.game_over = True
        if lib.markers[0][0] + lib.markers[1][1] + lib.markers[2][2] == -3 or lib.markers[2][0] + lib.markers[1][1] + \
                lib.markers[0][2] == -3:
            lib.winner = 2
            lib.game_over = True


def ai_random_move():
    while True:
        # Generate random row and column indices
        ai_row = random.randint(0, 2)
        ai_col = random.randint(0, 2)

        # Check if the selected cell is empty
        if lib.markers[ai_row][ai_col] == 0:
            return ai_row, ai_col
