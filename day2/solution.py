from operator import add
import functools
import re


def split(num):
    asStr = str(num)

    n = len(asStr)//2
    return map(int, (asStr[:n], asStr[n:]))


'''Part 1'''


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
    end = upper_l if upper_r >= upper_l else upper_l - 1

    sum = 0
    while start <= end:
        sum += int(str(start) + str(start))
        start += 1
    return sum


# Test input
with open("test.txt") as file:
    puzzle_input = map(lambda x: tuple(map(int, x.split("-"))),
                       file.readline().split(","))
    result = functools.reduce(lambda a, x: a + count(x), puzzle_input, 0)
result

count((19391, 47353))
count((4646427538, 4646497433))
count((4426384, 4463095))
count((527495356, 527575097))
count((2, 17))
count((9999984021, 10000017929))
count((77, 122))
count((165081, 338962))
assert count((26, 76)) == 33 + 44 + 55 + 66

with open("input.txt") as file:
    puzzle_input = map(lambda x: tuple(map(int, x.split("-"))),
                       file.readline().split(","))
    result = functools.reduce(lambda a, x: a + count(x), puzzle_input, 0)
result  # 24747430309

with open("test.txt") as file:
    puzzle_input = map(lambda x: tuple(map(int, x.split("-"))),
                       file.readline().split(","))
    result = functools.reduce(lambda a, x: a + count(x), puzzle_input, 0)
result

'''Part 2'''


def invalidIds(n):
    '''
    Given an integer of length n, generate all the invalid ids of length n
    with repeating sequences of length k >= 2.
    '''

    results = {}
    for k in range(2, n//2 + 1):
        if n % k == 0:
            results[k] = []
            z = (1-10**n) / (1-10**k)
            start = 10**(k-1)
            end = 10**(k) - 1
            for i in range(start, end):
                results[k].append(int(i * z))
    return results


result = invalidIds((100000, 999999))
result[3]
