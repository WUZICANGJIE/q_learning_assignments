#!/usr/bin/env python3
from agents import RandomAgent, HumanAgent
from tictactoe import TicTacToe

if __name__ == '__main__':
    n = 3
    game = TicTacToe(n)
    agents = [HumanAgent(1), RandomAgent(2)]
    print('ゲーム開始、サイズは' + str(n) + 'です、先手は1(○)、後手は2(×)です')
    while game.get_state() == 0:
        player = game.get_next()
        agent = agents[player - 1]
        x, y = agent.select_move(game._TicTacToe__board)
        print('プレイヤー:', player, '行:', x, '列:', y, 'にマークを置きます。')
        game.interactive_play(player, x, y)
        game.print_board()
    else:
        del game