import pygame

class HumanPlayer:
    def __init__(self):
        pass

    def get_move(self, board, player):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pos[1] <= 500:
                    return int(pos[0] / 80)
        return -1
