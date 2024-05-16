from math import sin, cos, pi
import pygame


def tie_check(gameboard):
    sum = 0
    for i in range(7):
        if gameboard[0][i] > 0:
            sum += 1
    if sum == 7:
        return 1
    else:
        return 0


def Winner_check(gameboard, player):
    # CHECK_ROWS
    for y in range(6):
        sum = 0
        for x in range(7):
            if gameboard[y][x] == player:
                sum += 1
                if sum == 4:
                    return player
            else:
                sum = 0

    # CHECK_COLUMNS
    for x in range(7):
        sum = 0
        for y in range(6):
            if gameboard[y][x] == player:
                sum += 1
                if sum == 4:
                    return player
            else:
                sum = 0
    # CHECK DIAGONAL
    for j in range(3):
        for i in range(4):
            sum_1 = 0
            for x in range(4):
                if gameboard[x + j][x + i] == player:
                    sum_1 += 1
                    if sum_1 == 4:
                        return player
                else:
                    sum_1 = 0
            sum_2 = 0
            for x in range(4):
                if gameboard[5 - (x + j)][x + i] == player:
                    sum_2 += 1
                    if sum_2 == 4:
                        return player
                else:
                    sum_2 = 0
    return 0


def apply_move(gameboard, human_input, player):
    if gameboard[0][human_input] > 0:
        return gameboard
    else:
        for y in range(len(gameboard)):
            if gameboard[5 - y][human_input] == 0:
                gameboard[5 - y][human_input] = player
                return gameboard


def draw_gameboard(gameboard, screen, colors):
    for x in range(7):
        for y in range(6):
            if gameboard[y][x] == 0:
                pygame.draw.circle(screen, colors.LIGHT_GREY, [50 + x * 80, 50 + y * 80], 30)
            elif gameboard[y][x] == 1:
                pygame.draw.circle(screen, colors.RED, [50 + x * 80, 50 + y * 80], 30)
            elif gameboard[y][x] == 2:
                pygame.draw.circle(screen, colors.YELLOW, [50 + x * 80, 50 + y * 80], 30)


def switch_player(player):
    if player == 1:
        return 2
    else:
        return 1


def draw_regular_polygon(surface, color, vertex_count, radius, position):
    n, r = vertex_count, radius
    x, y = position
    pygame.draw.polygon(surface, color, [
        (x + r * cos(2 * pi * i / n), y + r * sin(2 * pi * i / n))
        for i in range(n)
    ])

    # surface = pygame.Surface([100, 100])
    # pygame.draw.polygon(surface, colors.BLACK, points, width=0)
    # Usefull_functions.draw_regular_polygon(surface, colors.BLACK, 5, 30, [0, 0])