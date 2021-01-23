from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.root: List = list(range(n))

    def union(self, x: int, y: int):
        self.root[self.find(x)] = self.find(y)

    def find(self, x: int) -> int:
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def is_connect(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if not connections:
            return -1
        connection_point = set()
        for x, y in connections:
            connection_point.add(x)
            connection_point.add(y)
        count = n
        uf = UnionFind(n + 1)
        if count > 0:
            for x, y in connections:
                if uf.find(x) == uf.find(y):
                    continue
                uf.union(x, y)
                count -= 1
        return -1 if len(connections) < n - 1 else count - 1
