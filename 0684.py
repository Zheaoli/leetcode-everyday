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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges:
            return []
        uf = UnionFind(2000)
        for i in edges:
            if uf.find(i[0]) == uf.find(i[1]):
                return i
            uf.union(i[0], i[1])
        return []


print(Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3]]))
