from Game_Mechanics import Adverseries

class RandomPlayer:
    def __init__(self):
        pass

    def get_move(self, board, player):
        return Adverseries.random_adversary(board, player)
