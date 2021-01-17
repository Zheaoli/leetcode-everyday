from typing import Dict, Tuple


class Solution:
    def countVowelStrings(self, n: int) -> int:
        visited = {}
        return self.search(visited, n, 5)

    def search(self, visited: Dict[Tuple[int, int], int], n: int, k: int) -> int:
        if (n, k) in visited:
            return visited[(n, k)]
        if n == 1 or k == 1:
            visited[(n, k)] = k
            return k
        visited[(n, k)] = sum(self.search(visited, n - 1, k) for k in range(1, k + 1))
        return visited[(n, k)]


class Solution:
    def countVowelStrings(self, n: int) -> int:
        a, e, i, o, u = 1, 1, 1, 1, 1
        for _ in range(n - 1):
            a, e, i, o, u = a + e + i + o + u, e + i + o + u, i + o + u, o + u, u
        return a + e + i + o + u
