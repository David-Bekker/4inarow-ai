import math
import random
from Game_Mechanics import Adverseries


class BetaAi:
    def init(self):
        self.ai = 0
        self.human = 0
        pass

    # @profile
    def get_move(self, board, player):
        self.ai = player
        self.human = 3 - player
        col, _ = self.minimax(board, 7, -math.inf, math.inf, True)
        print(player, ",", col)
        return col

    # board[i][j] == player #player
    # board[i][j] == 3 - player #player 2
    # board[i][j] == 0 #empty place
    # depth = moves ahead

    # @profile
    def minimax(self, board, depth, alpha, beta, maximizingPlayer):
        is_terminal = self.is_terminal_node(board)
        if depth == 0 or is_terminal:
            if is_terminal:
                if self.winning_move(board, self.ai):
                    return None, 100000000000000
                elif self.winning_move(board, self.human):
                    return None, -10000000000000
                else:  # Game is over, no more valid moves
                    return None, 0
            else:  # Depth is zero
                return None, self.utility_calc(board)
        if maximizingPlayer:
            value = -math.inf
            choise = Adverseries.possible_choices(board)
            try:
                column = random.choice(Adverseries.possible_choices(board))
            except:
                column = 0
            for col in choise:
                row = self.get_next_open_row(board, col)
                # b_copy = copy.deepcopy(board)
                #self.drop_piece(b_copy, row, col, self.ai)
                self.drop_piece(board, row, col, self.ai)
                _, new_score = self.minimax(board, depth-1, alpha, beta, False)
                self.remove_piece(board, row, col)
                if new_score > value:
                    value = new_score
                    column = col
                # alpha = max(alpha, value)
                # if alpha >= beta:
                #     break
            return column, value
        else:  # Minimizing player
            value = math.inf
            choise = Adverseries.possible_choices(board)
            try:
                column = random.choice(Adverseries.possible_choices(board))
            except:
                column = 0
            for col in choise:
                row = self.get_next_open_row(board, col)
                # b_copy = copy.deepcopy(board)
                self.drop_piece(board, row, col, self.human)
                _, new_score = self.minimax(board, depth - 1, alpha, beta, True)
                self.remove_piece(board, row, col)
                if new_score < value:
                    value = new_score
                    column = col
                # beta = min(beta, value)
                # if alpha >= beta:
                #    break
            return column, value

    # @profile
    def get_next_open_row(self, board, col):
        for r in range(6):
            if board[5-r][col] == 0:
                return 5-r

    # @profile
    def drop_piece(self, board, row, col, player):
        board[row][col] = player

    # @profile
    def remove_piece(self, board, row, col):
        board[row][col] = 0

    # @profile
    def utility_calc(self, board):
        score = 0

        # Score center column |=|
        center_array = []
        for i in board[:][3]:
            center_array.append(i)
        center_count = center_array.count(self.ai)
        score += center_count * 3

        # Score Horizontal --
        for r in range(6):
            row_array = []
            for i in board[r][:]:
                row_array.append(i)
            for c in range(4):
                window = row_array[c:c + 4]
                score += self.evaluate_board(window)

        # Score Vertical |
        for c in range(7):
            col_array = []
            for i in range(6):
                col_array.append(board[i][c])
            for r in range(3):
                window = col_array[r:r + 4]
                score += self.evaluate_board(window)

        # Score positive sloped diagonal / \
        for r in range(3):
            for c in range(4):
                window = [board[r + i][c + i] for i in range(4)]
                score += self.evaluate_board(window)
        for r in range(3):
            for c in range(4):
                window = [board[r + 3 - i][c + i] for i in range(4)]
                score += self.evaluate_board(window)
        return score

    # @profile
    def evaluate_board(self, board):
        board_count = [0, 0, 0]
        # board_count[0] = ai
        # board_count[1] = human
        # board_count[2] = empty
        for i in range(4):
            if board[i] == self.ai:
                board_count[0] += 1
            elif board[i] == self.human:
                board_count[1] += 1
            else:
                board[2] += 1
        score = 0
        opp_piece = self.human
        if board_count[0] == 4:
            score += 1000000
        elif board_count[0] == 3 and board_count[2] == 1:
            score += 5
        elif board_count[0] == 2 and board_count[2] == 2:
            score += 2
        elif board_count[1] == 4:
            score -= 1000000
        elif board_count[1] == 3 and board_count[2] == 1:
            score -= 5
        return score

    # @profile
    def winning_move(self, board, player):
        # CHECK_ROWS
        for y in range(6):
            sum = 0
            for x in range(7):
                if board[y][x] == player:
                    sum += 1
                    if sum == 4:
                        return True
                else:
                    sum = 0

        # CHECK_COLUMNS
        for x in range(7):
            sum = 0
            for y in range(6):
                if board[y][x] == player:
                    sum += 1
                    if sum == 4:
                        return True
                else:
                    sum = 0
        # CHECK DIAGONAL
        for j in range(3):
            for i in range(4):
                sum_1 = 0
                for x in range(4):
                    if board[x + j][x + i] == player:
                        sum_1 += 1
                        if sum_1 == 4:
                            return True
                    else:
                        sum_1 = 0
                sum_2 = 0
                for x in range(4):
                    if board[5 - (x + j)][x + i] == player:
                        sum_2 += 1
                        if sum_2 == 4:
                            return True
                    else:
                        sum_2 = 0
        return False

    # @profile
    def is_terminal_node(self, board):
        return self.winning_move(board, self.ai) or self.winning_move(board, self.human) or Adverseries.possible_choices(board) == 0