#!/usr/bin/env python3
from agents import RandomAgent, QAgent
from tictactoe import TicTacToe

def print_progress(games_played, wins, losses, draws):
    win_rate = wins / games_played * 100
    loss_rate = losses / games_played * 100
    draw_rate = draws / games_played * 100
    print(f'\r {games_played}回試行 - 勝率: {win_rate:.2f}% 敗率: {loss_rate:.2f}% 引分: {draw_rate:.2f}%', end='')

if __name__ == '__main__':
    n = 3
    num_games = 1000000
    progress_interval = 10000  # 進捗表示の間隔
    print(f'{num_games}回の試行を開始します (サイズ{n})')
    print()

    # 対戦ルール 1: 先手:ランダムエージェント 後手:Q 学習エージェント
    wins = losses = draws = 0
    q_agent = QAgent(player=2)
    random_agent = RandomAgent(player=1)

    print("対戦ルール 1: 先手:ランダムエージェント 後手:Q 学習エージェント")
    for i in range(num_games):
        game = TicTacToe(n)
        while game.get_state() == 0:
            player = game.get_next()
            if player == 1:
                x, y = random_agent.select_move(game._TicTacToe__board)
            else:
                x, y = q_agent.select_move(game._TicTacToe__board)
            game.play(player, x, y)
            if player == random_agent.player:
                q_agent.update(game._TicTacToe__board, 0)
        if game.get_state() == 2:
            winner = game.get_next()
            if winner == q_agent.player:
                q_agent.update(game._TicTacToe__board, 1)
                wins += 1
            else:
                q_agent.update(game._TicTacToe__board, -1)
                losses += 1
        else:
            q_agent.update(game._TicTacToe__board, 0)
            draws += 1
        
        if (i + 1) % progress_interval == 0:
            print_progress(i + 1, wins, losses, draws)
        
        del game
    print()

    # 対戦ルール 2: 先手:Q 学習エージェント 後手:ランダムエージェント
    wins = losses = draws = 0
    q_agent = QAgent(player=1)
    random_agent = RandomAgent(player=2)

    print("\n対戦ルール 2: 先手:Q 学習エージェント 後手:ランダムエージェント")
    for i in range(num_games):
        game = TicTacToe(n)
        while game.get_state() == 0:
            player = game.get_next()
            if player == 1:
                x, y = q_agent.select_move(game._TicTacToe__board)
            else:
                x, y = random_agent.select_move(game._TicTacToe__board)
            game.play(player, x, y)
            if player == random_agent.player:
                q_agent.update(game._TicTacToe__board, 0)
        if game.get_state() == 2:
            winner = game.get_next()
            if winner == q_agent.player:
                q_agent.update(game._TicTacToe__board, 1)
                wins += 1
            else:
                q_agent.update(game._TicTacToe__board, -1)
                losses += 1
        else:
            q_agent.update(game._TicTacToe__board, 0)
            draws += 1
        
        if (i + 1) % progress_interval == 0:
            print_progress(i + 1, wins, losses, draws)
        
        del game
    print()

    # 対戦ルール 3: 勝者が次の対局で後手になる
    wins = losses = draws = 0
    q_agent = QAgent(player=1)
    random_agent = RandomAgent(player=2)
    first_player_is_q = True

    print("\n対戦ルール 3: 勝者が次の対局で後手になる")
    for i in range(num_games):
        game = TicTacToe(n)
        if not first_player_is_q:
            q_agent.player, random_agent.player = random_agent.player, q_agent.player
        while game.get_state() == 0:
            player = game.get_next()
            if player == q_agent.player:
                x, y = q_agent.select_move(game._TicTacToe__board)
            else:
                x, y = random_agent.select_move(game._TicTacToe__board)
            game.play(player, x, y)
            if player == random_agent.player:
                q_agent.update(game._TicTacToe__board, 0)
        if game.get_state() == 2:
            winner = game.get_next()
            if winner == q_agent.player:
                q_agent.update(game._TicTacToe__board, 1)
                wins += 1
            else:
                q_agent.update(game._TicTacToe__board, -1)
                losses += 1
            # 勝者が次の対局で後手になる
            first_player_is_q = (winner != q_agent.player)
        else:
            q_agent.update(game._TicTacToe__board, 0)
            draws += 1
        
        if (i + 1) % progress_interval == 0:
            print_progress(i + 1, wins, losses, draws)
        
        del game
    print()


# 1000000回の試行を開始します (サイズ3)

# 対戦ルール 1: 先手:ランダムエージェント 後手:Q 学習エージェント
#  1000000回試行 - 勝率: 83.83% 敗率: 5.91% 引分: 10.26%

# 対戦ルール 2: 先手:Q 学習エージェント 後手:ランダムエージェント
#  1000000回試行 - 勝率: 95.44% 敗率: 2.16% 引分: 2.40%

# 対戦ルール 3: 勝者が次の対局で後手になる
#  1000000回試行 - 勝率: 85.66% 敗率: 7.03% 引分: 7.31%