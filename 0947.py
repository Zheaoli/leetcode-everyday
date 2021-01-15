from typing import List, Dict


class UnionFind:
    def __init__(self):
        self.root: Dict[int, int] = {}

    def union(self, x: int, y: int):
        self.root.setdefault(x, x)
        self.root.setdefault(y, y)
        self.root[self.find(x)] = self.find(y)

    def find(self, x: int) -> int:
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def is_connect(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def __len__(self):
        return len({self.find(x) for x in self.root})


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind()
        for x, y in stones:
            uf.union(x, y + 2000000000)
        return len(stones) - len(uf)


print(Solution().removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))
