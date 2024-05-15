#!/usr/bin/python3
""" task queens """


def queens(chessBoard, r, maje, res):
    """ queens method """
    if maje == len(chessBoard):
        res.append(extract(chessBoard))
        return (res)

    for col in range(len(chessBoard)):
        if chessBoard[r][col] == -1:
            demo = copy_board(chessBoard)
            demo[r][col] = 1
            exit_queens(demo, r, col)
            res = queens(demo, r + 1, maje + 1, res)
    return (res)


def exit_queens(chessBoard, r, col):
    """ exit_queens method """
    len = len(chessBoard)
    for c in range(col + 1, len):
        chessBoard[r][c] = 0
    for c in range(col - 1, -1, -1):
        chessBoard[r][c] = 0
    for r in range(r + 1, len):
        chessBoard[r][col] = 0
    for r in range(r - 1, -1, 1):
        chessBoard[r][col] = 0
    c = col + 1
    for r in range(r + 1, len):
        if c >= len:
            break
        chessBoard[r][c] = 0
        c += 1
    c = col - 1
    for r in range(r - 1, -1, -1):
        if c < 0:
            break
        chessBoard[r][c] = 0
        c -= 1
    c = col + 1
    for r in range(r - 1, -1, -1):
        if c >= len:
            break
        chessBoard[r][c] = 0
        c += 1
    c = col - 1
    for r in range(r + 1, len):
        if c < 0:
            break
        chessBoard[r][c] = 0
        c -= 1


def chessBoard(N):
    """ chessBoard method"""
    chessBoard = []

    for r in range(N):
        chessBoard.append([])

    for r in chessBoard:
        for n in range(N):
            r.append(-1)

    return (chessBoard)


def copy_board(chessBoard):
    """ copy_board method """
    if type(chessBoard) == list:
        return list(map(copy_board, chessBoard))
    return (chessBoard)


def extract(chessBoard):
    """ extract method """
    outcome = []
    for row in range(len(chessBoard)):
        for col in range(len(chessBoard)):
            if chessBoard[row][col] == 1:
                outcome.append([row, col])
                break
    return outcome


def execute():
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isnumeric() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    chess = chessBoard(int(sys.argv[1]))
    resultMatrix = queens(chess, 0, 0, [])
    for r in resultMatrix:
        print(r)


if __name__ == '__main__':
    execute()
