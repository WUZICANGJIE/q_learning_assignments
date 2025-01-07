#!/usr/bin/env python3

class CountBoards:
    def __init__(self, n=3):
        self.n = n
        self.cells = n * n
        self.symbols = [0, 1, 2]  # 0="",1=O,2=X

    def is_valid(self, board):
        o_count = board.count(1)
        x_count = board.count(2)
        return o_count == x_count or o_count == x_count + 1

    def rotate(self, matrix):
        return [list(row) for row in zip(*matrix[::-1])]

    def reflect_horizontal(self, matrix):
        return matrix[::-1]

    def reflect_vertical(self, matrix):
        return [row[::-1] for row in matrix]

    def reflect_diagonal(self, matrix):
        n = len(matrix)
        return [[matrix[j][i] for j in range(n)] for i in range(n)]

    def reflect_anti_diagonal(self, matrix):
        n = len(matrix)
        return [[matrix[n-j-1][n-i-1] for j in range(n)] for i in range(n)]

    def get_symmetries(self, board):
        n = self.n
        mat = [board[i*n:(i+1)*n] for i in range(n)]
        transformations = [
            lambda x: x,
            lambda x: self.rotate(x),
            lambda x: self.rotate(self.rotate(x)),
            lambda x: self.rotate(self.rotate(self.rotate(x))),
            lambda x: self.reflect_horizontal(x),
            lambda x: self.reflect_vertical(x),
            lambda x: self.reflect_diagonal(x),
            lambda x: self.reflect_anti_diagonal(x)
        ]
        boards = []
        for transform in transformations:
            t = transform(mat)
            boards.append(sum(t, []))
        return boards

    def generate_boards(self, n):
        def backtrack(pos, current):
            if pos == n*n:
                yield current[:]
                return
            for s in self.symbols:
                current[pos] = s
                yield from backtrack(pos+1, current)
        yield from backtrack(0, [0]*(n*n))


if __name__ == "__main__":
    bf = CountBoards(n=4)
    all_boards = set()
    count = 0

    for board in bf.generate_boards(bf.n):
        if not bf.is_valid(board):
            continue

        symmetries = bf.get_symmetries(board)
        canonical_form = min(symmetries)
        cf_tuple = tuple(canonical_form)
        if cf_tuple not in all_boards:
            all_boards.add(cf_tuple)
            count += 1

    print(f"力尽く法で求めた{bf.n}目並べの状態の数：{count}")

# 力尽く法で求めた3目並べの状態の数：850
# 力尽く法で求めた4目並べの状態の数：1273771