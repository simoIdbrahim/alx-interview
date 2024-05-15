#!/usr/bin/python3
""" task N queens """


def solve_n_queens(num):
    """ solve n queens function """
    def is_safe(board, row, col):
        """ is safe function """
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def backtrack(board, row):
        """ backtrack function """
        if row == num:
            solutions.append(list(board))
            return

        for col in range(num):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)

    solutions = []
    chessboard = [-1] * num
    backtrack(chessboard, 0)
    return solutions


def print_solutions(solutions):
    """ print solutions function """
    for solution in solutions:
        print([[i, solution[i]] for i in range(len(solution))])


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(N)
    print_solutions(solutions)

