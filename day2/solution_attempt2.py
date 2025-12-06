from operator import add
import functools
import re


def split(num):
    asStr = str(num)

    n = len(asStr)//2
    return map(int, (asStr[:n], asStr[n:]))


def count(bounds):
    lower, upper = bounds
    if lower > upper:
        return 0

    if len(str(lower)) % 2 == 1:
        newLower = 10 ** len(str(lower))
        return count((newLower, upper))
    if len(str(upper)) % 2 == 1:
        newUpper = 10 ** (len(str(upper)) - 1) - 1
        return count((lower, newUpper))
    if len(str(lower)) != len(str(upper)):
        leftPartition = lower, 10**len(str(lower)) - 1
        rightPartition = 10**(len(str(lower))+1), upper
        return count(leftPartition) + count(rightPartition)

    lower_l, lower_r = split(lower)
    upper_l, upper_r = split(upper)
    start = lower_l if lower_r <= lower_l else lower_l + 1
    end = upper_l if upper_r >= upper_r else upper_l - 1

    sum = 0
    while start <= end:
        sum += int(str(start) + str(start))
        start += 1
    return sum


sum([
    count((11, 22)),
    count((95, 115)),
    count((998, 1012)),
    count((1188511880, 1188511890)),
    count((222220, 222224)),
    count((1698522, 1698528)),
    count((446443, 446449)),
    count((38593856, 38593862))
])  # 1227775554

count((2, 17))
count((9999984021, 10000017929))
with open("input.txt") as file:
    puzzle_input = map(lambda x: tuple(map(int, x.split("-"))),
                       file.readline().split(","))
    result = functools.reduce(lambda a, x: a + count(x), puzzle_input, 0)
result
