'''
Observations:
Given a bank of length n:
The tens digit can only be in [0, n-1)
The ones digit can only be in [1, n)

If I ever see a digit greater than the tens place or the ones place, I should
always take it, with priority to upgrading the tens digit.

If I take an upgrade to the tens place at index i, I need to update the ones
digit to be bank[i+1].

So if I initialize the stack with the first element, then I do the following:
Iterate from i = [1, n-1).
While bank[i] > stack[-1]:
    pop from stack
push bank[i]

Then I can take 10*stack[0] + stack[1] to make my maximum joltage. However,
if the the last element causes me to pop all of my stack elements, I may need
to add the last element in the bank as the ones place. Additionally, it could
be the case that the last element in the list is greater than stack[1], in
which case I need to return 10*stack[0] + max(stack[1], bank[-1]).
'''
import functools


def processInput(input_file):
    with open(input_file) as file:
        banks = [[int(digit) for digit in line if digit.isdigit()]
                 for line in file.readlines()]
    return banks


def getMaxJoltageOne(bank):
    stack = []
    for i in range(len(bank)-1):
        while len(stack) > 0 and bank[i] > stack[-1]:
            stack.pop()
        stack.append(bank[i])

    if len(stack) < 2:
        return 10*stack[0] + bank[-1]
    else:
        return 10*stack[0] + max(bank[-1], stack[1])


def solve(input_file, maxJoltageFunc):
    return functools.reduce(lambda a, bank: a + maxJoltageFunc(bank),
                            processInput(input_file), 0)


getMaxJoltageOne([9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1])  # 98
getMaxJoltageOne([8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9])  # 89
getMaxJoltageOne([2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 7, 8])  # 78
getMaxJoltageOne([8, 1, 8, 1, 8, 1, 9, 1, 1, 1, 1, 2, 1, 1, 1])  # 92

solve("test.txt", getMaxJoltageOne)  # 357
solve("input.txt", getMaxJoltageOne)  # 16887


'''
Part Two
'''


def getMaxJoltageTwo(bank):
    stack = []
    n = len(bank)
    for i in range(n):
        while len(stack) > 0 and len(stack) + n - i > 12 and bank[i] > stack[-1]:
            stack.pop()
        stack.append(bank[i])

    while len(stack) > 12:
        stack.pop()

    return functools.reduce(lambda a, x: a*10 + x, stack, 0)


tests = processInput("test.txt")
getMaxJoltageTwo(tests[0])
getMaxJoltageTwo(tests[1])
getMaxJoltageTwo(tests[2])
getMaxJoltageTwo(tests[3])

solve("test.txt", getMaxJoltageTwo)  # 3121910778619
solve("input.txt", getMaxJoltageTwo)  # 167302518850275
