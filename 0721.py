from typing import List


class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))

    def union(self, x, y):
        self.root[self.find(x)] = self.find(y)

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        if not accounts:
            return []
        uf = UnionFind(10000)
        visited = {}
        for i in range(len(accounts)):
            for email in accounts[i][1:]:
                if email in visited:
                    uf.union(visited[email], i)
                else:
                    uf.union(i, i)
                visited[email] = i
        temp_data = {}
        for i in range(len(accounts)):
            temp_data.setdefault(uf.find(i), []).append(i)
        results = []
        for item in temp_data.values():
            names = []
            emails = []
            for i in item:
                names.append(accounts[i][0])
                emails.extend(accounts[i][1:])
            results.append(list(set(names)) + sorted(list(set(emails))))
        return results
