from functools import reduce
import operator


def preprocess(filepath):
    dataframe = {}
    with open(filepath) as file:
        dataframe["rows"] = [list(line.split()) for line in file.readlines()]
        dataframe["cols"] = [[] for col in dataframe["rows"][0]]
        for row in dataframe["rows"][:-1]:
            for i, v in enumerate(row):
                dataframe["cols"][i].append(int(v))
        dataframe["ops"] = dataframe["rows"][-1]
        return dataframe


def getOperation(op):
    match op:
        case "*":
            return operator.mul
        case "+":
            return operator.add


def partOne(filepath):
    df = preprocess(filepath)
    result = 0
    for op, col in zip(df["ops"], df["cols"]):
        result += reduce(getOperation(op), col, 0 if op == "+" else 1)
    return result


partOne("test.txt")  # 4277556
partOne("input.txt")  # 6169101504608


def preprocessCephalopod(filepath):
    with open(filepath) as file:
        rows = [line.strip("\n") for line in file.readlines()]
        operators = rows[-1].split()

        transposed = ["" for col in range(len(rows[0]))]
        for row in rows[:-1]:
            for i, v in enumerate(row):
                transposed[i] += v

        numbers = [[]]
        i = 0
        for row in transposed:
            if row.strip() == "":
                i += 1
                numbers.append([])
            else:
                numbers[i].append(int(row))
        return [operators, numbers]


def partTwo(filepath):
    operators, rows = preprocessCephalopod(filepath)
    count = 0
    for op, row in zip(operators, rows):
        count += reduce(getOperation(op), row, 0 if op == "+" else 1)
    return count


partTwo("test.txt")  # 3263827
partTwo("input.txt")  # 10442199710797
