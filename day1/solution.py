input = []
with open("input.txt", "r") as file:
    input = file.readlines()


def partOne(input):
    count = 0
    pos = 50
    rotations = [(line[0], int(line[1:])) for line in input]

    for direction, amount in rotations:
        amount = -1 * amount if direction == "L" else 1 * amount
        pos = (pos + amount) % 100
        if pos == 0:
            count += 1

    return count


partOne(input)


def partTwo(input):
    count = 0
    pos = 50
    rotations = [(line[0], int(line[1:])) for line in input]

    def rotationHelper(pos, direction, amount):
        result = amount // 100
        amount = amount % 100
        rotation = -1*amount if direction == "L" else 1*amount
        # If rotation left from 0, need to reset the position so we don't
        # double-count a click.
        if pos == 0 and rotation < 0:
            pos = 100
        pos = pos + rotation
        if pos >= 100 or pos <= 0:
            result += 1
        pos %= 100
        return pos, result

    for direction, amount in rotations:
        pos, c = rotationHelper(pos, direction, amount)
        count += c

    return count


test = []
with open("test.txt", "r") as file:
    test = file.readlines()

partTwo(test)

partTwo(input)
