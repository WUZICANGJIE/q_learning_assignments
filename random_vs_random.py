#!/usr/bin/env python3
from agents import RandomAgent
from tictactoe import TicTacToe

if __name__ == '__main__':
    n = 3
    num_games = 100000

    # 対戦ルール 1: 先手後手固定
    first_player_wins = 0
    second_player_wins = 0
    draws = 0

    for _ in range(num_games):
        game = TicTacToe(n)
        agents = [RandomAgent(1), RandomAgent(2)]
        while game.get_state() == 0:
            player = game.get_next()
            agent = agents[player - 1]
            x, y = agent.select_move(game._TicTacToe__board)
            game.play(player, x, y)
        if game.get_state() == 2:
            winner = 0 if game.get_next() == 1 else 1
            if winner == 0:
                first_player_wins += 1
            else:
                second_player_wins += 1
        else:
            draws += 1
        del game

    results1 = [first_player_wins, second_player_wins, draws]

    # 対戦ルール 2: 勝者が次の対局で後手になる
    first_player_wins = 0
    second_player_wins = 0
    draws = 0

    agents = [RandomAgent(1), RandomAgent(2)]
    first_player_is_agent1 = True

    for _ in range(num_games):
        game = TicTacToe(n)
        while game.get_state() == 0:
            player = game.get_next()
            agent = agents[player - 1]
            x, y = agent.select_move(game._TicTacToe__board)
            game.play(player, x, y)
        if game.get_state() == 2:
            winner = 3 - game.get_next()
            if (winner == 1 and first_player_is_agent1) or (winner == 2 and not first_player_is_agent1):
                first_player_wins += 1
            else:
                second_player_wins += 1
            # 勝者が次の対局で後手になるように順番を入れ替える
            agents = [agents[1], agents[0]]
            first_player_is_agent1 = not first_player_is_agent1
        else:
            draws += 1
        del game

    results2 = [first_player_wins, second_player_wins, draws]

    print('対戦ルール 1: 先手後手固定')
    print(f'先手の勝利数: {results1[0]} ({results1[0] / num_games * 100:.2f}%)')
    print(f'後手の勝利数: {results1[1]} ({results1[1] / num_games * 100:.2f}%)')
    print(f'引き分け数: {results1[2]} ({results1[2] / num_games * 100:.2f}%)')
    print()
    print('対戦ルール 2: 勝者が次の対局で後手になる')
    print(f'先手の勝利数: {results2[0]} ({results2[0] / num_games * 100:.2f}%)')
    print(f'後手の勝利数: {results2[1]} ({results2[1] / num_games * 100:.2f}%)')
    print(f'引き分け数: {results2[2]} ({results2[2] / num_games * 100:.2f}%)')

    # 対戦ルール 1: 先手後手固定
    # 先手の勝利数: 58418 (58.42%)
    # 後手の勝利数: 28943 (28.94%)
    # 引き分け数: 12639 (12.64%)

    # 対戦ルール 2: 勝者が次の対局で後手になる
    # 先手の勝利数: 43386 (43.39%)
    # 後手の勝利数: 43858 (43.86%)
    # 引き分け数: 12756 (12.76%)