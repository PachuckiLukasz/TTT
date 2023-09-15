import random

import library as lib


def checkWinner():
    player_won = False
    y_pos = 0
    for z in lib.markers:
        # rows
        player_won = horizontal_check(z, player_won)  # Check for horizontal win
        # columns
        player_won = vertical_check(y_pos, player_won)  # Check for vertical win
        y_pos += 1
        # cross
        player_won = cross_check(player_won)  # Check for cross win

    # Check for draw only if no player has won
    if not player_won:
        check_for_draw(player_won)


def cross_check(player_won):
    if lib.markers[0][0] + lib.markers[1][1] + lib.markers[2][2] == 3 or lib.markers[2][0] + lib.markers[1][1] + \
            lib.markers[0][2] == 3:
        lib.winner = 1
        lib.game_over = True
        player_won = True
    if lib.markers[0][0] + lib.markers[1][1] + lib.markers[2][2] == -3 or lib.markers[2][0] + lib.markers[1][1] + \
            lib.markers[0][2] == -3:
        lib.winner = 2
        lib.game_over = True
        player_won = True
    return player_won


def vertical_check(y_pos, player_won):
    if lib.markers[0][y_pos] + lib.markers[1][y_pos] + lib.markers[2][y_pos] == 3:
        lib.winner = 1
        lib.game_over = True
        player_won = True
    if lib.markers[0][y_pos] + lib.markers[1][y_pos] + lib.markers[2][y_pos] == -3:
        lib.winner = 2
        lib.game_over = True
        player_won = True
    return player_won


def horizontal_check(z, player_won):
    if sum(z) == 3:
        lib.winner = 1
        lib.game_over = True
        player_won = True
    if sum(z) == -3:
        lib.winner = 2
        lib.game_over = True
        player_won = True
    return player_won


def check_for_draw(player_won):
    if all(cell != 0 for row in lib.markers for cell in row) and not player_won:
        lib.winner = 0
        lib.game_over = True


def ai_random_move():
    while True:
        # Generate random row and column indices
        ai_row = random.randint(0, 2)
        ai_col = random.randint(0, 2)

        # Check if the selected cell is empty
        if lib.markers[ai_row][ai_col] == 0:
            return ai_row, ai_col
