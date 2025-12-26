def preprocess(filepath):
    with open(filepath) as file:
        rows = [line.strip() for line in file.readlines()]
        result = []
        for row in rows:
            r = []
            for i, v in enumerate(row):
                if v == "S" or v == "^":
                    r.append(i)
            result.append(r)
        return result


preprocess("test.txt")[0][0]


def partOne(filepath):
    rows = preprocess(filepath)
    columns = set()
    columns.add(rows[0][0])
    splitCount = 0
    for row in rows:
        for splitter in row:
            if splitter in columns:
                columns.remove(splitter)
                columns.update([splitter-1, splitter+1])
                splitCount += 1
    return splitCount


partOne("test.txt")  # 21
partOne("input.txt")  # 1490


def preprocessTwo(filepath):
    with open(filepath) as file:
        return [line.strip() for line in file.readlines()]


def partTwo(filepath):
    rows = preprocessTwo(filepath)

    cache = {}

    def dfs(pos):
        nonlocal rows
        i, j = pos
        if i >= len(rows):
            return 1
        if i < 0 or j < 0 or j >= len(rows[0]):
            return 0
        if rows[i][j] == "^":
            return dfs((i, j-1)) + dfs((i, j+1))

        if (i+1, j) not in cache:
            cache[(i+1, j)] = dfs((i+1, j))
        return cache[(i+1, j)]

    start = rows[0].find("S")
    return dfs((0, start))


partTwo("test.txt")  # 40
partTwo("input.txt")  # 3806264447357
