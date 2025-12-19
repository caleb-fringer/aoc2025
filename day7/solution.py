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
