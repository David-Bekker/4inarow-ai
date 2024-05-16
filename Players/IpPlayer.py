from socket import *
from pickle import *

class IpPlayer:
    def __init__(self, ip):
        self.ip = ip
        self.init = True

    def get_move(self, board, player):
        if self.init:
            self.init = False
            if player == 2:
                # Send the board first
                self.socket = socket(AF_INET, SOCK_STREAM)
                self.socket.connect((self.ip, 7777))

            else: #recv the board first
                lsocket = socket(AF_INET, SOCK_STREAM)
                lsocket.bind(("0.0.0.0", 7777))
                lsocket.listen(1)
                self.socket, _ = lsocket.accept()
                lsocket.close()
                self.recvboard(board)
                return 8

        self.sendboard(board)
        self.recvboard(board)
        return 8

    def sendboard(self, board):
        self.socket.send(dumps(board))

    def recvboard(self, board):
        newboard = loads(self.socket.recv(0x1000))
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = newboard[i][j]
