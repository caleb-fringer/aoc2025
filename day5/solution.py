def preprocess(filepath):
    with open(filepath) as file:
        lines = [line.strip() for line in file.readlines()]
        splitIdx = lines.index("")
        intervals = [tuple(map(int, line.split("-")))
                     for line in lines[:splitIdx]]
        queries = [int(line) for line in lines[splitIdx+1:]]
        return (intervals, queries)


def mergeIntervals(intervals):
    intervals.sort(key=lambda i: i[1])
    result = []
    while len(intervals) > 1:
        curr = intervals.pop()
        pred = intervals.pop()

        if pred[1] >= curr[0]:
            # Need to take min in case the current interval's start time is
            # greater than the predecessor's start time.
            intervals.append((min(pred[0], curr[0]), curr[1]))
        else:
            result.append(curr)
            intervals.append(pred)

    while len(intervals) > 0:
        curr = intervals.pop()
        result.append(curr)

    result.reverse()
    return result


def binarySearch(intervals, val):
    '''
    Initialization: intervals contains non-overlapping intervals in increasing
    order. intervals[lo:hi+1] contains all the intervals in the list. lo <= hi
    If val is an element of any of the intervals in the list, then some
    interval[i] has interval[i][0] <= val <= interval[i][1]
    '''
    lo, hi = 0, len(intervals) - 1

    while lo < hi:
        midpoint = (lo + hi) // 2
        if intervals[midpoint][1] < val:
            lo = midpoint + 1
        else:
            hi = midpoint
    lower, upper = intervals[lo]
    return lower <= val and val <= upper


def partOne(filepath):
    intervals, queries = preprocess(filepath)
    merged = mergeIntervals(intervals)
    count = 0
    for query in queries:
        if binarySearch(merged, query):
            print(f'{query} is fresh!')
            count += 1
    return count


partOne("test.txt")  # 3
partOne("input.txt")  # 509


def partTwo(filepath):
    intervals, queries = preprocess(filepath)
    merged = mergeIntervals(intervals)
    count = 0
    for a, b in merged:
        count += b - a + 1
    return count


partTwo("test.txt")  # 14
partTwo("input.txt")  # 336790092076620
