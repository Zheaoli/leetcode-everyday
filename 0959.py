from typing import List


class UnionFind:
    def __init__(self):
        self.root = {}

    def union(self, x, y):
        self.root[self.find(x)] = self.find(y)

    def find(self, x):
        self.root.setdefault(x, x)
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def __len__(self):
        return len(set({self.find(x) for x in self.root.keys()}))


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        uf = UnionFind()
        for i in range(len(grid)):
            for j in range(len(grid)):
                if i > 0:
                    uf.union((i - 1, j, 2), (i, j, 0))
                if j > 0:
                    uf.union((i, j - 1, 1), (i, j, 3))
                if grid[i][j] != "/":
                    uf.union((i, j, 0), (i, j, 1))
                    uf.union((i, j, 3), (i, j, 2))
                if grid[i][j] != "\\":
                    uf.union((i, j, 0), (i, j, 3))
                    uf.union((i, j, 1), (i, j, 2))
        return len(uf)
