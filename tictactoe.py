#!/usr/bin/env python3

class TicTacToe:
    def __init__(self, n = None):
        if n == None:
            print('１桁の正の整数のサイズを指定してください')
            return
        if not isinstance(n, int) or not (1 <= n <= 9):
            print('サイズは１桁の正の整数でなければなりません')
            return
        self.__size = n
        self.__next = 1
        self.__board = [[0 for _ in range(n)] for _ in range(n)]
        self.__state = 0

    def get_next(self):
        return self.__next

    def get_state(self):
        return self.__state

    def play(self, player, x, y):
        self.__board[x][y] = player
        if self.check_winner(player, x, y):
            self.__state = 2
            self.__winner = player
            return
        elif self.check_draw():
            self.__state = 1
            return
        else:
            self.__next = 1 if self.__next == 2 else 2

    def interactive_play(self, player, x, y):
        if player != self.__next:
            print('' + str(player) + '番のプレイヤーの番ではありません')
            return
        if self.__board[x][y] != 0:
            print('すでに置かれています')
            return
        self.__board[x][y] = player
        if self.check_winner(player, x, y):
            self.__state = 2
            self.__winner = player
            print('' + str(player) + '番のプレイヤーの勝ち')
            return
        elif self.check_draw():
            self.__state = 1
            print('引き分け')
            return
        else:
            self.__next = 1 if self.__next == 2 else 2

    def print_board(self):
        for row in self.__board:
            for cell in row:
                if cell == 0:
                    print('□', end = ' ')
                elif cell == 1:
                    print('○', end = ' ')
                elif cell == 2:
                    print('×', end = ' ')
            print()

    def check_winner(self, player, x, y):
        for i in range(self.__size):
            if self.__board[i][y] != player:
                break
        else:
            return True
        for i in range(self.__size):
            if self.__board[x][i] != player:
                break
        else:
            return True
        if x == y:
            for i in range(self.__size):
                if self.__board[i][i] != player:
                    break
            else:
                return True
        if x + y == self.__size - 1:
            for i in range(self.__size):
                if self.__board[i][self.__size - 1 - i] != player:
                    break
            else:
                return True
        return False

    def check_draw(self):
        for row in self.__board:
            if 0 in row:
                return False
        return True