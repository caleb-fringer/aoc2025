import math
import functools
import re

x = 123456


def toLog(x):
    n = math.ceil(math.log10(x))
    if x % 10 == 0:
        n += 1
    mantissa = x / (10 ** (n//2))
    return mantissa, n


def toDec(mantissa, n):
    return int(mantissa * 10 ** (n//2))


def recoverFractional(num):
    '''
    Recover the fractional part of the number as an integer.
    '''
    asString = str(num)
    fractional = re.sub(r'\d+\.', '', asString)
    return int(fractional)


recoverFractional(123.45)
recoverFractional(123.405)
recoverFractional(.45)

10**(6)


def count(bounds):
    lower, upper = bounds
    if lower > upper:
        return 0

    if lower == 1:
        return count((2, upper))

    lower_mantissa, lower_exp = toLog(lower)
    upper_mantissa, upper_exp = toLog(upper)

    if lower_exp % 2 == 1:
        newBounds = toDec(1, lower_exp+1), upper
        return count(newBounds)

    if upper_exp % 2 == 1:
        newBounds = lower, toDec(1, upper_exp+1) - 1
        return count(newBounds)

    if lower_exp < upper_exp:
        leftPartition = (lower, (10**lower_exp)-1)
        rightPartition = (10**lower_exp, upper)
        return count(leftPartition) + count(rightPartition)

    lower_left = int(math.floor(lower_mantissa))
    lower_right = recoverFractional(lower_mantissa)

    upper_left = int(math.floor(upper_mantissa))
    upper_right = recoverFractional(upper_mantissa)

    start = lower_left if lower_right <= lower_left else lower_left + 1
    end = upper_left if upper_right >= upper_left else upper_right - 1
    return 1 + end - start


count((11, 22))
count((95, 115))
count((998, 1012))
count((38593856, 38593862))
count((9999984021, 10000017929))
count((19391, 47353))

'''
Cursed FP
functools.reduce(lambda s, b: s + count(b), 
    map(lambda x: tuple(map(int, x.split("-"))), 
        file.readline().split(",")), 
    0)
'''
with open("input.txt") as file:
    puzzle_input = map(lambda x: tuple(map(int, x.split("-"))),
                       file.readline().split(","))
    for b in puzzle_input:
        print(b)
        print(count(b))
