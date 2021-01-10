import collections
from typing import List


class Solution:
    def minimumHammingDistance(
        self, source: List[int], target: List[int], allowedSwaps: List[List[int]]
    ) -> int:
        result = n = len(source)
        self.graph = [set() for i in range(n)]
        for i, j in allowedSwaps:
            self.graph[i].add(j)
            self.graph[j].add(i)
        self.visited = [False] * n
        for i in range(n):
            if self.visited[i]:
                continue
            found = []
            self.dfs(i, found)
            count1 = collections.Counter(source[j] for j in found)
            count2 = collections.Counter(target[j] for j in found)
            result -= sum((count1 & count2).values())
        return result

    def dfs(self, i: int, found: List[int]):
        self.visited[i] = True
        found.append(i)
        for j in self.graph[i]:
            if not self.visited[j]:
                self.dfs(j, found)


class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))

    def union(self, x, y):
        self.root[self.find(x)] = self.find(y)

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]


class Solution1:
    def minimumHammingDistance(
        self, source: List[int], target: List[int], allowedSwaps: List[List[int]]
    ) -> int:
        uf = UnionFind(len(source))
        result = len(source)
        for x, y in allowedSwaps:
            uf.union(x, y)
        m = collections.defaultdict(set)
        for i in range(len(source)):
            m[uf.find(i)].add(i)
        for component in m:
            indexes = m[component]
            A, B = [], []
            for i in indexes:
                A.append(source[i])
                B.append(target[i])
            count1, count2 = collections.Counter(A), collections.Counter(B)
            result -= sum((count1 & count2).values())
        return result


print(Solution1().minimumHammingDistance([1, 2, 3, 4], [2, 1, 4, 5], [[0, 1], [2, 3]]))
