def preprocess(filepath):
    with open(filepath) as file:
        return [tuple(map(int, line.split(","))) for line in file.readlines()]


def getArea(a, b):
    '''
    Each (x,y) pair tells us the (0-based) index of where the red tile falls on the grid.

    Given (x1,y1), and (x2,y2), the area of the rectangle will be
    (x2-x1+1) * (y2-y1+1), assuming that x1<x2 and y1<y2
    '''
    ax, ay = a
    bx, by = b
    length = abs(bx-ax) + 1
    width = abs(by-ay) + 1
    return length*width


def solution(filepath):
    input = preprocess(filepath)
    maxArea = 0
    for i in range(len(input)):
        for j in range(i+1, len(input)):
            maxArea = max(maxArea, getArea(input[i], input[j]))
    return maxArea


solution("test.txt")  # 50
solution("input.txt")  # 4777816465
