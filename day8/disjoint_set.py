class DisjointSet:
    def __init__(self, n):
        self.parents = list(range(n))

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        repX, repY = self.find(x), self.find(y)
        if repX == repY:
            return False

        self.parents[repX] = repY
        return True

    def __repr__(self):
        return str(self.parents)

    def __str__(self):
        return str(self.parents)


if __name__ == "__main__":
    graph = DisjointSet(8)
    graph.union(0, 1)
    graph.union(1, 6)
    graph.union(2, 4)
    graph.union(2, 7)
    graph.union(3, 5)
    graph  # [1, 6, 4, 5, 7, 5, 6, 7]
    graph.compress()  # None
    graph  # [6, 6, 7, 5, 7, 5, 6, 7]
