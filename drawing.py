import pygame as pg
import library as lib


def drawGrid():
    for x in range(1, 3):
        pg.draw.line(window, lib.GRID_COLOR, (0, x * lib.grid_size), (lib.window_size, x * lib.grid_size),
                     lib.lineWidth)
        pg.draw.line(window, lib.GRID_COLOR, (x * lib.grid_size, 0), (x * lib.grid_size, lib.window_size),
                     lib.lineWidth)


def prepare_grid():
    global x
    for x in range(3):
        row = [0] * 3
        lib.markers.append(row)


def drawMarkers():
    x_pos = 0
    for x in lib.markers:
        y_pos = 0
        for y in x:
            if y == 1:  # Player 1's marker (X)
                center_x = x_pos * lib.grid_size + lib.grid_size // 2
                center_y = y_pos * lib.grid_size + lib.grid_size // 2
                pg.draw.line(window, lib.P1_COLOR, (center_x - lib.markers_adj, center_y - lib.markers_adj),
                             (center_x + lib.markers_adj, center_y + lib.markers_adj), lib.lineWidth)
                pg.draw.line(window, lib.P1_COLOR, (center_x - lib.markers_adj, center_y + lib.markers_adj),
                             (center_x + lib.markers_adj, center_y - lib.markers_adj), lib.lineWidth)
            elif y == -1:  # Player 2's marker (O)
                center_x = x_pos * lib.grid_size + lib.grid_size // 2
                center_y = y_pos * lib.grid_size + lib.grid_size // 2
                pg.draw.circle(window, lib.P2_COLOR, (center_x, center_y), lib.grid_size // 2 - lib.lineWidth,
                               lib.lineWidth)
            y_pos += 1
        x_pos += 1


def printWinner(winner):
    win_text = ""
    if lib.winner == 0:
        win_text = "It's a draw!"
        win_img = font.render(win_text, True, lib.FONT_COLOR)
        pg.draw.rect(window, lib.WINNER_BG_COLOR,
                     (lib.window_size // 2 - 100, lib.window_size // 2 - 15, 200, 30))  # Center the text on the screen
        window.blit(win_img, (lib.window_size // 2 - 100, lib.window_size // 2 - 15))
    else:
        win_text = "Player " + str(winner) + " wins"
        win_img = font.render(win_text, True, lib.FONT_COLOR)
        pg.draw.rect(window, lib.WINNER_BG_COLOR,
                     (lib.window_size // 2 - 100, lib.window_size // 2 - 15, 200, 30))  # Center the text on the screen
        window.blit(win_img, (lib.window_size // 2 - 100, lib.window_size // 2 - 15))

    play_again_str = "Play again?"
    play_again_img = font.render(play_again_str, True, lib.FONT_COLOR)
    pg.draw.rect(window, lib.WINNER_BG_COLOR, play_again_rect)
    window.blit(play_again_img, (lib.window_size // 2 - 85, lib.window_size // 2 + 20, 170, 30))


pg.init()

font = pg.font.SysFont(None, 40)  # font

play_again_rect = pg.Rect(lib.window_size // 2 - 85, lib.window_size // 2 + 20, 170, 30)

window = pg.display.set_mode((lib.window_size, lib.window_size))
pg.display.set_caption("TIC TAC TOE")
