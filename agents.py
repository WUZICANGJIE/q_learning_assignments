#!/usr/bin/env python3
import random
from abc import ABC, abstractmethod
from tictactoe import TicTacToe

class Agent(ABC):
    def __init__(self, player):
        self.player = player

    @abstractmethod
    def select_move(self, board):
        pass

    def update(self, board, reward):
        pass

class RandomAgent(Agent):
    def select_move(self, board):
        empty_cells = [(i, j) for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == 0]
        return random.choice(empty_cells)

class HumanAgent(Agent):
    def select_move(self, board):
        while True:
            try:
                x = int(input(f'プレイヤー {self.player}、行を入力してください: '))
                y = int(input(f'プレイヤー {self.player}、列を入力してください: '))
                if board[x][y] == 0:
                    return (x, y)
                else:
                    print('そのセルは既に埋まっています。もう一度試してください。')
            except (ValueError, IndexError):
                print('無効な入力です。有効な行と列の番号を入力してください。')

class QAgent(Agent):
    def __init__(self, player, alpha=0.1, gamma=0.9, epsilon=0.1):
        super().__init__(player)
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = {}
        self.last_state = None
        self.last_action = None

    def get_state(self, board):
        return tuple(tuple(row) for row in board)

    def select_move(self, board):
        state = self.get_state(board)
        self.last_state = state
        if random.uniform(0, 1) < self.epsilon:
            empty_cells = [(i, j) for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == 0]
            action = random.choice(empty_cells)
        else:
            q_values = self.q_table.get(state, {})
            if q_values:
                max_q = max(q_values.values())
                max_actions = [action for action, q in q_values.items() if q == max_q]
                action = random.choice(max_actions)
            else:
                empty_cells = [(i, j) for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == 0]
                action = random.choice(empty_cells)

        self.last_action = action
        return action

    def update(self, board, reward):
        state = self.last_state
        action = self.last_action
        next_state = self.get_state(board)

        # Q値の初期化
        self.q_table.setdefault(state, {})
        self.q_table[state].setdefault(action, 0.0)
        self.q_table.setdefault(next_state, {})

        # Q学習の更新ルール
        future_rewards = self.q_table[next_state].values()
        max_future_q = max(future_rewards) if future_rewards else 0.0
        old_q = self.q_table[state][action]
        self.q_table[state][action] = old_q + self.alpha * (reward + self.gamma * max_future_q - old_q)


