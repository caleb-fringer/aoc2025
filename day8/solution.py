from collections import Counter
from functools import reduce
from disjoint_set import DisjointSet


def preprocess(filepath):
    with open(filepath) as file:
        return [tuple(map(int, line.split(","))) for line in file.readlines()]


class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v
        self.weight = euclideanDistance(u, v)

    def __lt__(self, other):
        return self.weight < other.weight

    def __repr__(self):
        return f'{self.u}<->{self.v}: {self.weight}'


def euclideanDistance(u, v):
    a, b, c = u
    d, e, f = v
    return (d-a)**2 + (e-b)**2 + (f-c)**2


def generateEdges(vertices):
    edges = []
    n = len(vertices)
    for i in range(n-1):
        for j in range(i+1, n):
            e = Edge(vertices[i], vertices[j])
            edges.append(e)

    return edges


def solution(filepath, num_joins):
    vertices = preprocess(filepath)
    edges = generateEdges(vertices)
    edges.sort(key=lambda e: e.weight, reverse=True)
    keymap = {v: i for i, v in enumerate(vertices)}
    graph = DisjointSet(len(vertices))

    for i in range(num_joins):
        edge = edges.pop()
        u, v = keymap[edge.u], keymap[edge.v]

        if graph.union(u, v):
            i += 1

    for i in range(len(graph.parents)):
        graph.find(i)

    freq = Counter(graph.parents)
    largest = [f[1] for f in freq.most_common(3)]
    return reduce(lambda a, x: a * x, largest, 1)


solution("test.txt", 10)  # 40
solution("input.txt", 1000)  # 115885

'''
Part Two
'''


def solution2(filepath):
    vertices = preprocess(filepath)
    edges = generateEdges(vertices)
    edges.sort(key=lambda e: e.weight)
    keymap = {v: i for i, v in enumerate(vertices)}
    graph = DisjointSet(len(vertices))

    a, b = None, None
    for edge in edges:
        u, v = keymap[edge.u], keymap[edge.v]

        if graph.union(u, v):
            a, b = edge.u, edge.v

    return a[0] * b[0]


solution2("test.txt")  # 25272
solution2("input.txt")  # 274150525
