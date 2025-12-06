import math

x = 123456


def toLog(x):
    n = math.ceil(math.log10(x))
    if x % 10 == 0:
        n += 1
    mantissa = x / (10 ** (n//2))
    return mantissa, n


def toDec(mantissa, n):
    return int(mantissa * 10 ** (n//2))


def recoverFractional(num, n):
    return int((num * 10**(n//2)) % 10**(n//2))


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
        newBounds = lower, toDec(10, upper_exp) - 1
        return count(newBounds)

    if lower_exp < upper_exp:
        leftPartition = (lower, (10**lower_exp)-1)
        rightPartition = (10**lower_exp, upper)
        return count(leftPartition) + count(rightPartition)

    return 1 + math.floor(upper_mantissa) - math.ceil(lower_mantissa)


count((38593856, 38593862))
