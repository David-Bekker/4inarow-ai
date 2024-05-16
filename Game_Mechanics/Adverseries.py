import random
from Basic_Things import Basic_Game_Functions


def possible_choices(gameboard):
    choices = []
    for i in range(7):
        if gameboard[0][i] == 0:
            choices.append(i)
    return choices


def center_check(choice):
    if choice == 3:
        return 0.75
    elif choice == 4 or choice == 2:
        return 0.5
    elif choice == 5 or choice == 1:
        return 0.25
    else:
        return 0


def random_adversary(gameboard, player):
    choices = possible_choices(gameboard)
    machine_input = random.choice(choices)
    return machine_input


def check_how_many_free_space(game_board):
    free_spots = 0
    for i in range(len(game_board)):
        for j in range(7):
            if int(game_board[i][j]) == 0:
                free_spots += 1
    return free_spots
