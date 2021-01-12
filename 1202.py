import collections
import heapq
from typing import List


class UnionFind:
    def __init__(self, n):
        self.root: List[int] = list(range(n))

    def union(self, x, y):
        self.root[self.find(x)] = self.find(y)

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        index_used = set(list(range(len(s))))
        uf = UnionFind(len(s))
        result = []
        for x, y in pairs:
            uf.union(x, y)
        m = collections.defaultdict(list)
        for i in range(len(s)):
            heapq.heappush(m[uf.find(i)], s[i])
        for i in range(len(s)):
            result.append(heapq.heappop(m[uf.find(i)]))
        return "".join(result)
