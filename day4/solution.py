import copy
from functools import reduce


def pad(input, amt=1):
    padding = "."*amt
    result = [list("."*len(input[0]) + 2*padding) * amt]
    result += [list(padding+line+padding) for line in input]
    result += [list("."*len(input[0]) + 2*padding) * amt]
    return result


def processInput(filepath):
    with open(filepath) as file:
        return pad([line.strip() for line in file.readlines()])


def isAccessible(square, maxAdjacent=4):
    n = len(square)
    if square[n//2][n//2] != "@":
        return False

    count = reduce(lambda a, row: a + reduce(lambda a,
                   c: a + (c == "@"), row, 0), square, 0)
    return count <= maxAdjacent


def partOne(filepath):
    board = processInput(filepath)
    rows, cols = len(board), len(board[0])

    return reduce(lambda a, i:
                  a + reduce(lambda b, j:
                             b + isAccessible([row[j:j+3]
                                               for row in board[i:i+3]]),
                             range(cols-2), 0),
                  range(rows-2), 0)


def unpad(input, amt=1):
    return [row[amt:-amt] for row in input][amt:-amt]


def partOneVisualizer(filepath):
    board = processInput(filepath)
    result = copy.deepcopy(board)
    rows, cols = len(board), len(board[0])
    for i in range(rows-2):
        for j in range(cols - 2):
            square = [row[j:j+3] for row in board[i:i+3]]
            if isAccessible(square):
                result[i+1][j+1] = "x"
    for row in unpad(result):
        print(row)


partOneVisualizer("test.txt")
partOne("test.txt")  # 13
partOne("input.txt")  # 1435
